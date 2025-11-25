a=0
b=0
c=0
d=0
e=0
#the letters shown above are a list of the variables

print("\nzero to fifty:")
for a in range(0,51):#this will count from 0 to 50
    print(a)#this will print the values 0 to 50
    
print("\nfifty to zero:")
for b in reversed(range(0,51)):#this will count from 50 to 0
    print(b)#this will print the values 50 to 0
    
print("\nthirty to fifty:")
for c in range(30,51):#this will count from 30 to 50
    print(c)#this will print the values 30 to 50
    
print("\nfifty to ten:")
for d in reversed(range(10,51,2)):#this will count from 50 to 10 but the values are decreasing by 2's
    print(d)#this will print the values 50 to 10 but the values will go down by 2's (ex. 50, 48, 46, so on and so forth) until it reaches 10
    
print("\none hundred to two hundred:")
for e in range(100,201,5):#this will count from 100 to 200 but the values are increasing by 5's 
    print(e)#this will print the values 100 to 200 but the values will go up by 5's (ex. 100, 105, 110, so on and so forth) until it reaches 200