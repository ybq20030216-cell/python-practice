"""
第 6 天 · 05_requests调用 参考答案
==============================

练习文件里已经给了骨架，这里补上自检要用的部分。
重点不是代码，是你跑完之后能回答那几个问题。
"""

import os
import json
import requests

API_URL = "https://api.deepseek.com/chat/completions"
MODEL = "deepseek-chat"


def call_llm(prompt, temperature=1.0, verbose=False):
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        raise RuntimeError("没找到 DEEPSEEK_API_KEY，先设置环境变量再重开终端")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "你是一个简洁的助手。"},
            {"role": "user", "content": prompt},
        ],
        "temperature": temperature,
        "max_tokens": 200,
    }

    resp = requests.post(API_URL, headers=headers, json=payload, timeout=30)

    # 先看状态码，再取内容
    # 401 = key 错了，402 = 余额不足，429 = 请求太频繁
    if resp.status_code != 200:
        print("请求失败，状态码：", resp.status_code)
        print(resp.text)
        return None

    data = resp.json()
    print(json.dumps(data, ensure_ascii=False, indent=2))

    return data["choices"][0]["message"]["content"]

    if verbose:
        print(json.dumps(data, ensure_ascii=False, indent=2))

    return data["choices"][0]["message"]["content"]


if __name__ == "__main__":
    # ---- 第 1、2 步：跑通 + 看完整 JSON ----
    print("=== 正常调用 ===")
    print(call_llm("用一句话解释什么是大模型", verbose=True))




    # ---- 第 3 步：对比 temperature ----
    print("\n=== temperature = 0 ===")
    print(call_llm("给我起一个宠物名字", temperature=0))
    print(call_llm("给我起一个宠物名字", temperature=0))

    print("\n=== temperature = 1.5 ===")
    print(call_llm("给我起一个宠物名字", temperature=1.5))
    print(call_llm("给我起一个宠物名字", temperature=1.5))


# ---------------- 跑完之后，你应该能回答 ----------------
#
# 1. 返回的 JSON 结构：
#    data["choices"][0]["message"]["content"]
#    外层是 choices 列表（可以一次要多个回答），
#    里面是 message，再里面才是 content 文字。
#
# 2. role 有哪几种：
#    system —— 设定模型的角色和行为，放在最前面
#    user   —— 用户说的话
#    assistant —— 模型说过的话（多轮对话时要把它塞回去）
#
# 3. max_tokens 设太小的后果：
#    回答会被硬生生截断，而且多数情况下不会报错，
#    你只会看到一句话说到一半就没了。所以排查「回答不完整」时先看这个值。
#
# 4. temperature 的观察：
#    0 附近同一个 prompt 结果几乎一样；
#    调高之后每次都不一样，也更容易跑题。
#    要稳定输出（比如抽结构化数据）就用低值。
#
# 5. key 改错一个字符：
#    返回 401，属于认证失败。程序应该提示「key 有问题」而不是崩掉。

# import os
# import json
# import requests
#
# API_URL = "https://api.deepseek.com/chat/completions"
# MODEL = "deepseek-chat"
#
#
# def call_llm(prompt, temperature=1.0):
#     api_key = os.environ.get("DEEPSEEK_API_KEY")
#     if not api_key:
#         raise RuntimeError("没找到 DEEPSEEK_API_KEY，先去设置环境变量")
#
#     headers = {
#         "Authorization": f"Bearer {api_key}",
#         "Content-Type": "application/json",
#     }
#     payload = {
#         "model": MODEL,
#         "messages": [
#             {"role": "system", "content": "你是一个简洁的助手。"},
#             {"role": "user", "content": prompt},
#         ],
#         "temperature": temperature,
#         "max_tokens": 200,
#     }
#
#     resp = requests.post(API_URL, headers=headers, json=payload, timeout=30)
#     resp.raise_for_status()
#     data = resp.json()
#
#     # 第 2 步：把下面这行取消注释，看完整 JSON
#     print(json.dumps(data, ensure_ascii=False, indent=2))
#
#     return data["choices"][0]["message"]["content"]
#
#
# if __name__ == "__main__":
#     print(call_llm("用一句话解释什么是大模型"))
