# Write a Python function that checks whether a passed string is palindrome or not
def isPalindrome(st) :
    is_pal=True 
    for i in range(0, int(len(st)/2)):
        if st[i] != st[len(st)-i-1]:
            is_pal= False
    return is_pal
# function that takes a number as a parameter and checks if the number is prime or not.
def isPrime(num) :
    is_prime=True 
    for i in range(2,int(num**1/2+1)):
      if num%i==0:
          is_prime=False
    return(is_prime)
#to check whether a number is in a given range
def inRange(num,start,end):
 return num in range(int(start),int(end))
#calculate the factorial of a number (a non-negative integer)
def fact(num) :
    num=int(num)
    if num==0 :
        return 1
    else :
        return num*fact(num-1)
#Write a Python program to reverse a string
def reverse(st) :
    return st[::-1]
#function to sum all the numbers in a list
def sumlist(l):
    sum=0
    for i in l :
        sum=sum+i
    return sum     
#function to find the Max of three numbers
def maxThree(a,b,c):
    if a<b :
      if b<c :
          return c 
      else : 
          return b    
    elif a<c : 
        return c 
    else : return a
