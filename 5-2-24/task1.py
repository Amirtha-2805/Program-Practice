# for i in range(1,11):
#     ans=2*i
#     print(i,"x2=",ans)

# a=int(input("Enter a number:"))
# b=int(input("Enter a number:"))
# for i in range(a+1,b):
#     print(i)

# for i in range(1,11):
#     if i%2==0:
#         print(i)


# count_even=0
# count_odd=0
# for i in range(1,11):
#     if i%2==0:
#         count_even=count_even+1
#     else:
#         count_odd=count_odd+1    
# print("The no.of even numbers:",count_even)
# print("The no.of odd numbers",count_odd)

# count1=0
# count2=0
# for i in range(1,101):
#     if i%3==0:
#         count1=count1+1
#     elif i%5==0:
#         count2=count2+1
# print("No.of values divisible by 3 are:",count1)
# print("No.of values divisible by 5 are:",count2) 

# total=0
# for i in range(1,6):
#     total=total+i
# print(total)   


# list=[]
# total=0
# for i in range(1,11):
#     number=int(input("Enter a number:"))
#     list.append(number)
#     total=total+number  
# print("Numbers=",list)     
# print("The sum of all number is:",total)
# print("The average is:",total/10)



# n_terms=int(input("Enter how many terms of natural numbers do you want to add:"))
# list=[]
# total=0
# for i in range(1,n_terms+1):
#     number=int(input("Enter a number:"))
#     list.append(number)
#     total=total+number
# print(list)
# print("The sum of all numbers in the list is=",total)    


# n_terms=int(input("Enter how many terms do you want to add:"))
# list=[]
# for i in range(1,n_terms+1):
#          number=int(input("Enter a number:"))
#          cube=number**3
#          print(number,"and cube of",number,"is",cube)


# for i in range(1,8):
#     print("week:",i)
#     for j in range(1,4):
#         print("day:",j)       

for i in range(1,5):
    print()
    for j in range(1,i+1):
        print("*",end="")
        

