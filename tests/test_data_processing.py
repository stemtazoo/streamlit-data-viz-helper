import sys
import os
import pandas as pd
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from streamlit_data_viz_helper.data_processing import load_csv_to_dataframe, load_excel_to_dataframe, load_all_files_in_folder

# テスト用のサンプルデータ作成
@pytest.fixture
def sample_csv(tmp_path):
    file_path = tmp_path / "sample.csv"
    data = "Name,Age,Gender\nAlice,30,Female\nBob,25,Male"
    file_path.write_text(data, encoding="utf-8")
    return file_path

@pytest.fixture
def sample_excel(tmp_path):
    file_path = tmp_path / "sample.xlsx"
    df = pd.DataFrame({"Name": ["Alice", "Bob"], "Age": [30, 25], "Gender": ["Female", "Male"]})
    df.to_excel(file_path, index=False)
    return file_path

@pytest.fixture
def sample_folder(tmp_path):
    # CSVファイル作成
    csv_file = tmp_path / "data1.csv"
    csv_file.write_text("Name,Age,Gender\nAlice,30,Female\nBob,25,Male", encoding="utf-8")
    # Excelファイル作成
    excel_file = tmp_path / "data2.xlsx"
    pd.DataFrame({"Name": ["Charlie"], "Age": [35], "Gender": ["Male"]}).to_excel(excel_file, index=False)
    return tmp_path

# CSV読み込みのテスト
def test_load_csv_to_dataframe(sample_csv):
    df = load_csv_to_dataframe(sample_csv)
    assert not df.empty
    assert list(df.columns) == ["Name", "Age", "Gender"]
    assert len(df) == 2

# Excel読み込みのテスト
def test_load_excel_to_dataframe(sample_excel):
    df = load_excel_to_dataframe(sample_excel)
    assert not df.empty
    assert list(df.columns) == ["Name", "Age", "Gender"]
    assert len(df) == 2

def test_load_all_files_in_folder(sample_folder):
    df = load_all_files_in_folder(sample_folder, include_subfolders=False)
    assert not df.empty
    assert len(df) == 2  # CSV 2行のみ

def test_load_all_files_in_folder_with_subfolders(tmp_path, sample_folder):
    # サブフォルダ作成
    subfolder = tmp_path / "subfolder"
    subfolder.mkdir()
    csv_file_in_subfolder = subfolder / "data3.csv"
    csv_file_in_subfolder.write_text("Name,Age,Gender\nEve,28,Female", encoding="utf-8")

    df = load_all_files_in_folder(tmp_path, include_subfolders=True)
    assert not df.empty
    assert len(df) == 3  # 2行 (元データ) + 1行 (サブフォルダ)

# エンコーディングエラーのテスト
def test_load_csv_with_encoding_error(tmp_path):
    file_path = tmp_path / "sample_shiftjis.csv"
    data = "名前,年齢,性別\n花子,29,女性\n太郎,35,男性".encode("shift_jis")
    file_path.write_bytes(data)
    
    df = load_csv_to_dataframe(file_path)
    assert not df.empty
    assert list(df.columns) == ["名前", "年齢", "性別"]
    assert len(df) == 2
