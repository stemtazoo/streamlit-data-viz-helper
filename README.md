# Streamlit Data Viz Helper

A Python library for simplifying data processing and visualization tasks, especially for use with Streamlit apps. This library provides utility functions to handle common file formats like CSV and Excel, and to combine multiple files into a single DataFrame.

## Features

- **Load CSV Files**: Handles encoding issues and automatically detects encoding if an error occurs.
- **Load Excel Files**: Easily load data from Excel files with customizable headers and sheet selection.
- **Combine Multiple Files**: Combine all CSV and Excel files in a folder (with optional subfolder support) into a single DataFrame.

## Installation

To use this library, clone the repository and install it locally:

```bash
pip install -e .
```

## Usage

### 1. Load a CSV File

```python
from streamlit_data_viz_helper.data_processing import load_csv_to_dataframe

df = load_csv_to_dataframe("data.csv", encoding="utf-8")
print(df.head())
```

### 2. Load an Excel File

```python
from streamlit_data_viz_helper.data_processing import load_excel_to_dataframe

df = load_excel_to_dataframe("data.xlsx", sheet_name=0)
print(df.head())
```

### 3. Combine All Files in a Folder

```python
from streamlit_data_viz_helper.data_processing import load_all_files_in_folder

df = load_all_files_in_folder("data_folder", include_subfolders=True)
print(df.head())
```

## Contributing

Contributions are welcome! If you'd like to improve this library or add new features, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
