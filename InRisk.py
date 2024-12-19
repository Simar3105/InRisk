import pandas as pd

# Load the dataset(to be changed acc to user)
data = pd.read_excel("/Users/simarjot/Desktop/InRisk_Labs_Assignment.xlsx")

#preview
#print("Preview of the Data:")
#print(data.head())

# Define threshold
threshold = 60

# Step 1: Number of excess rainfall days for each region
excess_rainfall = data[data['Rainfall_mm'] > threshold].groupby('Region').size()

# Step 2: Calculate claims on excess rainfall
def calculate_claims(excess_days):
    if excess_days <= 10:
        return 0
    elif 11 <= excess_days <= 30:
        return excess_days * 100
    elif 31 <= excess_days <= 50:
        return excess_days * 200
    else:
        return excess_days * 300

# Step 3: Store claims per region
claims_data = pd.DataFrame({
    'Excess_Rainfall_Days': excess_rainfall,
})

#Claims calculation to each region
claims_data['Claim_Amount'] = claims_data['Excess_Rainfall_Days'].apply(calculate_claims)

print("\nRegion-wise Claims:")
print(claims_data)



