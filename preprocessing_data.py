import os
import pandas as pd

# Define file paths
input_file = r"F:\Data\Churn_Modelling.csv"  # Raw dataset file
output_dir = r"F:\Data\PowerBI\Cleaned_Data"  # Output directory
output_file = os.path.join(output_dir, "cleaned_churn_data.csv")  # Path to save cleaned data

# Ensure the output directory exists before saving
os.makedirs(output_dir, exist_ok=True)  # Creates the folder if it doesn’t exist

df = pd.read_csv(input_file)

# Rename columns for better readability
df.rename(columns={
    "RowNumber": "Row_Number",
    "CustomerId": "Customer_ID",
    "Surname": "Last_Name",
    "CreditScore": "Credit_Score",
    "Geography": "Country",
    "Gender": "Gender",
    "Age": "Age",
    "Tenure": "Tenure_Years",
    "Balance": "Account_Balance",
    "NumOfProducts": "Number_of_Products",
    "HasCrCard": "Has_Credit_Card",
    "IsActiveMember": "Is_Active_Member",
    "EstimatedSalary": "Estimated_Salary",
    "Exited": "Churn"
}, inplace=True)

# Handle missing values
df.fillna({
    "Account_Balance": 0,  # Fill missing balances with 0
    "Estimated_Salary": df["Estimated_Salary"].median(),  # Fill missing salaries with median
}, inplace=True)

# Convert data types
df["Age"] = df["Age"].astype(int)
df["Credit_Score"] = df["Credit_Score"].astype(int)
df["Estimated_Salary"] = df["Estimated_Salary"].astype(float)

# Save the cleaned data
df.to_csv(output_file, index=False)

print(f"Data preprocessing completed. Cleaned file saved at: {output_file}")
