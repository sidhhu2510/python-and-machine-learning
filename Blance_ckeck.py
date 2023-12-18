import pandas as pd

df= pd.read_csv(f"D:\\python_task__\\files\\upi_2.csv")
# print(df)
def check_balance(UPI_number):
    while True:
        if UPI_number in df['UPI_number'].values:
            # Extract the balance for the given UPI number
            balance = df.loc[df['UPI_number'] == UPI_number, 'Balance'].values[0]
            Name = df.loc[df['UPI_number'] == UPI_number, 'Name'].values[0]
            print(f"{Name}'s Bank Balance: RS : {balance}\n")
            break
        else:
            print(f"{UPI_number} the UPI Number is invalid \n")
            UPI_number = int(input("Enter UPI ID: "))



