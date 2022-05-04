"""Author: Meliyah Watson
Date Created: 04/28/2022
Course: ITT103
Purpose: Based on specified input and criteria, compute and output the commission received by an undefined number of salespersons.
Based on specified input and criteria, compute and output the commission received by an undefined number of salespersons.
"""


"""
JamEx Limited requires a program to calculate and print the commission received by a
salesperson. The program should process an undetermined number of salespersons and
appropriately terminate by a predefined input. The commission rate is based on two factors,
the amount of sales and the class to which a salesperson belongs. The input will be the
salesperson number, sales amount and class. The commission rate will be based on the
following criteria:

Class=1
If sales is equal to or less than $1000, the rate is 6 percent.
If sales is greater than $1000 but less than $2000, the rate is 7 percent.
If the sales is $2000 or greater, the rate is 10 percent.

Class=2
If the sales is less than $1000, the rate is 4 percent.
If the sales is $1000 or greater, the rate is 6 percent.

Class=3
The rate is 4.5 percent for all sales amount

Class=any other value
Output an appropriate error message.
"""



classrate_1 = 0.06

classrate_1b = 0.07

classrate_1c = 0.10 

classrate_2 = 0.04 

classrate_2b = 0.06 

classrate_3 = 0.045 

rate_of_commission = 0 

commission_rate = 0 
 


import sys

def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, count))
        file.flush()        
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()

import time

for i in progressbar(range(10), "Loading JamEx Limited Program: ", 40):
    time.sleep(0.1) 




def output_results (number, salesclass, amount, rate):   
   
    print("\n****************")
    print("///////*RESULT*///////\n//////////////////////")
    print("\nSalesperson number:" + str(number))
    print("salesperson class: " + str(salesclass))
    print("sales amount: $" + str(amount))
    print("comission rate: $" + str(round(rate, 2)))
    print("\n****************")
    
print(u"\n\u001b[32mJamEx Limited's company commission program is now open!\n\u001b[0m")

while True:
    while True: 
        message = input("To exit the program, type Exit.\nTo proceed, type Push: ")
        if message == 'Push'or message == 'push':
            break           
        elif message == 'Exit' or message == 'exit':
            print(u"\u001b[31mThe Program has ended.\u001b[0m")
            break
        else:
            print(u"\u001b[4m\u001b[44mSorry, this information is invalid\n\u001b[0m")
    
    if message == 'Stop' or message == 'stop':
        break 
    

    salesclerk_num = input("\nInput the salesperson number: ")
    amount_sales = int(input("\nInput the sales amount: "))
    

    while True:
        try:
            salesperson_class = int(input("\nInput the salesperson class: "))      
        except ValueError:
            print(u"\u001b[4m\u001b[44mSorry, this class is invalid\u001b[0m")
    
            continue
        if salesperson_class < 1 or salesperson_class > 3:
            print(u"\u001b[1m\u001b[31mThis is an invalid class. please enter from class 1-3:\u001b[0m")
        else:    
           
            break
        
    if salesperson_class == 1:
        if amount_sales <= 1000:
            commission_rate = classrate_1 * amount_sales
        elif amount_sales > 1000 and amount_sales < 2000:
            commission_rate = classrate_1b * amount_sales
        elif amount_sales >= 2000:
            commission_rate = classrate_1c * amount_sales

    if salesperson_class == 2:
        if amount_sales < 1000:
            commission_rate = classrate_2 * amount_sales
        elif amount_sales >= 1000:
            commission_rate = classrate_2b * amount_sales

    if salesperson_class == 3:
        commission_rate = classrate_3 * amount_sales

    
    output_results(salesperson_class , salesclerk_num ,amount_sales, commission_rate)
    print('Thank you and Goodbye\n')