import numpy as np
import datetime

import matplotlib.pyplot as plt

import plotly.express as px
from plotly.offline import plot
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def plotly_bar(df, xcol, title, xtitle, ytitle, filename, ycol=None,
               color='#273bd8', barmode=None, splitby=None, facetrow=None, facetcol=None, updates=None, labels=None):
    '''
    Plot a bar chart using plotly and save.
    Paramet
    ----------
    df : pandas.DataFrame
        Pandas dataframe.
    xcol : str
        Name of the column to plot on x axis.
    title : str
        Plot title.
    xtitle : str
        x axis title.
    ytitle : str
        y axis title.
    filename : str
        Path and name of the file to save.
    ycol : str, optional
        Optional column to plot on y axis. The default is None.
    color : str, optional
        Colour of the bars. The default is #01295C.
    barmode : str, optional
        Type of bars to plot such as 'group'. The default is None.
    splitby: str, optional
        Column to split bars by. The default is None.
    facetrow : str, optional
        Name of column to facet on rows. The default is None.
    facetcol : str, optional
        Name of column to facet on columns. The default is None.
    labels: dict, optional
        Rename columns to be plotted. Keys are existing col names, values are new names.
    Returns
    -------
    None.
    '''

    if ycol is None:
        feature_count = df[xcol].value_counts(dropna=False).reset_index().rename(
            columns={"index": "value", xcol: "count"})

        fig = make_subplots()

        fig.add_trace(go.Bar(
            x=feature_count["value"],
            y=feature_count["count"],
            name=xcol,
            marker_color=color,
            opacity=0.8))

    else:
        fig = px.bar(df, x=xcol, y=ycol, color=splitby, barmode=barmode,
                     facet_row=facetrow, facet_col=facetcol, labels=labels)

        # Use date string to set xaxis range
    fig.update_layout(title_text=title,
                      xaxis_title=xtitle,
                      yaxis_title=ytitle)

    fig.update_layout(updates)

    plot(fig, filename=(filename + "_BAR.html"), auto_open=False)


def plotly_histogram(df, xcol, xname, title, xaxis, yaxis, filename, opacity=0.75,
                     marginal=None, color=['#273bd8'], log_y=False, log_x=False,
                     nbins=None, xcol2=None, name2=None, secondary_y=False, opacity2=None,
                     secondary_title=None, nbins2=None, yrange2=[0, 10]):
    '''
    Plots a histogram using plotly for numerical variables and saves it.
    Parameters
    ----------
    df : pandas.DataFrame
        Pandas dataframe.
    xcol : str
        Name of cloumn to plot on x axis.
    xname : str
        Name corresponding to xcol given to legend.
    title : str
        Plot title.
    xaxis : str
        x axis title.
    yaxis : str
        y axis title.
    filename : str
        Path and name of the file to save.
    opacity : float, optional
        Controls the transparency of the points with 0 being transparent
        and 1 being solid. The default is 0.75.
    marginal : str, optional
        marginal="box" returns a boxplot on top of the histogram. The default is None.
    color : str, optional
        Colour of histogram. The default is ['#01295C'].
    log_y : bool, optional
        Optional flag to use log scale on y axis. The default is False.
    log_x : bool, optional
        Optional flag to use log scale on x axis. The default is False.
    nbins : int, optional
        The number of bins to plot. The default is None.
    xcol2 : str, optional
        Name of 2nd column to plot on x axis. The default is None.
    name2 : str, optional
        Name corresponding to xcol2 given to legend. The default is None.
    secondary_y : bool, optional
        Flag whether or not to include a secondary y axis. The default is False.
    opacity2 : float, optional
        Controls the transparency of the secondary points with 0 being transparent
        and 1 being solid. The default is None.
    secondary_title : str, optional
        Secondary y axis title. The default is None.
    nbins2 : int, optional
        Number of bins for secondary histogram. The default is None.
    yrange2 : list, optional
        The range of values to show on secondary y axis. The default is [0,10].
    Returns
    -------
    None.
    '''

    if marginal is not None:

        fig = px.histogram(df,
                           x=xcol,
                           marginal=marginal,
                           log_y=log_y,
                           log_x=log_x,
                           title=title,
                           color_discrete_sequence=color,
                           nbins=nbins,
                           opacity=opacity)
    else:
        fig = make_subplots(specs=[[{"secondary_y": secondary_y}]])

        fig.add_trace(go.Histogram(
            x=df[xcol],
            name=xname,
            marker_color=color,
            nbinsx=nbins,
            opacity=opacity))

        if secondary_y == True:
            fig.add_trace(go.Histogram(x=xcol2,
                                       name=name2,
                                       marker_color=None,
                                       opacity=opacity2,
                                       nbinsx=nbins2), secondary_y=True)

            fig.update_yaxes(title_text=secondary_title, secondary_y=True)
            fig.update_yaxes(range=yrange2, secondary_y=True)
            fig.update_yaxes(showgrid=False, secondary_y=True)

    fig.data[0].marker.line.width = 0.5

    fig.update_layout(title_text=title,
                      xaxis_title=xaxis,
                      yaxis_title=yaxis)
    plot(fig, filename=(filename + "_HIST.html"), auto_open=False)


def plotly_multiple_lines(df, xcol, ycol1, ycol2, yname1, yname2, \
                          title, xtitle, ytitle, filename, ycol3=None, yname3=None, \
                          xaxis_reversed=False, xaxis_rangeslider_visible=True):
    '''
    Plot a line graph with multiple lines using plotly and save.
    Parameters
    ----------
    df : pandas.DataFrame
        Pandas dataframe.
    xcol : str
        Name of the column to plot on x axis.
    ycol1 : str
        Name of the first column to plot on y axis.
    ycol2 : str
        Name of the second column to plot on y axis.
    yname1 : str
        Name corresponding to ycol1 to give to legend.
    yname2 : str
        Name corresponding to ycol2 to give to legend.
    title : str
        Plot title.
    xtitle : str
        x axis title.
    ytitle : str
        y axis title.
    filename : str
        Path and name of the file to save.
    ycol3 : str, optional
        Name of the third column to plot on y axis. The default is None.
    yname3 : str, optional
        Name corresponding to ycol3 to give to legend. The default is None.
    xaxis_reversed : bool, optional
        Flag to decide whether or not to reverse the x axis. The default is False.
    xaxis_rangeslider_visible : bool, optional
        Flag to decide whether or not to include an x axis slider. The default is True.
    Returns
    -------
    None.
    '''

    fig = make_subplots()

    fig.add_trace(go.Scatter(
        x=df[xcol],
        y=df[ycol1],
        name=yname1,
        line_color='#01295C',
        opacity=0.8))

    fig.add_trace(go.Scatter(
        x=df[xcol],
        y=df[ycol2],
        name=yname2,
        line_color='#EB2226',
        opacity=0.8))
    if ycol3 is not None:
        fig.add_trace(go.Scatter(
            x=df[xcol],
            y=df[ycol3],
            name=yname3,
            line_color='#777777',
            opacity=0.8))
    # Use date string to set xaxis range
    fig.update_layout(title_text=title,
                      xaxis_title=xtitle,
                      yaxis_title=ytitle,
                      xaxis_rangeslider_visible=xaxis_rangeslider_visible)

    if xaxis_reversed == True:
        fig.update_xaxes(autorange="reversed")

    plot(fig, filename=(filename + ".html"), auto_open=False)