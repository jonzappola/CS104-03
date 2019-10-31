#Sum/Average Program
#Jonathan Zappola
#s1248773

numberList = []
tot = 0
for x in range (0,20):
    num = int(input("Enter a number: "))
    numberList.append(num)
for x in range (0,20):
    tot = tot + numberList[x]
print("The sum of the numbers you entered is: ", tot)
print("The average of the numbers you entered is: ", tot/20)

    
