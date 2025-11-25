information={'first_name': str(input("Enter your first name:")),
             'last_name': str(input("Enter your last name:")),
             'hometown': str(input("Enter your hometown:")),
             'age': str(input("Enter your age:"))}

"""
this code will ask for the user's input and then the code will store the information that 
is put in by the user as "key-value pairs" in a dictionary
"""
print("\nYour Information:")
for value in information.values(): 
    print(value)#this will select and print the values
    
"""
Advanced Requirement
"""
print("n\Your name is"+" "+information['first_name']+" "
      +information['last_name']+".")
#this will print "Your name is (insert the first name you input here) (insert the last name you input here)."
print("Your hometown is located in"+" "+information['hometown']
      +".")
#this will print "Your hometown is located in (insert the hometown you input here)."
print ("You are"+" "+information['age']+" "+"years old.")
#this will print "You are (insert the age you input here) years old."