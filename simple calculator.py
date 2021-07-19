#Nahin CDR
#Date : 17 - 07 - 2021

global x
global y
print("Hello it Nahin the Coder !")
x = int(input("Master input first number "))
y = int(input("Master input second number "))
while 1 :
    print("Enter your choice : ")
    print("1 for Normal Division \n2 for Floor division \n3 for modulo division\n4 for addition\n5 for subtraction ")
    n = int(input("choice : "))
    if n == 1:
        print("Normal division : ", x / y)
    elif n == 2:
        print("Floor division : ", x // y)
    elif n == 3:
        print("Modulo division : ", x % y)
    elif n == 4:
        print("Addition : ",x+y)
    elif n == 5:
        print("Subtraction : ",x-y)
    else :
        print("wrong choice")
        break



