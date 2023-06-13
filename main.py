import random

keep_guessing = True
target_number = random.randint(1, 100)  # 生成一个1到100的随机数作为目标数字
guess_count = 0  # 记录用户猜测的次数

while keep_guessing:
    guess = input("猜一个1到100之间的数字：")  # 提示用户猜测一个数字

    try:
        guess = int(guess)  # 将用户输入的字符串转换为整数
        guess_count += 1  # 猜测次数加1
        # guess_count = guess_count + 1

        if guess == target_number:  # 如果猜测的数字等于目标数字
            print("你猜了" + str(guess_count) + "次。")
            print("恭喜你，猜对了！")
            keep_guessing = False  # 结束循环，猜测游戏结束
        else:
            if guess > target_number:  # 如果猜测的数字大于目标数字
                print("数字太大了！")
            else:
                print("数字太小了！")

        if guess_count >= 10:  # 如果猜测次数达到10次
            
            print("你已经达到最大猜测次数。")
            choice = input("Do you want continue y/n ?")

            if choice.lower() == "n":
                keep_guessing = False  # 结束循环，猜测游戏结束

    except ValueError as errInfo:
        
        print(errInfo.args[0])
        continue

print("游戏结束！")

