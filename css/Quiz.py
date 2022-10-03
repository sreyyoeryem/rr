

# number=eval(input())
# result=""
# for i in range(len(number)):
#     for j in range((number[i])):
#         print(number[i],end="")
#     print("")

# array2D = [[1, 2], [3, 4]]
# for a in array2D :
#     for b in range(len(a)) :
#         c = a[b]
#         print(c)
# array = [1, 3, 9, 3, 20]
# for i in range(len(array)) :
# 	print(i[0])

# def double(a) :
#     res = 2*a;
#     return res
# res = double(5);
# print(res);




# array = [-5, 2, 9, -10, 0]


# result=array[len(array)-1]

# print(result)


# array = [5, 2, 9, -10, 6]
# num=1
# for i in range(len(array)):
#     if i%2==0:
#         num*=array[i]
# print(num)
    
      
# EX1-----------------------------------------------------


# array=eval(input("array:"))
# isTrue=True
# for num in array:
#     if num < 8 or num > 12:
#         isTrue = False
# print(isTrue)


# EX2------------------------------------------------


# array = eval(input("arrayNumber:"))
# result=[]
# Value="[]"
# isTrue=False
# if (len(array)) >0:
#     for i in range(len(array)):
#         if array[i]==1:
#             isTrue=True
#         elif (array[i]!=1 and array[i]!=0) and isTrue:
#             Value+=str(array[i])
#         elif (array[i]!=1 and array[i]!=0):
#             result="[]"
#         elif array[i]==0 and isTrue:
#             result=Value
#             isTrue=False
#         elif not isTrue:
#             result=("[]")
# print(result)
          

# Ex3--------------------------------------------

# array=eval(input("array:"))
# sumNumber=0
# count=0
# Value=0
# result="Fail"
# for num in range(len(array)):
#     if (len(array))>0:
#         sumNumber+=array[num]
#         count+=1
#     Value=sumNumber/count
#     if Value > 50:
#         result = "Pass"
# print(result)

# EX4-------------------------------------------


# words = eval(input())
# valueOfTrue = 0
# for word in words:
#     if word == True:
#         valueOfTrue+=1
# print(valueOfTrue)



# EX5---------------------------------------------

# number = int(input("number:"))
# for index in range (number + 1):
#     if index % 2 == 0:
#         print(index , end=" ")


#  ---------------------------------------------------------


# def average(number1,number2,number3):
#     for i in range(3):
#         for arr in range(len(number1)):
#             if number1>50 and number1<60:
#               return 55  
#             if number2>30 and number2<50:
#                 return 40
#             if number3>60 and number3<80:
#                 return 70
# number1=(50+60/2)
# number2=[30+50/2]
# number3=[60+80+70/3]
# print(number1)
# print(number2)
# print(number3)


# EXAM1

# EX1


# array=eval(input("Enter array:"))
# for i in (array):
#     result=0
#     for j in (i):
#         if  j =="a":
#             result+=1
#     print("Number of A in ",i,"is",str(result))

# EX2









# def containUpperCase(word):
#     result=""
#     for num in (word):
#         for j in num:
#             if j ==j.upper():
#                 result="valit"
#             else:
#                 result="invalet"
#     return result
# word=eval(input())
# print(containUpperCase(word))



# EX3

def reversestring(word):
    result=""
    for i in range(len(word)):
        result+= word[len(word) -i -1 ]
    return result
text=eval(input())
print(reversestring(text))




