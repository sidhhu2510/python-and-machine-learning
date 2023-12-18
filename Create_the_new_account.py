import csv
import random
from pin_number import UPI_number_gen,get_user_pin,add_upi_account

import random
import csv
def UPI_number_gen():
    random_number = random.randint(10**9, (10**10)-1)
    return random_number

def get_user_pin():
    while True:
        try:
            pin = int(input("Enter a 4-digit PIN: "))
            if 1000 <= pin <= 9999:
                return pin
            else:
                print("Invalid PIN. Please enter a 4-digit number.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def add_upi_account(Name,Balance,Upi_Number,Pin_number):
    with open("D:\\python_task__\\files\\upi_2.csv", 'a', newline="") as file:
        file2 = csv.writer(file)
        file2.writerow([Name, Balance, Upi_Number,Pin_number, 0, 'none'])
        print("Your UPI Account is successfully Create\n")
    file.close()

