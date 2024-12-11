import plotly.express as px

colors = px.colors.qualitative.Light24

def create_scatter_plot(df, x, y, legend=None, title=None):
    """
    Create a scatter plot using Plotly Express.

    Args:
        df (pd.DataFrame): The DataFrame containing the data to plot.
        x (str): The column name for the x-axis.
        y (str): The column name for the y-axis.
        legend (str, optional): The column name for the legend (color grouping). Default is None.
        title (str, optional): The title of the scatter plot. Default is None.

    Returns:
        plotly.graph_objs._figure.Figure: The created scatter plot figure.
    """
    try:
        fig = px.scatter(df, x=x, y=y, color=legend, title=title, color_discrete_sequence=colors)
        return fig
    except Exception as e:
        raise ValueError(f"An error occurred while creating the scatter plot: {e}")

def create_bar_chart(df, x, y, legend=None, title=None):
    """
    Create a bar chart using Plotly Express.

    Args:
        df (pd.DataFrame): The DataFrame containing the data to plot.
        x (str): The column name for the x-axis.
        y (str): The column name for the y-axis.
        legend (str, optional): The column name for the legend (color grouping). Default is None.
        title (str, optional): The title of the bar chart. Default is None.

    Returns:
        plotly.graph_objs._figure.Figure: The created bar chart figure.
    """
    try:
        fig = px.bar(df, x=x, y=y, color=legend, title=title, color_discrete_sequence=colors)
        return fig
    except Exception as e:
        raise ValueError(f"An error occurred while creating the bar chart: {e}")

def create_line_chart(df, x, y, legend=None, title=None):
    """
    Create a line chart using Plotly Express.

    Args:
        df (pd.DataFrame): The DataFrame containing the data to plot.
        x (str): The column name for the x-axis.
        y (str): The column name for the y-axis.
        legend (str, optional): The column name for the legend (color grouping). Default is None.
        title (str, optional): The title of the line chart. Default is None.

    Returns:
        plotly.graph_objs._figure.Figure: The created line chart figure.
    """
    try:
        fig = px.line(df, x=x, y=y, color=legend, title=title, color_discrete_sequence=colors)
        return fig
    except Exception as e:
        raise ValueError(f"An error occurred while creating the line chart: {e}")

def create_histogram(df, x, title=None):
    """
    Create a histogram using Plotly Express.

    Args:
        df (pd.DataFrame): The DataFrame containing the data to plot.
        x (str): The column name for the x-axis.
        title (str, optional): The title of the histogram. Default is None.

    Returns:
        plotly.graph_objs._figure.Figure: The created histogram figure.
    """
    try:
        fig = px.histogram(df, x=x, title=title, color_discrete_sequence=colors)
        return fig
    except Exception as e:
        raise ValueError(f"An error occurred while creating the histogram: {e}")
