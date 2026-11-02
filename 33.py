"""任务 A：把下面的 profile 存成 data.json
    提示：json.dump(对象, 文件对象, ensure_ascii=False)

任务 B：从 data.json 读回来，打印里面的 name
    提示：json.load(文件对象)

任务 C：读一个不存在的字段，用 try/except 抓住，
    打印 "没有这个字段"，不要让程序崩

自检：
- 把 data.json 手工删掉，再运行，程序应该打印友好提示而不是一屏红色报错
- 你能说出 with open(...) as f: 这种写法的好处吗（忘记关闭文件会怎样）

固定写法，背下来：
    with open("文件.json", "r", encoding="utf-8") as f:
        data = json.load(f)
"""

import os
import json

profile = {
    "name": "小明",
    "age": 22,
    "city": "厦门",
    "skills": ["Python", "Git"],
}

# ---- 任务 A ----
def save(profile, path="data.json"):
    with open(path , "w" , encoding="utf_8") as f:
        json.dump(profile,f,ensure_ascii=False,indent=2)



# ---- 任务 B ----
def load(path="data.json"):
    with open(path,"r",encoding="utf_8") as f:
        return json.load(f)

# ---- 任务 C ----
def get_age(path="data.json"):
    # 要求：字段不存在时打印 "没有这个字段"，并返回 None
    try:
        data = load(path)
        return data["height"]

    except FileNotFoundError:
        # 文件被删了或者路径写错了
        print("找不到 data.json，请先运行 save()")
        return None

    except KeyError:
        # 文件读到了，但没有 age 这个字段
        # 想把这一支试出来：把下面那句改成 data["height"]
        print("没有这个字段")
        return None

if __name__ == "__main__":
    print("先完成三个函数，再取消下面的注释")
    save(profile)
    data = load()
    print(data["name"])
    print("年龄：", get_age())

    # 试试把这些逐个取消注释，看分别报什么、被哪一支接住
    # os.remove("data.json"); get_age()      # ← 触发 FileNotFoundError
    # print(load()["height"])

