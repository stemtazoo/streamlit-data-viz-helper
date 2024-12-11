import sys
import os
import io

import pytest
import plotly.graph_objects as go

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from streamlit_data_viz_helper.streamlit_helpers import download_chart_html

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
