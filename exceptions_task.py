# exceptions
try :
  a = 12
  s = "hello"
  print(a+s) 
except Exception as A :
   print("this is an exception where a is an int  ")  
   a=str(a) 
finally :
   print(a+s)   