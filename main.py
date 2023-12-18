from Create_the_new_account import UPI_number_gen, get_user_pin, add_upi_account
from pay_upi import transfer_money
from UPI_Fraud_detection import UPI_Fraud_Detection
from Fraud_Report import report_fraud
from  Blance_ckeck  import check_balance
import pandas as pd

df = pd.read_csv("D:\\python_task__\\files\\upi_2.csv")
while True:
    print("               -----   Welcome To UPI   -----             ")
    print("1 Create the  new UPI account ")
    print("2 UPI MONEY TRANSFER")
    print("3 UPI Fraud detection")
    print("4 Fraud Report")
    print("5 Balance check")
    print("6 exit\n")


    user = int(input(" Enter the Number : "))

    if user == 1:
        name = str(input("Enter Your Name : "))
        Blance = int(input("Enter the Deposite Amount : "))
        Upi_number = UPI_number_gen()
        Pin_number = get_user_pin()
        add_upi_account(name, Blance, Upi_number, Pin_number)
        # print(df)

    elif user == 2:
        # Provide giver's and receiver's UPI numbers, the amount to transfer, and the PIN for the giver's UPI
        giver_upi_number = int(input("Enter your UPI Number: "))
        receiver_upi_number = int(input("Enter the money receiver's UPI number: "))
        transfer_amount = int(input("Enter the transfer amount: "))
        giver_pin = input("Enter your 4-digit PIN: ")
        transfer_money(giver_upi_number, receiver_upi_number, transfer_amount, giver_pin)
        # print(df)

    elif user == 3:
        UPI_number = (input("Enter the upi number : "))
        UPI_Fraud_Detection(UPI_number)


    elif user == 4:
        reported_upi_number = int(input("Enter the Reporting UPI Number : "))
        fraud_report_description = str(input("Enter the Reason for Fraud Report : "))
        # Report fraud for the given UPI number
        report_fraud(reported_upi_number, fraud_report_description)
        # print(df)

    elif user == 5:
        UPI_number = int(input("Enter the UPI Number : "))
        check_balance(UPI_number)
        # print(df)

    elif user == 6:
        break

    else:
        print("invalid number")