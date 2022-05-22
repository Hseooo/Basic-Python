import random
while True:
    goal_num1= random.randrange(10)
    goal_num2= random.randrange(10)
    goal_num3= random.randrange(10)
    if goal_num1 != goal_num2 != goal_num3:
        goal_num1 = str(goal_num1)
        goal_num2 = str(goal_num2)
        goal_num3 = str(goal_num3)
        break
        
goal_num = [goal_num1, goal_num2, goal_num3]
print(goal_num)
while True:
    num = input("3자리 숫자 입력:")
    user = list(num)

    ballcount = 0
    strikecount = 0

    i=0
    for i in range(3):
        if goal_num[i]==user[i]:
            strikecount +=1
        elif goal_num[i] in user:
            ballcount += 1

    if strikecount == 3:
        print("홈런")
        break
