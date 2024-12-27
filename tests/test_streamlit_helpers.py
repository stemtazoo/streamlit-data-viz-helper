import sys
import os
import io

import pytest
import plotly.graph_objects as go
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from streamlit_data_viz_helper.streamlit_helpers import download_chart_html, filter_dataframe, download_csv_jis, show_df_with_expander

@pytest.fixture
def sample_plot():
    """
    Create a sample Plotly figure for testing.
    """
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6], mode='lines', name='Test'))
    return fig

def test_download_chart_html(sample_plot):
    """
    Test the download_chart_html function.
    """
    # Prepare a sample title
    title = "test_chart"

    # Mock the Streamlit download_button
    def mock_download_button(label, data, file_name, mime):
        assert label == "Download Chart"
        assert data is not None
        assert file_name == f"{title}.html"
        assert mime == "text/html"

    # Replace the Streamlit download_button with the mock
    import streamlit as st
    st.download_button = mock_download_button

    # Call the function
    download_chart_html(sample_plot, title)

def sample_dataframe():
    """Provide a sample DataFrame for testing."""
    data = {
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [25, 30, 35],
        "City": ["Tokyo", "Osaka", "Nagoya"]
    }
    return pd.DataFrame(data)

def test_filter_dataframe(sample_dataframe):
    """Test filter_dataframe function."""
    # Check if DataFrame is returned unchanged when no filters are applied
    result_df = filter_dataframe(sample_dataframe)
    pd.testing.assert_frame_equal(result_df, sample_dataframe)

def test_download_csv_jis(sample_dataframe):
    """Test download_csv_jis function (mock Streamlit download)."""
    # Check that CSV encoding is successful
    try:
        download_csv_jis(sample_dataframe, "test_file")
    except Exception as e:
        pytest.fail(f"download_csv_jis raised an exception: {e}")

def test_show_df_with_expander(sample_dataframe, mocker):
    """Test show_df_with_expander function."""
    # Mock Streamlit components to avoid actual UI rendering
    mock_expander = mocker.patch("streamlit.expander")
    mock_dataframe = mocker.patch("streamlit.dataframe")
    mock_download = mocker.patch("streamlit.markdown")

    try:
        show_df_with_expander(sample_dataframe, title="test_data")
        mock_expander.assert_called_once_with("See data!", expanded=False)
        mock_dataframe.assert_called_once_with(sample_dataframe)
    except Exception as e:
        pytest.fail(f"show_df_with_expander raised an exception: {e}")