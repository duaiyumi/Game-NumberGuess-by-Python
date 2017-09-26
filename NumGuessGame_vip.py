# coding=utf-8
    # 方便出中文版，采用utf-8字符

import random
secret = random.randint(1,100)
guess = int(0)
tries = int(0)
    # 加载随机数模块，生成了一个1-99的随机整数为答案。并将"猜的数字(guess)"和"次数(tries)"初始化。

print("我是个可怕的海盗，罗伯特。我有个秘密！")
print("猜一个0-99的整数，你有6的机会。")
    # 开场语，"我是可怕的海盗罗伯特，我有个秘密！"
    # 开场语，"猜一个0-99的整数，你有6次机会。"

while int(guess) != secret and tries < 6:
    guess = input("选一个吧：")
    # 游戏开始条件判定，当猜的数字不等于答案，且猜的次数有效。

    if int(guess) == 724:
        print(secret)
    # 为"BF"预留的后门，直接查看随机整数。默认值为724。

    elif int(guess) < 1 or int(guess) > 99:
        print("超出范围啦！")
    # 检测用户输入数值是否符合范围。

    elif int(guess) < secret and 1 < int(guess) < 100:
        print("太低了！")
    # 用户输入数值低于随机整数。

    elif int(guess) > secret and 1 < int(guess) < 100:
        print("高了！高了！")
    # 用户输入数值高于随机整数。

    tries = tries + 1
    # 每结束一个回合，次数+1。

if int(guess) == secret:
    print("漂亮！你明白了吗？！我找到了我的秘密！")
    # 用户猜对了，输出提示。

elif tries == 6:
    print("别再猜测了！下次好运，伙计！")
    print("秘密号码是：", secret)
    # 用户机会用完了，输出答案。
