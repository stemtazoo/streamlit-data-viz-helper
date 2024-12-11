import os

import pandas as pd
import chardet

def load_csv_to_dataframe(file_path, encoding='utf-8', sep=',', header='infer', index_col=None):
    """
    Load a CSV file into a DataFrame with error handling for encoding issues.

    Args:
        file_path (str): The path to the CSV file.
        encoding (str): The initial encoding to try (default is 'utf-8').
        sep (str): The delimiter to use (default is ',').
        header (int, list of int, or 'infer'): Row number(s) to use as column names (default is 'infer').
        index_col (int, str, sequence of int/str, or False): Column(s) to set as index (default is None).

    Returns:
        pd.DataFrame: The loaded DataFrame.
    """
    try:
        # Try loading the file with the provided encoding
        df = pd.read_csv(file_path, encoding=encoding, sep=sep, header=header, index_col=index_col)
        return df
    except UnicodeDecodeError:
        # If encoding error occurs, try to detect the correct encoding
        with open(file_path, 'rb') as f:
            result = chardet.detect(f.read())
            detected_encoding = result['encoding']

        print(f"Encoding error detected. Retrying with detected encoding: {detected_encoding}")

        try:
            # Reload the file with the detected encoding
            df = pd.read_csv(file_path, encoding=detected_encoding, sep=sep, header=header, index_col=index_col)
            return df
        except Exception as e:
            raise ValueError(f"Failed to load the file even after detecting encoding. Error: {e}")
    except Exception as e:
        raise ValueError(f"An error occurred while loading the file: {e}")

def load_excel_to_dataframe(file_path, sheet_name=0, header=0, index_col=None):
    """
    Load an Excel file into a DataFrame.

    Args:
        file_path (str): The path to the Excel file.
        sheet_name (str or int or list): Name or index of the sheet(s) to load (default is 0).
        header (int, list of int, or None): Row number(s) to use as column names (default is 0).
        index_col (int, str, sequence of int/str, or False): Column(s) to set as index (default is None).

    Returns:
        pd.DataFrame: The loaded DataFrame.
    """
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name, header=header, index_col=index_col)
        return df
    except Exception as e:
        raise ValueError(f"An error occurred while loading the Excel file: {e}")

def load_all_files_in_folder(folder_path, file_types=('csv', 'xlsx'), include_subfolders=False, encoding='utf-8', sep=',', header='infer', index_col=None):
    """
    Load all CSV and Excel files in a folder (and optionally its subfolders) and combine them into a single DataFrame.

    Args:
        folder_path (str): The path to the folder containing the files.
        file_types (tuple): Tuple of file extensions to include (default is ('csv', 'xlsx')).
        include_subfolders (bool): Whether to include files in subfolders (default is False).
        encoding (str): The encoding to use for CSV files (default is 'utf-8').
        sep (str): The delimiter to use for CSV files (default is ',').
        header (int, list of int, or 'infer'): Row number(s) to use as column names (default is 'infer').
        index_col (int, str, sequence of int/str, or False): Column(s) to set as index (default is None).

    Returns:
        pd.DataFrame: A single DataFrame containing data from all files.
    """
    all_dataframes = []

    if include_subfolders:
        # Walk through all subdirectories
        for root, _, files in os.walk(folder_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                file_extension = file_name.split('.')[-1].lower()

                if file_extension == 'csv' and 'csv' in file_types:
                    try:
                        df = load_csv_to_dataframe(file_path, encoding=encoding, sep=sep, header=header, index_col=index_col)
                        all_dataframes.append(df)
                    except Exception as e:
                        print(f"Error loading CSV file {file_name}: {e}")

                elif file_extension in ['xls', 'xlsx'] and 'xlsx' in file_types:
                    try:
                        df = load_excel_to_dataframe(file_path, header=header, index_col=index_col)
                        all_dataframes.append(df)
                    except Exception as e:
                        print(f"Error loading Excel file {file_name}: {e}")
    else:
        # Only look in the specified folder
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            file_extension = file_name.split('.')[-1].lower()

            if file_extension == 'csv' and 'csv' in file_types:
                try:
                    df = load_csv_to_dataframe(file_path, encoding=encoding, sep=sep, header=header, index_col=index_col)
                    all_dataframes.append(df)
                except Exception as e:
                    print(f"Error loading CSV file {file_name}: {e}")

            elif file_extension in ['xls', 'xlsx'] and 'xlsx' in file_types:
                try:
                    df = load_excel_to_dataframe(file_path, header=header, index_col=index_col)
                    all_dataframes.append(df)
                except Exception as e:
                    print(f"Error loading Excel file {file_name}: {e}")

    if all_dataframes:
        combined_dataframe = pd.concat(all_dataframes, ignore_index=True)
        return combined_dataframe
    else:
        raise ValueError("No valid files found in the folder.")
