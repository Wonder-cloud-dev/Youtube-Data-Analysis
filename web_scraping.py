import pandas as pd
import kagglehub

# Step 1: Download the dataset
print("Downloading the dataset from Kaggle...")
dataset_path = kagglehub.dataset_download("nelgiriyewithana/global-youtube-statistics-2023")
print("Dataset downloaded to:", dataset_path)

# Step 2: Specify the exact file name and path
input_file = f"{dataset_path}/Global YouTube Statistics.csv"  # Update based on your dataset
output_file = "output.xlsx"  # Output file will be saved in the same directory as this script

# Step 3: Load the dataset
try:
    print("Loading the dataset...")
    df = pd.read_csv(input_file, encoding="utf-8", on_bad_lines="skip")
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print(f"File not found at {input_file}. Check if the dataset was downloaded correctly.")
    exit(1)
except Exception as e:
    print("Error loading the dataset:", e)
    exit(1)

# Step 4: Clean the data
print("Cleaning the data...")
df = df.drop_duplicates()  # Remove duplicates
if 'Price' in df.columns:  # Example column cleaning
    df['Price'] = df['Price'].fillna(df['Price'].mean())

# Step 5: Save the cleaned data to an Excel file
try:
    print("Saving the cleaned data to an Excel file...")
    df.to_excel(output_file, index=False, engine="openpyxl")
    print(f"Cleaned data saved to {output_file}!")
except Exception as e:
    print("Error saving the file:", e)
    exit(1)
