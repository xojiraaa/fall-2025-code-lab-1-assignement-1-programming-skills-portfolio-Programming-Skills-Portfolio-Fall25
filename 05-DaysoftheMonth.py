Months_and_Days={1:31,
                 2:28,
                 3:31,
                 4:30,
                 5:31,
                 6:30,
                 7:31,
                 8:31,
                 9:30,
                 10:31,
                 11:30,
                 12:31}
#this creates a dictionary of the month numbers and the how many days are in them
your_year=int(input("Input the year number here:"))#this creates a variable for the user's input for the year number
month_number=int(input("Input the month number here:"))#this creates a variable for the user's input for the month number

def leap(year): 
    if(year % 400 ==0) or (year % 4==0 and year %100 != 0): 
        return True
    return False
if leap(your_year):#this will check if the year the user entered is a leap year (366 days in a year)
    print(f"{your_year} is a leap year.")#this will print "(the year the user entered) is a leap year."
    if month_number not in Months_and_Days:
        print("Month number invalid.")#this message will print if the month number the user entered is invalid (not in the dictionary)
    else:
        if month_number ==2:
            print("There are",Months_and_Days[month_number]+1,"days in this month.")
        else:
            print("There are", Months_and_Days[month_number], "days in this month.")
else:#this will check if the year the user entered is not a leap year (365 days in a year/normal year)
            print(f"{your_year} is not a leap year.")#this will print "(the year the user entered) is not a leap year."
            if month_number not in Months_and_Days:
                print("Month number invalid.")#the text "Month number invalid." will print if the month number the user entered is not in the dictionary of months and days
            else:#the text will print "There are (insert month number from months and days dictionary) days in this month." 
                print("There are",Months_and_Days[month_number], "days in this month.")#the value inside the parenthesis will show how many days there are in that specific month

