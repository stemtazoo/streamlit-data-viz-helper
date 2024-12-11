from setuptools import setup, find_packages

# Load the version from the package
with open("streamlit_data_viz_helper/__init__.py") as f:
    for line in f:
        if line.startswith("__version__"):
            __version__ = line.split("=")[1].strip().strip("\"'")
            break

setup(
    name="streamlit-data-viz-helper",
    version=__version__,  # Use the version from __init__.py
    description="Tools and utilities for building data visualization apps with Streamlit.",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "streamlit",
        "pandas",
        "plotly",
        "chardet"
    ],
)
