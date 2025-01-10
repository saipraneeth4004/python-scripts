c=input()
a=c.isupper()
b=c.islower()
d=c.isdigit()
if(a):
    print("Uppercase Letter") 
elif(b):
    print("Lowercase Letter") 
elif(d):
    print("Digit") 
else:
    print("Special Character")
