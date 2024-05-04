import pandas as pd

def aggregate_data(data, category_column, numerical_column):
    # Group the data by category column
    grouped_data = data.groupby(category_column)

    # Aggregate numerical column by calculating the mean
    aggregated_data = grouped_data.agg({numerical_column: 'mean'})

    return aggregated_data

if __name__ == "__main__":

    data = pd.read_csv("/content/sample_data/pm-data set.csv")  # Update with your dataset filename

    # Name of the category column
    category_column = "Maintenance History"  # Update with the name of your category column

    # Name of the numerical column to aggregate
    numerical_column = "Sensor 1 (Temperature)"  # Update with the name of your numerical column

    # Aggregate the data
    aggregated_data = aggregate_data(data, category_column, numerical_column)

    # Display the aggregated data
    print("Aggregated Data:")
    print(aggregated_data)