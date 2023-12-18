import pandas as pd

# Read the dataset
df = pd.read_csv("D:\\python_task__\\files\\upi_2.csv")

def report_fraud(upi_number, fraud_report):

    try:
        # Check if the UPI number exists in the DataFrame
        if upi_number in df['UPI_number'].values:
            # Update 'IsFraud' to 1 and set 'IsFraud Report'
            df.loc[df['UPI_number'] == upi_number, 'isFraud'] = 1
            df.loc[df['UPI_number'] == upi_number, 'IsFraud Report'] = fraud_report


            print(f"Fraud reported successfully for UPI number {upi_number}. Report: {fraud_report}\n")
            df.to_csv("D:\\python_task__\\files\\upi_2.csv", index=False)
            return True
        else:
            print(f"Error: UPI number {upi_number} not found. Fraud report failed.\n")
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False

# reported_upi_number = int(input("Enter the Reporting UPI Number : "))
# fraud_report_description = str(input("Enter the Reason for Fraud Report : "))
#
# # Report fraud for the given UPI number
# report_fraud(reported_upi_number, fraud_report_description)

# Save the updated DataFrame to the same or a new CSV file
# df.to_csv("D:\\python_task__\\files\\upi_2.csv", index=False)
# print(df)
