import random, easygui
secret = random.randint(1, 99)
guess = 50
tries = 0
easygui.msgbox("嘿，我是海盗王，我有个秘密! 秘密是1到99间的一个数，给你6次机会猜哦")
while guess != secret and tries <6:
    guess = int(easygui.enterbox("输入你猜的数：", default=str(guess)))
    if guess < secret:
        easygui.msgbox("这是第" + str(tries + 1) + "次。太小了，笨蛋")
    elif guess > secret:
        easygui.msgbox("这是第" + str(tries + 1) + "次。太大了，呆子")

    tries += 1

if guess == secret:
    easygui.msgbox("你真厉害，猜对了！共猜了" + str(tries) + "次")
else:
    easygui.msgbox("你没机会了，下次好运！我的秘密是：" + str(secret))


