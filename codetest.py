# exception

# try:
#     if '1' != 1:
#         raise "someError"
#     else:
#         print("someError has not occured")
# except "someError":
#     print("someError has occured")

# someerror" is not valid exception name


# condition = True
# if condition:
#     x = 1
# else:
#     x = 0
# print(x)


# x = 1 if condition else 0
# print(x)


# # number of zero counting challenge

# num1 = 100_00_00_00
# num2 = 10_00_00

# num = num1 + num2
# print(f'{num:,}')


# without context manager

# f = open("test.txt", 'r')
# file_Content = f.read()


# words = file_content.split()
# words_count = len(words)
# print(words_count)
# f.close()

# context manager thread for relaeasing lock,database connection --managing resources

    # with open('file.txt', 'r') as f:
    #     Content = f.read()
        
    # words = content.split()
    # words_count = len(words)
    # print(words_Count)


# names=['Ram','Nam','Cam']

# for index,name in enumerate(names,start=1):
#     print(index,value)


# name1=['karthiga','Kalyan','Tamil','Eswaran','Nive']
# name2=['Logu','Kanaga','Radha','Dhanam','chitha']

# for index,name in enumerate(name1):
#     name3=name2[index]
#     print(f"{name}:{name3}") 


#to loop over two list we use zip function
# for name1,name2 in zip(name1,name2):
#     print(f"{name1}:{name2}") 


#unpack values (_ to negelect that value whereas * for continues value inclusion)

# a,b=1,2

# print(a)

# a,b,*c=(1,2,3,4,5)

# print(c)

# # a,b,*c,d=(1,3,4,5,7)
# # print(a)
# # print(b)
# # print(c)
# # print(d)


# a,b,*_,d=(1,3,4,5,7)
# print(a)
# print(b)
# #print(c)
# print(d)


#setattr and getattr function to access attribute value corresponding to a key
class Person():
    pass

persons=Person()
# persons.first='Great'
# persons.last='Awesome'

# print(persons.first)
# print(persons.last)

# persons_items={'first':'Karthiga','second':'Dhachu'}

# for key,value in persons_items.items():
#     setattr(persons,key,value)

# print(persons.first)
# print(persons.second)


# for key in persons_items.keys():
#     getattr(persons,key)

# print(persons.first)
# print(persons.second)



#number prime or not



num=int(input("enter number"))
# If given number is greater than 1
if num > 1:
  
    # Iterate from 2 to n / 2
    for i in range(2, int(num/2)+1):
  
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime numbers")
            break
    else:
        print(num, "is a prime number")
  
else:
    print(num, "is not a prime number")