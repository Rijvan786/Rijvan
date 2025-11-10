#    ***************************************Dictionary Comprehensive *********************************

""" it is concept in which we  generate data elementsin keys and values pair"""

# data={chr(k):k for k in range(65,71)}
# print(data)




"""  sINGLE VALUE DATA"""

"""STRING                                collection data
                                     list 
  INT                                tuple 
  STRING                              set 
  float                              dictionary
  Bolean           


"""
# data={'a':23,True:[3,4,5,6],121:"airtel care",3.14:"value of pie"}
# print(data[121])

# data['a']={"age":22,"name":"Mohammad"}
# print(data)

# data["xyz"]=900
# print(data)


# def f1(a={}):
#      a['x']=90
#      return a
# print(f1())

# def f1(a=[]):
#      a.append(1)
#      return a
# print(f1())
# print(f1())

# def r(a,b=set()):
#     b.add(a)
#     return b

# print(r(1))
# print(r(2))



# """ HIgh ordered function """

# def add(a,b):
#     return a+b

# def subt(a,b):
#     return a-b

# def mul(a,b):
#     return a*b

# def div(a,b):
#     return a/b
# def operation(a,b,c,d):
#     return a(b(c(d)))
    

# add=lambda x:x+1
# mul=lambda x:x*x
# div=lambda x:x/x
# subt=lambda x:x-1


# print((operation(add,subt,mul,subt,10,20))) #//


# def sum (*argument):
#  s=0
#  for i in argument:
#     s+=i
#     return s

# # print(sum(44,55,77))

# data=[[1,2,3],[4,5,6],[7,8,9]]
# list=[]

# def make_flated(data):
#     for i in data:
#         for k in i:
#             list.append(k)
#     return list
# print(make_flated(data))



# str="Jit borawan"
# reverse the string without using the inbuild function using function
# def reverse_string(s):
#     rev=""
#     for i in s:
#         rev=i+rev
#     return rev
# print(reverse_string(str))



# print(str[::-1])


"""Recursion is a function that calls itself multiple times until it reaches the base condition"""

def f1(n):
   if n==0 :
        return # please reverse the 10
   else:
    print(n)
    return f1(n-1)
f1(10)



# def f1(n):
#     if n==0:
#         return 1                                                                                                                                                                                                                                                             
#     else:
#      return n*f1(n-1)
    
# print(f1(5))

# data=[12,23,45,56,67,6]
# def display(a):
#     element=len(data)
#     if a==element:
#         return 0
#     else:
#         print(data[a],end=' ')
    
#     return display(a+1)
# display(0)

# """ keyword Argument function   pass in parameter **kwargs"""
# def f1(**kwargs):
#     print(kwargs)

# f1(a=1,b=2,c=6)
                                                        










# def key(**kwargs):
    
#     print(kwargs)


# key(a=88,b=788)


"""##for loop mai else bhi execute karenga so brek se else ko rok denga"""
#while loop mai else tabhi execute hoga jab while loop ka condition false hoga

# i=1
# while i<=5:
#     print(i)
#     i+=1
#     if i==3:
        
# else: 
#     print("loop is ended")




# def f2(b):
#     def f1(a):
#         if a==11:
#             return 1
#         print(a)
#         return f2(a+1)
#     return f1(b)
# f2(1)

# original="welcome to the world of python programming welcome to the world"  #explain the code #only count the repeated word length
# count=0
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

                         ## smpt 
# import random
# num=random.randint(1001,9999)
# print(num)
# name=["mohammad","jitendra","sachin","rahul","saurabh","","","",""]



# print(random.choice(name))

# print(random.random())
# print(random.randrange(1,10,2))


# import smtplib,random,ssl
# app_password="csaiml@77"
# email="techbooster05@gmail.com"
# to="rizwanmnhr@gmail.com"

# otp=random.randint(1111,9999)
# body=f"your otp is {otp}"

# with smtplib.SMTP_SSL("smtp.gmail.com",465,context=ssl.create_default_context())as s:
#     s.login(email,app_password)
#     s.sendmail(email,to,body)
# print("otp send",otp)



"""single multiple multilevel hierachical """

"""" Inheritance in class"""

# class c1:
#   age=90

#   def __init__(self):
#      print("C1 Constructor")


# class c2(c1):
#   age=50
#   def __init__(self):
#      print("C2 Constructor")

# obj =c2()

"""Encapsulation""""Data hide karna Acess Modifier ka use karke  """

# class c1:
#     __age=90
#     def __init__(self):
#         print("i am c1 Constructor")
#     def __display(self):
#         print("I am Encapsulated method")
#     def call_dispalay(self):
#         return c1.__display(self)
# obj=c1()
# print(obj.call_dispalay())
      
            # """Types of Encapsulation"""
# class c1:   
#   _age=90 
#   _v=900  ## Partially Encapsulation
#   def m1(self,a,b):
#     self.a=a
#     self.b=b
#   def display(self):
#     print(self.a,self.b)
# obj=c1()
# print(obj._v)

"""Polymorphism"""


# class bank:
    

#  def __init__(self,bank_acount,balance): 
#        self.bank_acount=bank_acount
#        self.balance=balance
#  def display(self):
#      print(self.bank_acount,self.balance)

# Hdfc=bank(1234567,50000)

# print(Hdfc.bank_acount,Hdfc.balance)  

"""gettear and setter"""

# class Bank:
#  def __init__(self,bank_acount,balance): 
#        self.bank_acount=bank_acount
#        self.balance=balance
#  def getter(self):
#      print(self.bank_acount,self.balance)
#  def setter(self,b):
#      self.balance+=b

# Hdfc=Bank(1234567,50000)

# Hdfc.getter()
# Hdfc.setter(1000)
# Hdfc.getter() 

"""Abstraction :-mai implimaintation hide karna hai    """""""""

# from abc import abstractmethod,ABC
  

# class engine(ABC):
#     @abstractmethod
#     def start(self):
#         pass
#     def stop(self):
#         pass
# class car(engine):
#     def start(self):
#         print("engine started")
#     def stop(self):
#         print("engine stop")
   
# obj=car()
# obj.start()


"""Polymorphism  har ak class ke liye ak hi method""" 


# class animals:
#     def eating(self):
#         print("eating eating grass and meet ")

# class human:
#     def eating(self):
#         print("eating wheat ")

# class plant:
#     def eating(self):
#         print("eating sunlight")
# obj1=animals()
# obj2=human()
# obj3=plant()

# data=[obj1,obj2,obj3]
# for object in data:
#     object.eating()




# class Cse:
#     def attendence(self):
#         print("full all the class")
        
# class mechanical:
#     def attendence(self):
#         print("less than ")

# class civil:
#     def attendence(self):
#         print("median attendence")  
# class Agri:
#      def attendence(self):
#          print("all absent ")

# class Electriacal:
#     def attendence(self):
#         print("present")

# obj1=Cse()
# obj2=mechanical()
# obj3=Agri()
# obj4=Electriacal()

# data=[obj1,obj2,obj3,obj4]

# for object in data:
#     object.attendence()

# """ducktyping"""
# class cat:
#     def make_sound(self):
#         print("meaoo")
# class dog:
#     def make_sound(self):
#         print("bho bho")

# def call(a):
#     a.make_sound()
# call(cat())
# call(dog()) 






# """multilevelinheritance"""

# class c1:
   
#   def m1(self):
#        print("I am c2 from m1")

       
# class c2(c1):
#    def m1(self):
#        print("I am c2 fro m1")
 

# class c3(c2):

#    def m1(self):
#        print("I am c3 fro m1")
#        c1.m1(self)
#        c2.m1(self)
# obj=c3()
# print(obj.m1())


"""multiple inheritance"""
"""downword"""
# class c1:
#     age=90
#     def __init__(self):
#         print("I am constructor from c1 ")

# class c2:
#     age=80
#     def __init__(self):
#         print("I am constructor from c2 ")

# class c3(c1,c2):
#     age=80
#     def __init__(self):
#         print("I am constructor from c3 ")
#         c1.__init__(self)
#         c2.__init__(self)

# obj=c3()
# print(obj.age)

# """Upwords"""
# class c1:
#     def __init__(self):
#         print("I am constructor from c1 ")
#     def  m1(self):
#       print(" I am m1 from c1")
#     age=90

# class c2(c1):
#     age=80
#     def __init__(self):
#         print("I am constructor from c2 ")

# class c3(c1):
#     age=80
#     def __init__(self):
#         print("I am constructor from c3 ")
#         c1.__init__(self)
#         c2.__init__(self)
#     def  m1(self):
#       print(" I am m1 from c3")
#       c1.m1(self)
      


# obj=c3()
# obj.m1()

"""method overloading  It is achieve directly in other languages not in python"""
 

# class c1:
#     def m1(self):
#         print("h1")                  
#     def m1(self,a):
#         print("h1",a)
#     def m1(self,a,b):
#         print("h1",a,b)
# obj=c1()
# obj.m1(12,25)



# class c1:
#     def m1(self, a=0, b=0, c=0):
#         if b==0 and c==0:
#             print("One argument",a)
#         elif a!=0 and b!=0 and c!=0:
#             print("thrree argument",a+b+c)
#         elif  c==0:
#             print("twoo argument",a*b)
#         else:
#             print("no argument")
# o=c1()
# o.m1(4,5,4)


# """method overriding"""
# class c1: 
#    def __init__(self,a,b):
#        self.a=a
#        self.b=b

#    def __add__(self,second):
#      n1=self.a+second.a
#      n2=self.b+second.b
#      return n1,n2
# obj1=c1(12,34)

# obj2=c1(10,20)

# print(obj1.__add__(obj2))



# class multi:
#    def __init__(self,r,s):
#       self.r=r
#       self.s=s
    
#    def __mul__(self,second):
#       m1=self.r*second.r
#       m2=self.s*second.s
#       return m1 , m2

# o1=multi(12,10)

# o2=multi(10,10)

# print(o1.__mul__(o2))







# class div:
#    def __init__(self,r,s):
#       self.r=r
#       self.s=s
    
#    def __div__(self,second):
#       m1=self.r/second.r
#       m2=self.s/second.s
#       return m1 , m2

# o1=div(10,10)

# o2=div(10,10)

# print(o1.__div__(o2))



class power:
   def __init__(self,r,s):
      self.r=r
      self.s=s
    
   def __pow__(self,second):
      m1=self.r**second.r
      m2=self.s**second.s
      return m1 , m2

o1=power(2,3)

o2=power(10,2)

print(o1.__pow__(o2))


                           