#Author: Sidon Blake
#Date Created: April 3, 2022
#Course: ITT103
#Purpose: To determine the amount of commission each salesperson will earn based on the  
#the amount they sold and the class in which they belong.

#JamEX Limited salesperson's payroll system


import sys
commission =0.0
    #A function to calculate the commission earned for the respective salesperson.
def process_data(salesperson_num, sales_amt, class_type):
        if (class_type == 1):						
             if (sales_amt <= 1000):
                  comm_rate = 0.06 
             elif (sales_amt > 1000 and sales_amt < 2000):
                  comm_rate = 0.07	   
             else:
                  comm_rate = 0.1
             commission = comm_rate * sales_amt     
             print( "The commission earned is {}".format(commission))
        elif class_type == 2:
                     
             if (sales_amt < 1000): 
                      comm_rate = 0.04
             else:
                  comm_rate = 0.06
             commission = comm_rate * sales_amt
             print( "The commission earned is {}".format(commission))
        elif class_type == 3: 
             comm_rate = 0.045
             commission = comm_rate * sales_amt
             print( "The commission earned is {}".format(commission))
        else: 
             print( "You have entered an incorrect class type.")
            
            
#A Function to determine the valid and invalid user's input   
def input_data():
     response ="y"
     while (response=='y' or response=='Y'):
          try:            
               salesperson_num1 = input("Please enter salesperson's number.: ")
               if(salesperson_num1.isalnum()):
                    salesperson_num = salesperson_num1
               else:
                    a= 1/0                        
               sales_amt=float(input("Please enter sales amount. :"))
               class_type = int(input("Please enter '1','2' or '3' for class type. :"))
               while (class_type !=1 )and (class_type !=2) and(class_type !=3) :
                         class_type = int(input("Please enter '1','2' or '3' for class type. :"))
          except:
               response=input( "Invalid response. Do you want to exit this program? 'y' for Yes and 'n' for no :" )
               if(response =='y'or response=='Y'):
                    prog_exit()
               else:
                    input_data()
                    
          process_data(salesperson_num, sales_amt, class_type)
          response=input( "Do you want to enter another record? Enter 'y' for yes orn or 'N' for no :" )
          if(response =='n' or response=='N'):
               prog_exit()
          if(response=='y' or response=='Y'):
               input_data()

        
def prog_exit():
     sys.exit("Thank you for using JamEx Limited Payroll System. Goodbye.")
        
input_data()

