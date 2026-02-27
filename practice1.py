#wap to take a number and calculate the sun of its digits using a loop.

# n=eval(input('enter number:'))
# sum=0
# for i in str(n):
#     sum=sum+int(i)
# print(sum)

#wap to check if a given string is a palindrome or not...using loops
# string=input("enter string:")
# rev=''
# for char in string:
#     rev=char+rev
# if string==rev:
#     print('yes')
# else:
#     print('no')

#wap ro print how many times character occurs.

# word=input("enter word:")
# count_char={}
# for char in word:
#     if char in count_char:
#         count_char[char]=count_char[char]+1
#     else:
#         count_char[char]=1
# print(count_char)

#wap to check number is prime or not

# def isprime(num):
#     for i in range(2,num):
#         if num%i==0:
#             return False
#     return True
# print(isprime(10))

#wap to print all prime numbers between 1 and n..
# num=int(input("enter num:"))
# l=[]
# for num in range(2,num+1):
#     for i in range(2,num):
#         if num%i==0:
#             break
#     else:
#         l.append(num)
# print(l)


#wap to check whether a number is a parfect number or not.
# def is_perfect_num(num):
#     sum=0
#     for i in range(1,num):
#         if num%i==0:
#             sum=sum+i
#     if sum==num:
#         return True
#     else:
#         return False
    
# print(is_perfect_num(6))

# num=eval(input('enter num:'))
# l=[]
# for num in range(1,num+1):
#     sum=0
#     for i in range(1,num):
#         if num%i==0:
#             sum=sum+i
#     if sum==num:
#         l.append(num)
# print(l)

# num=eval(input('enter number:'))
# sum=0
# for i in num:
#     sum=sum+num
# print(sum)

#wap tp print 1 to 30 number

# i=1
# while i<=30:
#     print(i)
#     i=i+3

# #wap to print 10 to 1 number
# i=10
# while i>0:
#     print(i)
#     i=i-1

#wap to print 1 to 10 number

# for i in range(1,11,1):
#     print(i)

# #wap to print 1 to 30 number increment by 3

# for i in range(1,32,3):
#     print(i)


# #wap to print 10 to 1 number

# for i  in range(10,0,-1):
#     print(i)

#wap tp print number take range by user

# start=int(input("enter starting number:"))
# end=int(input("enter ending number:"))

# for i in range(start,end+1):
#     print(i)

# i=start
# while i<=end:
#     print(i)
#     i+=1

#wap to print sum of 1 to 10 number

# sum=0
# for i in range(1,11,1):
#     sum=sum+i
# print(sum)

# sum=0
# i=1
# while i<=10:
#     sum=sum+1
#     i=i+1
# print(sum)

#wap to print sum of number take range by user

# sum=0

# start=int(input("enter starting number:"))
# end=int(input("enter ending number:"))

# # for i in range(start,end+1):
# #     sum=sum+i
# # print(sum)

# sum=0
# i=start
# while i<=end:
#     sum=sum+i
#     i=i+1
# print(sum)

#wap to print sum of even number from 1 to 10 number

# sum=0
# for i in range(1,11,1):
#     if i%2==0:
#         sum=sum+i
# print(sum)

# l=[11,22,33,44,67,89,12,36,48,67]
# sum=0
# for i in l:
#     if i%3==0 and i%4==0:
#         sum=sum+i
# print(sum)

#marks={'math':78,'science':67,'His':90,'hindi':94,'marathi':85}
#wap to cal total obt marks

# sum=0
# for i in marks.values():
#     sum=sum+i
# print(sum)

#wap to cal percentage

# sum=0
# for i in marks.values():
#     sum=sum+i
#     per=sum/len(marks)
# print(per)

#product_mrp={'laptop':60000,'mobile':20000,'Tv':40000}
#print dict of selling price

# for name,price in product_mrp.items():
#     dis=price*15/100
#     product_mrp[name]=price-dis
# print(product_mrp)

# product_mrp={'laptop':60000,'mobile':20000,'Tv':40000,'laptop bag':2000,'table':5000}

# product_sp={}
# for product,mrp in product_mrp.items():
#     if mrp>25000:
#         dp=mrp*20/100
#         sp=mrp-dp
#         product_sp[product]=sp
#     else:
#         dp=mrp*10/100
#         sp=mrp-dp
#         product_sp[product]=sp
# print(product_sp)


#wap to cal length of string without using len()

# s=input("enter a string:")

# count=0
# for ch in s:
#     count+=1
# print(count)

#wap to cal number of vowels in given string

# string=input('enter string:')
# vowel_count=0
# for ch in string:
#     if ch in 'aeiou':
#         vowel_count+=1
# print(vowel_count)

#wap to reverese string

# string='divya'
# rev=''
# for char in string:
#     rev=char+rev
# print(rev)

#wap to check string is palindrome or  not

# string=input("enter string:")
# rev= ""
# for char in string:
#     rev= string[::-1]
# if string == rev:
#     print("string is palindrome")
# else:
#     print("string is not palindrome") 
# palindrome means the seq of char that reads forward or backword are same.



#SATURDAY                JAN 10 2026

# def area_rectangle(length,width):      #area of rectangle
#     return length*width
# print(area_rectangle(12,10))


# def perimeter_rectangle(length,width):      #perimeter of rectangle
#     a=2*length+width
#     return a

# def diagonal(length,width):        #diagonal of rectangle
#     a=length**2+width**2
#     b=a*0.5
#     return b
# print (diagonal(10,30))


# Q.2 CIRCLE

# def area_circle(r):
#     a=3.14(r**2)
#     return a
# print(area_circle)


# def circ_circle(r):
#     a=2*(r**2)
#     return a
# print(circ_circle(5))

# library managment system

class library :
    lname='the kiran acadamy'
    owner='kiran sir'
    def __init__(self,br):
        self.branch=br
        self. books ={}    #{'bookname':count}
        self.members={}    #{mid:[]}

    def add_book(self,book,count):
        #var [key] = value
        if book in self.books:
            self.books [book] = self.books[book]+count
        else:
            self.books [book] = count
        return 'added....'

        def remove_book(self,book,count=0) :
            if book in self.books:
                if count==0:
                    del self.books[book]
                else:
                    self.books[book]=self.books[book]-count

karve = library('karve nagar')
warje = library('warje')
karve.add_book('java',50)
warje.add_book('python',5)

    

prime or nor prime 