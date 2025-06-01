import pandas as pd
from sklearn.model_selection import train_test_split
import os

INPUT_FILE_PATH = "data/Business.csv"  # <-- Set your full input CSV path here
OUTPUT_DIR_PATH = "splits/output"     # <-- Set your full output directory path here
TARGET_COLUMN = None                  # <-- Set your target column name if you want stratification
TEST_SIZE = 0.2                        # <-- Fraction of dataset to allocate for test + validation
VAL_SIZE = 0.5                         # <-- Fraction of temp set to allocate to validation
RANDOM_STATE = 42                      # <-- Random seed for reproducibility

def load_data(file_path):
    """Load CSV data."""
    if not os.path.exists(file_path):
        print(f"❌ Input file not found: {file_path}", flush=True)
        raise FileNotFoundError(f"Input file not found: {file_path}")
    print(f"✅ Loading data from: {file_path}", flush=True)
    return pd.read_csv(file_path)

def save_data(df, output_path):
    """Save DataFrame to CSV."""
    print(f"💾 Saving data to: {output_path}", flush=True)
    df.to_csv(output_path, index=False)

def create_output_dir(output_dir):
    """Create directory if it doesn't exist."""
    if not os.path.exists(output_dir):
        print(f"📁 Creating output directory: {output_dir}", flush=True)
        os.makedirs(output_dir)

def split_data(df, target_column=None, test_size=0.2, val_size=0.5, random_state=42):
    """Split data into train, validation, and test sets."""
    stratify = df[target_column] if target_column else None
    train_df, temp_df = train_test_split(
        df,
        test_size=test_size,
        stratify=stratify,
        random_state=random_state
    )

    stratify_temp = temp_df[target_column] if target_column else None
    val_df, test_df = train_test_split(
        temp_df,
        test_size=val_size,
        stratify=stratify_temp,
        random_state=random_state
    )

    return train_df, val_df, test_df

def split_csv(file_path, target_column=None, output_dir='splits', test_size=0.2, val_size=0.5, random_state=42):
    """
    Main function to split CSV into train/val/test sets.

    Args:
        file_path (str): Path to the input CSV file.
        target_column (str, optional): Column to stratify on. If None, no stratification.
        output_dir (str): Directory to save the splits.
        test_size (float): Proportion of data for test + validation.
        val_size (float): Proportion of temp set to allocate to validation.
        random_state (int): Random seed for reproducibility.
    """

    df = load_data(file_path)
    create_output_dir(output_dir)

    train_df, val_df, test_df = split_data(
        df,
        target_column=target_column,
        test_size=test_size,
        val_size=val_size,
        random_state=random_state
    )

    save_data(train_df, os.path.join(output_dir, 'train.csv'))
    save_data(val_df, os.path.join(output_dir, 'val.csv'))
    save_data(test_df, os.path.join(output_dir, 'test.csv'))

    print(f"\n✅ Splits completed!", flush=True)
    print(f"Train: {len(train_df)} samples", flush=True)
    print(f"Validation: {len(val_df)} samples", flush=True)
    print(f"Test: {len(test_df)} samples", flush=True)

def main():
    print(f"🚀 Starting CSV Splitter", flush=True)
    print(f"Input file: {INPUT_FILE_PATH}", flush=True)
    print(f"Output directory: {OUTPUT_DIR_PATH}", flush=True)

    split_csv(
        file_path=INPUT_FILE_PATH,
        target_column=TARGET_COLUMN,
        output_dir=OUTPUT_DIR_PATH,
        test_size=TEST_SIZE,
        val_size=VAL_SIZE,
        random_state=RANDOM_STATE
    )

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"❌ Error: {e}", flush=True)
        exit(1)