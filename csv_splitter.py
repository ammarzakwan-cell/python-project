import pandas as pd
import os
import time

input_file = input("Enter CSV file path: ").strip()

if not input_file:
    print('\x1b[31m' + 'File cannot be empty')
    exit()

try:
    rows_per_file = input("Enter number of rows per file (default: 10000): ").strip()
    rows_per_file = int(rows_per_file) if rows_per_file else 10000

    df = pd.read_csv(
        input_file,
        sep="|",
        dtype=str,
        low_memory=False,
    )

    timestamp = time.strftime("%Y%m%d_%H%M%S")
    output_folder = f"{timestamp}"
    os.makedirs(timestamp, exist_ok=True)

    for i, start_row in enumerate(range(0, len(df), rows_per_file)):
        split_df = df.iloc[start_row:start_row + rows_per_file]
        output_file = os.path.join(output_folder, f"split_part_{i+1}.csv")
        split_df.to_csv(output_file, index=False, sep="|")
        print(f"Saved {output_file} with {len(split_df)} rows")

    print(f"Splitting completed! Files saved in folder: {output_folder}")

except ValueError as ve:
    print('\x1b[31m' + f"Value Error: {ve}")
except Exception as e:
    print('\x1b[31m' + f"Error: {e}")
