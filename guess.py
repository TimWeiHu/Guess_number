import random
num = random.randint(1, 100)

while True:
    guess = input('猜數字：')
    guess = int(guess)
    if guess < num:
        print('答案比', guess, '大')
    elif guess > num:
        print('答案比', guess, '小')
    else:
        print('終於猜對了！')
        break

