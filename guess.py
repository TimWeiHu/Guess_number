import random
num = random.randint(1, 100)
count = 0
while True:
    count = count + 1
    print('')
    print('第', count, '次')
    guess = input('請猜數字：')
    guess = int(guess)
    if guess < num:
        print('答案比', guess, '大')
    elif guess > num:
        print('答案比', guess, '小')
    else:
        print('終於猜對了！')
        break
print('')
print('共猜了', count, '次')
