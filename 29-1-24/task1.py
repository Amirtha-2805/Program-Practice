# mark=int(input("Enter your mark:"))
# if mark>35:
#     print("pass")
# else:
#     print("Fail")
    
# number=int(input("Enter a number:"))
# if (number%3==0) and (number%5==0):
#     print("The number is divisible by both 3 and 5")
# else:
#     print("The number doesn't divisible by both 3 and 5") 


# score=int(input("Enter your score"))
# if score<35:
#     print("Poor Student")
# elif 35<score<70:
#     print("Average Student")    
# elif score>=70:
#     print("Good Student")    

# input1=int(input("Enter ur input1:"))
# input2=int(input("Enter ur input2:"))
# ask_user=input("Do you want to add/sub/multiply/divide the number:")
# if ask_user=="add":
#     addition=input1+input2
#     print (addition)
# elif ask_user=="Substract":
#     if input1>input2:
#         substraction=input1-input2
#         print(substraction)
#     elif input2>input1:
#         substraction=input2-input1
#         print(substraction)    
# elif ask_user=="multiply":
#     multiplication=input1*input2
#     print(multiplication)
# elif ask_user=="divide":
#     if input1>input2:
#         division=input1/input2
#         print(division)
#     elif input2>input1:
#         division=input2/input1
#         print(division)        
# else:
#     print("Syntax Error")


# percentage=input("Enter your academic percentage:")
# if int(percentage)>70:
#     name=input("Enter your name:")
#     location=input("Enter your place:")
#     department=input("Enter your dept:")
#     print("You are eligible")
# else:
#     print("You are not eligible")



# salary=int(input("Enter your salary amount:"))
# age=int(input("Enter your age:"))
# if (salary>=20000) or (age<=25):
#     loan=int(input("Enter a loan amount you want:"))
#     if loan<=50000:
#         print("You are eligible for loan")
#     else:
#         print("Maximum loan amount is 50000") 
# else:
#     print("You are not eligible for loan")    



tamil=int(input("Enter your mark:"))
english=int(input("Enter your mark:"))
maths=int(input("Enter your mark:"))
science=int(input("Enter your mark:"))
social=int(input("Enter your mark:"))
addition=tamil+english+maths+science+social
average=addition/5
if average<35:
    print("Additional class is required")
else:
    print("You are good to go")    






