import pandas as pd

test_csv_path = 'Test.csv'
categories_csv_path = 'cleaned_fixed_categories.csv'

test_data = pd.read_csv(test_csv_path)

categories_data = pd.read_csv(categories_csv_path)

test_data['CPU Name'] = test_data['CPU Name']
categories_data['CPU Name'] = categories_data['CPU Name']

for index, row in test_data.iterrows():
    if row['Category'] == 'Unknown':
        for _, category_row in categories_data.iterrows():
            if row['CPU Name'] == category_row['CPU Name']:
                test_data.at[index, 'Category'] = category_row['Category']
                break

updated_test_csv_path = 'Updated_Test.csv'
test_data.to_csv(updated_test_csv_path, index=False)

print("\nUpdated Test DataFrame:")
print(test_data)

remaining_unknowns = test_data[test_data['Category'] == 'Unknown'].shape[0]
print(f"\nRemaining 'Unknown' categories: {remaining_unknowns}")

print(f"\nUpdated data saved to: {updated_test_csv_path}")
