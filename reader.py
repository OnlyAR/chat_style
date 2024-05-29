import os
import re
import json

data_path = os.path.join(os.path.dirname(__file__), 'data')


def clean_quote(s: str):
    """
    清洗字符串中的引用
    :param s:
    :return:
    """
    if "\n- - - - - - - - - - - - - - -\n" in s:
        s = s.split("\n- - - - - - - - - - - - - - -\n")[-1]
    if re.search(r'\[.*\]', s):
        s = re.sub(r'\[.*\]', '', s)
    return s


def read_messages(user_name_maps):
    """
    读取指定用户的的聊天记录
    :param user_name_maps: {'user_name': ['alias', ...], ...}
    :return: data_corpus: {'user_name': [json1, ...], ...}
    """
    data_corpus = {}
    lines = []
    for files in os.listdir(data_path):
        if files.endswith('.log'):
            with open(os.path.join(data_path, files), 'r', encoding='utf-8') as f:
                lines += f.readlines()
    for line in lines:
        js_obj = json.loads(line)
        for user_name in user_name_maps:
            alias = user_name_maps[user_name]
            if js_obj['user_name'] in alias:
                if user_name not in data_corpus:
                    data_corpus[user_name] = []
                js_obj['content'] = clean_quote(js_obj['content'])
                data_corpus[user_name].append(js_obj)
    return data_corpus
