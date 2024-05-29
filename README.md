# 聊天记录词云生成

## 1 安装依赖

```bash
pip install -r requirements.txt
```

## 2 准备数据

在 `data` 文件夹中准备以 `.log` 结尾的聊天记录文件，内容形如：

```json
{"user_name": "alias1", "content":  "+1"}
...
```

## 3 修改配置

在 `main.py` 中

```python
username = 'XXX'  # 某人的姓名
user_alias = {
    username: [
        'aaa',    # 该人使用的所有昵称
    ]
}
```

## 4 运行

```bash
python main.py
```

结果保存在 `images` 文件夹中。