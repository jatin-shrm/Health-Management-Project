#Health management system for 3 person Harry, Hammad and Rohan
#In this program we are giving input and also we are retrieving input
def getdate():
    import datetime
    return datetime.datetime.now()
#here we are defing function for giving input
def writeinput(x):
    if x==1:
        a=int(input("Press 1 for exercise or 2 for food\n"))
        if a==1:
            Give_value=input("What exercise did yo do?\n")
            with open("harry_exercise.txt","a") as f:
                f.write(str(str([getdate()]))+ ": " + Give_value + "\n")
            print("Successfully written")
        elif a==2:
            Give_value=input("What food did you eat\n")
            with open("harry_food.txt","a") as f:
                f.write(str(str([getdate()]))+ ": "+ Give_value + "\n")
            print("Successfully written")
    elif x==2:
        a = int(input("Press 1 for exercise or 2 for food\n"))
        if a==1:
            Give_value = input("What exercise did yo do?\n")
            with open("hammad_exercise.txt","a") as f:
                f.write(str(str([getdate()]))+ ": " + Give_value + "\n")
            print("Successfully written")
        elif a==2:
            Give_value=input("What food did you eat\n")
            with open("hammad_food.txt","a") as f:
                f.write(str(str([getdate()]))+ ": "+ Give_value + "\n")
            print("Successfully written")
    elif x==3:
        a = int(input("Press 1 for exercise or 2 for food\n"))
        if a == 1:
            Give_value = input("What exercise did yo do?\n")
            with open("rohan_exercise.txt", "a") as f:
                f.write(str(str([getdate()]))+ ": " + Give_value + "\n")
            print("Successfully written")
        elif a == 2:
            Give_value = input("What food did you eat\n")
            with open("rohan_food.txt", "a") as f:
                f.write(str(str([getdate()]))+ ": " + Give_value + "\n")
            print("Successfully written")

#here we are defining function for retrieving input
def retrieveinput(y):
    if y==1:
        a = int(input("Press 1 for exercise or 2 for food\n"))
        if a==1:
            with open("harry_exercise.txt") as f:
                for i in f:
                    print(i,end=" ")
        elif a==2:
            with open("harry_food.txt") as f:
                for i in f:
                    print(i,end=" ")
    if y==2:
        a = int(input("Press 1 for exercise or 2 for food\n"))
        if a==1:
            with open("hammad_exercise.txt") as f:
                for i in f:
                    print(i,end=" ")
        elif a==2:
            with open("hammad_food.txt") as f:
                for i in f:
                    print(i,end=" ")
    if y==3:
        a = int(input("Press 1 for exercise or 2 for food\n"))
        if a==1:
            with open("rohan_exercise.txt") as f:
                for i in f:
                    print(i,end=" ")
        elif a==2:
            with open("rohan_food.txt") as f:
                for i in f:
                    print(i,end=" ")


print("Health Management System")
num=int(input("Press 1 for giving input or 2 for retrieving input\n"))
if num==1:
    num1=int(input("Press 1 for Harry, 2 for Hammad or 3 for Rohan\n"))
    writeinput(num1)
elif num==2:
    num2=int(input("Press 1 for Harry, 2 for Hammad or 3 for Rohan\n"))
    retrieveinput(num2)