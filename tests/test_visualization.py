import sys
import os

import pytest
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from streamlit_data_viz_helper.visualization import create_scatter_plot, create_bar_chart, create_line_chart, create_histogram

def test_create_scatter_plot():
    # Create a sample DataFrame
    data = {
        "x": [1, 2, 3, 4, 5],
        "y": [10, 20, 30, 40, 50],
        "category": ["A", "B", "A", "B", "A"]
    }
    df = pd.DataFrame(data)

    # Test with x and y only
    fig = create_scatter_plot(df, x="x", y="y")
    assert fig is not None
    assert fig.layout.title.text is None  # Update to check for None
    assert len(fig.data) == 1

    # Test with x, y, and legend
    fig_with_legend = create_scatter_plot(df, x="x", y="y", legend="category")
    assert fig_with_legend is not None
    assert set(data["category"]) == set(trace.name for trace in fig_with_legend.data)

    # Test with a title
    title = "Test Scatter Plot"
    fig_with_title = create_scatter_plot(df, x="x", y="y", title=title)
    assert fig_with_title.layout.title.text == title

    # Test with invalid column names
    with pytest.raises(ValueError):
        create_scatter_plot(df, x="invalid", y="y")

    with pytest.raises(ValueError):
        create_scatter_plot(df, x="x", y="invalid")

def test_create_bar_chart():
    # Create a sample DataFrame
    data = {
        "x": ["A", "B", "C"],
        "y": [10, 20, 30]
    }
    df = pd.DataFrame(data)

    # Test bar chart creation
    fig = create_bar_chart(df, x="x", y="y")
    assert fig is not None
    assert fig.layout.title.text is None
    assert len(fig.data) == 1

    # Test with a title
    title = "Test Bar Chart"
    fig_with_title = create_bar_chart(df, x="x", y="y", title=title)
    assert fig_with_title.layout.title.text == title

def test_create_line_chart():
    # Create a sample DataFrame
    data = {
        "x": [1, 2, 3, 4, 5],
        "y": [10, 20, 30, 40, 50]
    }
    df = pd.DataFrame(data)

    # Test line chart creation
    fig = create_line_chart(df, x="x", y="y")
    assert fig is not None
    assert fig.layout.title.text is None
    assert len(fig.data) == 1

    # Test with a title
    title = "Test Line Chart"
    fig_with_title = create_line_chart(df, x="x", y="y", title=title)
    assert fig_with_title.layout.title.text == title

def test_create_histogram():
    # Create a sample DataFrame
    data = {
        "x": [1, 2, 2, 3, 3, 3, 4]
    }
    df = pd.DataFrame(data)

    # Test histogram creation
    fig = create_histogram(df, x="x")
    assert fig is not None
    assert fig.layout.title.text is None
    assert len(fig.data) == 1

    # Test with a title
    title = "Test Histogram"
    fig_with_title = create_histogram(df, x="x", title=title)
    assert fig_with_title.layout.title.text == title
