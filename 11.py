text = "今天 天气 不错 今天 心情 不错 今天 我 想 出去 玩"


def count_words(text):
    """返回 {词: 出现次数}"""
    counts = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts

def print_top(counts, n):
    """打印出现次数最多的前 n 个词"""
    items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    for word, count in items[:n]:
        print(f"{word}：{count} 次")


class Pet:
    def __init__(self, name, sound):

        self.name = name
        self.sound = sound
    def speak(self):

        print(f"{self.name}说:{self.sound}")

if __name__ == "__main__":
    print("先完成上面三个部分，再把下面几行取消注释跑一遍")
    print(count_words(text))
    print_top(count_words(text), 3)
    p = Pet("小白", "汪汪")
    p.speak()
