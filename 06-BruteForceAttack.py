password= "12345"#this is the variable for the password
guesses= ""#this is the variable for the guesses
attempts= 5#this is the variable for the number of attempts

while attempts>0:#if the attempts are more than 0, the user can guess more
    guess= input("Enter the password here: ")#this is where the user will input their guess
    if guess== password:
        print("Password is correct, welcome.")#this will print if the user has entered the correct password (12345)
        break#the code ends here if the user has guessed the password correctly
    else:
        attempts= attempts - 1 #the number of attempts lessen by 1 if the answer the user entered is incorrect
        print("Incorrect password entered, you have", attempts,"attempts left.")
        #this will print if the password is wrong and it will also print how many remaining attempts the user has left
        if attempts == 0:
            print("Too many attempts have been made, the system is alerting the authorities and initiating lockdown.")
            #this will print if the password the user entered is wrong and if there are zero attempts left to guess