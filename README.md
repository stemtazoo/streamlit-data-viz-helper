# Streamlit Data Viz Helper

A Python library for simplifying data processing and visualization tasks, especially for use with Streamlit apps. This library provides utility functions to handle common file formats, interactive data filtering, and Plotly chart integrations.

## Features

- **Load and Clean Data**: Functions for loading and cleaning CSV and Excel files.
- **Data Visualization**: Create scatter plots, bar charts, line charts, and histograms using Plotly.
- **Interactive Data Filtering**: Add UI filters to dataframes in Streamlit apps.
- **Download Charts**: Easily download Plotly charts as HTML files.

## Installation

To install the library for normal use:

```bash
pip install .
```

For development mode:

```bash
pip install -e .
```

## Usage

### 1. Load and Clean Data

Example for loading a CSV file:
```python
from streamlit_data_viz_helper.data_processing import load_csv_to_dataframe

df = load_csv_to_dataframe("data.csv", encoding="utf-8")
print(df.head())
```

### 2. Create Visualizations

Example for creating a scatter plot:
```python
from streamlit_data_viz_helper.visualization import create_scatter_plot

fig = create_scatter_plot(df, x="column_x", y="column_y", legend="category", title="My Scatter Plot")
fig.show()
```

### 3. Add Download Button for Charts

Example for adding a download button to save a chart as an HTML file:
```python
from streamlit_data_viz_helper.streamlit_helpers import download_chart_html

# In your Streamlit app
download_chart_html(fig, "my_chart")
```

### 4. Interactive Data Filtering

Example for filtering a dataframe interactively in a Streamlit app:
```python
from streamlit_data_viz_helper.streamlit_helpers import filter_dataframe

# In your Streamlit app
filtered_df = filter_dataframe(df)
st.write(filtered_df)
```

## Development

If you make changes to the library and need to rebuild:

1. Update the version in `setup.py`.
2. Reinstall the library locally:
   ```bash
   pip install -e .
   ```

To build a distributable package:
```bash
python setup.py sdist
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.
