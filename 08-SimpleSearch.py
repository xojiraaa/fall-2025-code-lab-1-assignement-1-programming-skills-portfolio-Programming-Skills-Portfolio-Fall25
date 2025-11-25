my_list=["Jake","Zac","Ian","Ron","Sam","Dave"]#this is the list of the specific names given
print("Objective: Find the person who left the door open. You only have one attempt.")
print(my_list)#this will print the list of names above (Jake, Zac, Ian, Ron, Sam, and Dave)
search=str(input("Enter the name of the person who left the door open: "))#this asks for the user's input on who left the door open
if search== "Sam":
    print("Good job, it was Sam! Always close the door.")#this will print if the user correctly guessed who left the door open (if the user answered Sam)
else:
    print("Incorrect guess, better luck next time.")#this will print if the user does not manage to guess who left the door open (if the user didn't answer Sam)