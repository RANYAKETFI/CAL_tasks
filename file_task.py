import random
import string
import os
file=open("./student_names.txt")
# 1-- read all the file concent in one variable
students=file.read()
print(students)
# 2-- Write a list of random names to my file 
letters = string.ascii_lowercase
print ( ''.join(random.choice(letters) for i in range(10)) )
for i in range(10) :
    name=''.join(random.choice(letters) for i in range(10))
    students=students+'\n'+name
file=open("./student_names.txt","w")
file.write(students)
#Read the first n lines of the file
n=int(input(" type the number of the lines "))
with open("./student_names.txt") as file:
  for i in range(n):
        first_lines = next(file).strip()
        print(first_lines)
#Read the last n lines of the file 
l=int(input(" type the number of the lines "))
with open("./student_names.txt") as file:
  
  lines = file.readlines()

last_lines = lines[-l:]  
for i in last_lines :       
  print(i)
#Check if the name x is in the file
x=input(" Please enter the name : ")
with open("./student_names.txt") as file:
  lines = file.readlines()
exists=False  
for n in lines:
    if x in n :
        exists=True
if exists :
    print('the name exists in the file')
else :
    print('the name does not exist in the file')            
#generate 26 text files named A.txt, B.txt, and so on up to Z.txt
os.makedirs("CLA_names_file")
for letter in string.ascii_uppercase:
   with open(letter + ".txt", "w") as f:
       f.writelines(letter)