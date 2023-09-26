'''
10.Build a countdown calculator.
Write some code that can take two dates as input,
and then calculate the amount of time between them
'''
from datetime import datetime

def countdown(start_date, end_date):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    countdown = end - start
    return countdown

start_date = input("enter the start date (YYYY-MM-DD): ")
end_date = input("enter the end date (YYYY-MM-DD): ")
result = countdown(start_date, end_date)
print("The countdown is", result.days)

#----------------------------------------------------------
'''
11.Make a temperature/measurement converter.
Write a script that can convert Fahrenheit to Celcius and back,
or inches to centimeters and back, etc in 3 di
'''

class Converter:
    @staticmethod
    def fehrenheit_to_celsius(fehernheit):
        celsius = (fehernheit - 32)*(5/9)
        return print("result = ", celsius)
    
    @staticmethod
    def celsius_to_fehrenheit(celsius):
        fehrenheit = (celsius * (9/5))+32
        return print("result = ", fehrenheit)
        
    @staticmethod
    def inches_to_centimeters(inches):
        centimeters = inches * 2.54
        return print("result = ", centimeters)
    
    @staticmethod
    def centimeters_to_inches(centimeters):
        inches = centimeters / 2.54
        return print("result = ", inches)
    
    @staticmethod
    def kilos_to_pounds(kilos):
        pounds = kilos * 2.20462
        return print("result = ", pounds)

    @staticmethod
    def pounds_to_kilos(pounds):
        kilos = pounds / 2.20462
        return print("result = ", kilos) 



converter = Converter()
while True:
    
    n = int(input(
        '''Choose your operation:
                   1:fehrenheit_to_celsius
                   2:celsius_to_fehrenheit
                   3:inches_to_centimeters
                   4:centimeters_to_inches
                   5:kilos_to_pounds
                   6:pounds_to_kilos
                   7:exit
                   '''))

    if n == 1:
        f = float(input("enter the fehernheit temp: "))
        converter.fehrenheit_to_celsius(f)
    elif n == 2:
        c = float(input("enter the celsius temp: "))
        converter.celsius_to_fehrenheit(c)
    elif n == 3:
        i = float(input("enter the inches measure: "))
        converter.inches_to_centimeters(i)
    elif n == 4:
        cm = float(input("enter the centimeter measure: "))
        converter.centimeters_to_inches(cm)
    elif n == 5:
        k = float(input("enter the kilos measure: "))
        converter.kilos_to_pounds(k)
    elif n == 6:
        p = float(input("enter the pounds measure: "))
        converter.pounds_to_kilos(p)
    elif n == 7:
        break
    else :
        print("invalid value")
    
#----------------------------------------------------------

'''
12. Build an email slicer : create a function that takes an email as input
and retrieve the username and domain of the email
'''

def email_slicer(email):
    username, domain = email.split('@')
    return print(f"Username: {username}\nDomain: {domain}")

email = input("enter your email : ")
email_slicer(email)

#----------------------------------------------------------

'''
13.Currency converter : create a python script that
takes a money with currency sign and
convert it to some other currencies ,
the code should be like the game we did before
'''

class Currency_Exchange:
    def __init__(self):
        
        self.converted_money = None
        while True :
            n = int(''' Welcome Sir, Please choose your Currency Conversion transaction:
                            1:EGP to USD
                            2:EGP to EURO
                            3:EGP to AED
                            4:EGP to KWD
                            5:Exit
                            ''')
            
            money = float(input("Enter the money ")
                          
            if n == 1:
                self.converted_money = money * 30.93
                print(f"Your Currency Conversion transaction to USD is : {self.converted_money} USD")
            elif n == 2:
                self.converted_money = money * 32.69
                print(f"Your Currency Conversion transaction to EURO is : {self.converted_money} EUR ")
            elif n == 3:
                self.converted_money = money * 8.42
                print(f"Your Currency Conversion transaction to AED is : {self.converted_money} AED ")

            elif n == 4:
                self.converted_money = money * 100.00
                print(f"Your Currency Conversion transaction to KWD is : {self.converted_money} KWD ")
            elif n == 5:
                break
            else :
                print("invalid option")
                
                          
currency = Currency_Exchange()











    
