# data="mohammadrijvan"
# print(data.replace('rijvan','Farooque'))
# print(data.capitalize())
# print('count of e is --',data.count('e'))
# print(data.find('e'))
# print(data.isalpha())
# print(data.join("$&"))
# str="   Wanihar  "
# print(str.ljust(15,'*'))

# print(str.rjust(15,'*'))
# print(str.strip(' '))

# str2="manihar"
# result=str+str2
# print(result.strip(' '))

# Data="My collage name name  is is jit jit"

# count=''
# for i in Data.split():
#     if i not in count:
#         count+=i+' '
# print(count)
#         count+=' '
# print(count)unt=''
# for i in Data.split():
#     if i not in count:
#         count+=i+' '
# print(count)
#         count+=' '
# print(count)
# data=' '
# itr=0
# for i in Data.split():
#     count=0
#     for j in Data.split():
#         if i==j:
#             count+=1
#             itr+=1
#         if count==2:
#            count=1
#     if count==1:
#         data+=i
#         data+=' '
# print(data)
#only count the repeated word length
# original="welcome to to python python   dklsa dklsa dkslsa jj jj jj kk kk kk aa aa"
# # count=0
# for i in original.split():    
#     for j in original.split():
#         if i==j:
#             count+=1
#     if count>1:
#         count=0
#         continue
#     else:
#         print(i)
#     count=0

# new=original.split()
# duplicate={}
# for i in new:
#     c=new.count(i)
#     if c>=2:
#         duplicate[i]=c
# print(duplicate)

# add=lambda a,b:a+b
# print(add(4,5))
                            ## Interview point of view
# def f1():
#     return lambda x,y:x+y
# a=f1()
# print(a(10,892))


# n = int(input())
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or i==n-1 or j==n-1:
#             print("*"," ", end=" ")
#         else:
#             print(" "," ", end=" ")
#     print()
##like pattern [*1*,**2**,***3***,****4****] in format of list
# data=[f'{"*"*i}{i}{i*"*" }'for i in range(1,11) if i%2!=0]
# print(data)


#like pattern [*1*,**2**,***3***,****4****] in format of list
# data = []
# for i in range(1, 11):
#     data.append('*' * i + str(i) + '*' * i)
# print(data)

# data=[(lambda x:x**2)(x) for x in range(1,5)]
# print(data)
# data =['abc','pqr','str']
# new=[]
# for i in reversed(data):
#     print(new.append(i[::-1]))
# print(new)
#[1,2] [1][2][1,2] like print 


# data=[1,2,3]
# for i in range(3):
#     print(data)
#     for j in range(len(data)):
#         print([data[j]])
#     print(data)
#     for k in range(len(data)):
#         print([data[k]],end="")
#     print()
# data.append(data)
# print(data)

# n=int(input("enter the number"))
# for i in range(n):
#     for j in range(n):
#         if j<=i:
#             print("*",end="")
#     print(i+1,end="")
#     for k in range(n):
#         if k<=i:
#             print("*",end="")
#     print()


data =[1,2,3,4,4,5]

# for i in data:
#  print(i**2)
  
data=[x**2 for x in data]
print(data)