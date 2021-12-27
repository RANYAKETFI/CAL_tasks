# exceptions
try :
  a = 12
  s = "hello"
  print(a+s) 
except Exception as A :
   print("this is an exception where a is an int : TypeError Exception")  
   a=str(a) 
finally :
   print(a+s)  