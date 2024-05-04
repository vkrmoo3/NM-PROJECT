import pandas as pd

def merge_datasets(data1_path, data2_path, common_column):
    # Read the datasets
    data1 = pd.read_csv(data1_path)
    data2 = pd.read_csv(data2_path)

    # Merge the datasets based on the common column
    merged_data = pd.merge(data1, data2, on=common_column)

    return merged_data

if __name__ == "__main__":
    # Paths to the datasets
    data1_path = "/content/sample_data/pm-data set.csv"  # Update with the filename of the first dataset
    data2_path = "/content/sample_data/pm2.csv"  # Update with the filename of the second dataset

    # Common column to merge on
    common_column = "Equipment ID"  # Update with the name of the common column

    # Merge the datasets
    merged_data = merge_datasets(data1_path, data2_path, common_column)

    # Display the merged dataset
    print("Merged Dataset:")
    print(merged_data)