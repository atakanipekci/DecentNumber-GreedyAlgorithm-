#Decent Number:
#A Decent Number having N digits has the following properties:
#1. Its digits can only be 3's and/or 5's.
#2. The number of 3's it contains is divisible by 5.
#3. The number of 5's it contains is divisible by 3.
#4. If there is more than one such number, we pick the largest one.
#decentNumber function takes 1 parameter called digits which
#obviously means the amount of digits the decent number
#we are looking for can have.
#Before starting to explain the algorithm you should know that
#5s always have to be at the start(by start i mean the left side)
#since we are looking for the maximum number. For example if the
#digits =8 then 35353533,53535333 etc. can provide all the
#properties we need but for it to be the largest one all 5s should be
#at the start so the answer is 55533333.
#This algorithm uses a greedy approach where the greedy choice here
#is that since we are always looking for the largest one we will
#assume that all digits are 5s. The important part here is that
#we always have to be sure that the number of 5s are divisible by 3
#and number of 3s are divisible by 5. Since we were assuming that
#all digits are 5s at start we have to check if it is divisible by 3.
#If it is then we found our number. For example if digits=3 then the
#result is 555. If not we have to switch some 5s with 3s. Since the
#amount of 3s have to be divisible by 5 we can only switch 5x amount of
#digits. The trick here is that you should keep in mind that no matter
#the number that gives the remainder of 2 when divided by 3,
#subtracting 5 from it will always make it divisible by 3. And if the
#remainder is 1 then subtracting 5 from it will make it so that the
#remainder is 2 then subtracting another 5 will make it divisible by 3.
#Also don't forget that we have to keep the max amount of 5s we can
#have so the number of switches should be minimum. As explained before
#If the remainder is 2 then we have to switch 5 digits with 3s from the
#end. If the remainder is 1 then we have to switch 10 digits. And of
#course there is a possibility that there are no decent numbers that has
#digits(parameter) amount of digits. For example if digits = 4
#then there are no decent numbers since the sum of no of 5s and no of 3s have
#to be equal to digits and they have to be divisible by 3 and 5 respectively.
#Same goes for 1,2 and 7.

import sys


def decentNumber(digits):
    numberOfFives=digits
    if(numberOfFives%3==2):
        numberOfFives-=5
    elif(numberOfFives%3==1):
        numberOfFives-=10
    if(numberOfFives<0):
        return "-1"
    else:
        numberOfThrees=digits-numberOfFives
        return numberOfFives*'5'+numberOfThrees*'3'
        
        
dn = decentNumber(1)
print(dn)
#Output: -1
dn = decentNumber(3)
print(dn)
#Output: 555
dn = decentNumber(5)
print(dn)
#Output: 33333
dn = decentNumber(13)
print(dn)
#Output: 55555533333
