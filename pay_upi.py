import pandas as pd

df = pd.read_csv("D:\\python_task__\\files\\upi_2.csv")

def verify_pin(upi_number, entered_pin):
    correct_pin = df.loc[df['UPI_number'] == upi_number, 'Pin Number'].values[0]
    return str(entered_pin) == str(correct_pin)

def transfer_money(giver_upi, receiver_upi, amount, pin):
    # Check if both UPI numbers exist in the DataFrame
    if giver_upi in df['UPI_number'].values and receiver_upi in df['UPI_number'].values:
        # Verify PIN for the giver's UPI
        if verify_pin(giver_upi, pin):
            # Extract balances for giver and receiver UPI numbers
            giver_balance = df.loc[df['UPI_number'] == giver_upi, 'Balance'].values[0]
            receiver_balance = df.loc[df['UPI_number'] == receiver_upi, 'Balance'].values[0]

            if giver_upi == receiver_upi:
                print(f"Error: The UPI Number for giver and receiver is the same. Transfer failed.\n")
            # Check if the giver has sufficient balance
            elif giver_balance >= amount:
                # Update balances after the transfer
                df.loc[df['UPI_number'] == giver_upi, 'Balance'] -= amount
                df.loc[df['UPI_number'] == receiver_upi, 'Balance'] += amount

                message = f"Money transferred successfully from UPI {giver_upi} to UPI {receiver_upi}.\n"
                print(message)
                # Save the updated DataFrame to the CSV file
                df.to_csv("D:\\python_task__\\files\\upi_2.csv", index=False)
            else:
                message = f"Error: Insufficient balance for UPI {giver_upi}. Transfer failed.\n"
                print(message)
        else:
            message = "Error: Incorrect PIN. Transfer failed.\n"
            print(message)
    else:
        message = "Error: UPI number not found. Transfer failed.\n"
        print(message)

# # Provide giver's and receiver's UPI numbers, the amount to transfer, and the PIN for the giver's UPI
# giver_upi_number = int(input("Enter your UPI Number: "))
# receiver_upi_number = int(input("Enter the money receiver's UPI number: "))
# transfer_amount = int(input("Enter the transfer amount: "))
# giver_pin = input("Enter your 4-digit PIN: ")
#
# transfer_money(giver_upi_number, receiver_upi_number, transfer_amount, giver_pin)
# print(df)