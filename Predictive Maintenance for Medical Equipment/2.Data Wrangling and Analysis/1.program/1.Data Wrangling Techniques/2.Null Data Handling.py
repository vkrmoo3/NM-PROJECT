import pandas as pd

def null_data_handling(data):
    # Display the number of missing values for each column
    print("Missing Values:")
    print(data.isnull().sum())

    # Drop rows with missing values
    data_cleaned = data.dropna()

    # Optional: Display the shape of the original and cleaned datasets
    print("\nOriginal Dataset Shape:", data.shape)
    print("Cleaned Dataset Shape:", data_cleaned.shape)

    return data_cleaned

if __name__ == "__main__":
    # Assuming 'data' is your pandas DataFrame
    # If not, replace 'data' with the name of your DataFrame
    data = pd.read_csv("/content/sample_data/pm-data set.csv")  # Update with your dataset filename

    # Null data handling
    cleaned_data = null_data_handling(data)
