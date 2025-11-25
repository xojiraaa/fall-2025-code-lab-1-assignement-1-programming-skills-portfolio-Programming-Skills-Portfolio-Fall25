def even(number): #this defines the function for even numbers
    return number % 2==0#if the number is divisible by 2 and if it has a remainder of 0
def odd(number):
    return number %2==1#if the number is divisible by 2 and if it has a remainder of 1
def main():
    number= int(input("Enter a number here: "))#this asks for the user's input for the number
    
    if even(number):#if the number the user entered has 0 as its remainder
        print("This is an even number.")
    elif odd(number):#if the number the user entered has 1 as its remainder
        print("This is an odd number.")
main()