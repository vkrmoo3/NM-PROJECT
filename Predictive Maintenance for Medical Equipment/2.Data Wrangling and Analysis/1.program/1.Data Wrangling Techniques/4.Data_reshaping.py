import pandas as pd

def transpose_dataset(dataset_path):
    # Read the dataset
    df = pd.read_csv(dataset_path)

    # Transpose the dataset
    transposed_data = df.T

    return transposed_data

if __name__ == "__main__":
    # Path to the dataset
    dataset_path = "/content/sample_data/pm-data set.csv"  # Update with your dataset filename

    # Transpose the dataset
    transposed_data = transpose_dataset(dataset_path)

    # Display transposed dataset
    print("Transposed Dataset:")
    print(transposed_data)