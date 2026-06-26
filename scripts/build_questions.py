#!/usr/bin/env python3
"""
scripts/build_questions.py
=======================
将 questions/*.csv 转换为 questions/*.json 并推送到 GitHub。

使用方法:
    python scripts/build_questions.py [模块名]

示例:
    python scripts/build_questions.py           # 构建所有模块
    python scripts/build_questions.py yanyu     # 只构建言语理解
    python scripts/build_questions.py panduan   # 只构建判断推理
"""
import subprocess, urllib.request, json, base64, csv, io, sys, os

tok = subprocess.check_output(['gh', 'auth', 'token']).decode().strip()
GH = 'https://api.github.com/repos/feiguang50-hub/study_assistant/contents'
HEADERS = {'Authorization': f'token {tok}', 'Accept': 'application/vnd.github.v3+json'}

def api_get(path):
    req = urllib.request.Request(f'{GH}/{path}', headers=HEADERS)
    return json.loads(urllib.request.urlopen(req, timeout=10).read())

def api_put(path, content_bytes, sha, msg):
    data = json.dumps({
        'message': msg,
        'content': base64.b64encode(content_bytes).decode(),
        'sha': sha
    }).encode()
    req = urllib.request.Request(
        f'{GH}/{path}', method='PUT', data=data,
        headers={**HEADERS, 'Content-Type': 'application/json'}
    )
    return json.loads(urllib.request.urlopen(req, timeout=10).read())

MODULE_NAMES = {
    'changshi': '常识判断',
    'yanyu':    '言语理解',
    'shuliang': '数量关系',
    'panduan':  '判断推理',
    'ziliao':   '资料分析',
}

def parse_csv(csv_text):
    """解析 CSV，返回题目列表"""
    # 去掉 BOM（文件可能带 BOM）
    if csv_text.startswith('\ufeff'):
        csv_text = csv_text[1:]
    # 用显式字段名，避免表头格式问题
    fieldnames = ['id', 'type', 'knowledge', 'question', 'options', 'answer', 'explanation']
    reader = csv.DictReader(io.StringIO(csv_text), fieldnames=fieldnames)
    # 第一行是表头，跳过
    next(reader, None)
    questions = []
    for row in reader:
        # options 用 ||| 分隔
        options = [o.strip() for o in row['options'].split('|||')]
        questions.append({
            'id':          row['id'].strip(),
            'type':        row['type'].strip(),
            'knowledge':   row['knowledge'].strip(),
            'question':    row['question'].strip(),
            'options':     options,
            'answer':      int(row['answer'].strip()),
            'explanation': row['explanation'].strip(),
        })
    return questions

def build_module(mod):
    csv_path = f'questions/{mod}.csv'
    json_path = f'questions/{mod}.json'
    name = MODULE_NAMES.get(mod, mod)

    print(f'Building {name} ({mod})...')

    # 读取 CSV
    csv_data = api_get(csv_path)
    import base64 as b64
    csv_text = b64.b64decode(csv_data['content']).decode('utf-8-sig')
    csv_sha = csv_data['sha']

    questions = parse_csv(csv_text)
    print(f'  CSV: {len(questions)} questions read')

    # 生成 JSON
    data = {'module': mod, 'moduleName': name, 'questions': questions}
    json_bytes = (json.dumps(data, ensure_ascii=False, indent=2) + '\n').encode('utf-8')

    # 验证 JSON
    try:
        json.loads(json_bytes)
        print(f'  JSON: valid')
    except Exception as e:
        print(f'  JSON ERROR: {e}')
        return

    # 推送
    json_sha = api_get(json_path)['sha']
    result = api_put(json_path, json_bytes, json_sha,
                     f'build: regenerate {name} JSON from CSV ({len(questions)} questions)')
    print(f'  Pushed: {result["commit"]["sha"][:7]}')

if __name__ == '__main__':
    args = sys.argv[1:]

    if not args:
        # 构建所有模块
        for mod in MODULE_NAMES:
            build_module(mod)
            print()
    else:
        for arg in args:
            if arg in MODULE_NAMES:
                build_module(arg)
                print()
            else:
                print(f'Unknown module: {arg}')
                print(f'Available: {list(MODULE_NAMES.keys())}')
