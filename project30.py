class numeral:
    def __init__(self,number):
        self.number = number
    
    def find(self,number):
        if number < 4:
            print("your number is between I and III")
        elif number>4 and number<9:
            print("your number is between IV and VIII")
        elif number>9 and number<40:
            print("your number is between X and XXXIX")
        elif number>40 and number<90:
            print("your number is between XL and LXXXIX")
        elif number>90 and number<101:
            print("your number is bewtween XC and C")

n = int(input("enter a number beetween 1 and 100 : "))

num = numeral(n)
num.find(n)