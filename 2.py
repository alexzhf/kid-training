import random
secret = random.randint(1, 99)
guess = 0
tries = 0
print("嘿，我是海盗王，我有个秘密")
print("秘密是1到99间的一个数，给你6次机会猜哦")
while guess != secret and tries <6:
    guess = int(input("输入你猜的数："))
    if guess < secret:
        print("太小了，笨蛋")
    elif guess > secret:
        print("太大了，呆子")

    tries = tries +1

if guess == secret:
    print("你真厉害，猜对了！")
else:
    print("你没机会了，下次好运！")
    print("我的秘密是：", secret)


