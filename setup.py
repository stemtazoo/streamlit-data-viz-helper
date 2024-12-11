from setuptools import setup, find_packages

setup(
    name="streamlit_data_viz_helper",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "matplotlib",
        "streamlit",
        "plotly"
    ],
    description="Tools and utilities for building data visualization apps with Streamlit.",
    author="stemtazoo",
    author_email="stem.sci.tech.eng.math.2013@gmail.com",
)
