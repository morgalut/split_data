```markdown
# CSV Splitter

🚀 A simple and efficient script to split a large CSV file into **Train**, **Validation**, and **Test** datasets.

---

## 📦 Features
- Splits a CSV into **train**, **validation**, and **test** sets.
- Supports **stratified splitting** (optional) if you provide a target column.
- Handles missing input files with friendly error messages.
- Automatically creates output folders.
- Lightweight and easy to use.

---

## 📂 Project Structure

```

split/
├── data/
│   └── Business.csv        # Your input CSV file
├── splits/
│   └── output/
│       ├── train.csv       # Train set (80%)
│       ├── val.csv         # Validation set (10%)
│       └── test.csv        # Test set (10%)
├── split\_csv.py             # Main script
└── README.md

````

---

## 🛠️ Requirements

Make sure you have Python 3.x installed. Then install the required packages:

```bash
pip install pandas scikit-learn
````

---

## 🚀 How to Use

1. **Place your input CSV** in the `data/` folder (e.g., `data/Business.csv`).
2. **Configure the paths** inside `split_csv.py`:

   ```python
   INPUT_FILE_PATH = "data/Business.csv"
   OUTPUT_DIR_PATH = "splits/output"
   TARGET_COLUMN = None  # or set to your column name if stratified splitting needed
   TEST_SIZE = 0.2       # 20% for validation+test
   VAL_SIZE = 0.5        # 50% of the 20% split equally into val/test
   RANDOM_STATE = 42
   ```
3. **Run the script**:

   ```bash
   python split_csv.py
   ```

---

## 🧮 How the Splitting Works

| Set            | Percentage | Notes                      |
| -------------- | ---------- | -------------------------- |
| **Train**      | 80%        | Main training dataset      |
| **Validation** | 10%        | For model validation       |
| **Test**       | 10%        | For final model evaluation |

First split into:

* 80% Train
* 20% Temp (to split into Validation/Test)

Then split Temp into:

* 50% Validation
* 50% Test

---
