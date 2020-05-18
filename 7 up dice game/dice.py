import random
import time
dice=[1,2,3,4,5,6]
print('ALL THE BEST')
print('SELECT FROM THE 3 CHOICES')
choice1=random.randrange(2,6)
print('choice1 is select the no from 2 to 5')
choice2=random.randrange(6,8)
print('choice2 is select the no from 6 to 8')
choice3=random.randrange(9,13)
print('choice3 is select the no from 9 to 12')
ans=int(input('enter your choice:'))

if ans==1:
    dice1=random.choice(dice)
    print('DICE IS ROLLING.....')
    time.sleep(2)
    print('the value of the first dice is:',dice1)
    dice2=random.choice(dice)
    print('DICE IS ROLLING.....')
    time.sleep(2)
    print('the value of the second dice is:',dice2)
    d=dice1+dice2
    print('the sum of the 2 die is:',d)
    if d<=5:
        print('YOU WIN')
    else:
        print('YOU LOSE')
    
    
elif ans==2:
     dice1=random.choice(dice)
     print('DICE IS ROLLING.....')
     time.sleep(2)
     print('the value of the first dice is:',dice1)
     dice2=random.choice(dice)
     print('DICE IS ROLLING.....')
     time.sleep(2)
     print('the value of the second dice is:',dice2)
     d=dice1+dice2
     print('the sum of the 2 die is:',d)
     if ((d>=6) and (d<=8)):
        print('YOU WIN')
     else:
        print('YOU LOSE')

else:
     dice1=random.choice(dice)
     print('DICE IS ROLLING.....')
     time.sleep(2)
     print('the value of the first dice is:',dice1)
     dice2=random.choice(dice)
     print('DICE IS ROLLING.....')
     time.sleep(2)
     print('the value of the second dice is:',dice2)
     d=dice1+dice2
     print('the sum of the 2 die is:',d)
     if (d>=9) and (d<=12):
        print('YOU WIN')
     else:
        print('YOU LOSE')
    
    
