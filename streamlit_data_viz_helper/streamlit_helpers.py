import io
import streamlit as st

def download_chart_html(fig, title):
    """
    Add a download button in a Streamlit app to save a Plotly chart as an HTML file.

    Args:
        fig (plotly.graph_objs._figure.Figure): The Plotly figure to be saved.
        title (str): The title of the file to save (used as the filename).
    """
    try:
        html_buff = io.StringIO()
        fig.write_html(html_buff, include_plotlyjs='cdn')
        html_bytes = html_buff.getvalue().encode()
        st.download_button(
            label='Download Chart',
            data=html_bytes,
            file_name=f"{title}.html",
            mime='text/html'
        )
    except Exception as e:
        st.error(f"An error occurred while creating the download button: {e}")
