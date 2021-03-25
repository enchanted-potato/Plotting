import numpy as np
import pandas as pd
import datetime
import os

import plotly.express as px
from plotly.offline import plot
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt

from plot import plotly_bar, plotly_histogram
from utilities import get_current_date

import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
stopwords = stopwords.words('english')
from wordcloud import WordCloud
from sklearn.feature_extraction.text import CountVectorizer

pd.set_option('display.max_columns', 70)

# READ DATA ============================================================================================================

data_path = 'C:/Users/KristiaKarakatsani/Projects/Plotting/datasets-master/datasets-master/1962_2006_walmart_store_openings.csv'
data = pd.read_csv(data_path)

# PLOT DIRECTORY =======================================================================================================

plots_dir = 'C:/Users/KristiaKarakatsani/Projects/Plotting/'
proc_dir = os.path.join(plots_dir, get_current_date())
if not os.path.exists(proc_dir):
    os.makedirs(proc_dir)

# PLOTS =====================================================================================================================

plotly_bar(data, 'type_store',
           'Number of stores per type',
           'Type of Store', 'Count',
            proc_dir + '\Type_of_store')

df = data.groupby(['STRSTATE', 'type_store']).size().reset_index().rename(columns={0:'Count'})
plotly_bar(df,
           xcol='type_store',
           ycol='Count',
           title='Types of stores per state',
           xtitle='Type of Store',
           ytitle='Count',
           filename= proc_dir + '\Type_of_store_per_state',
           splitby='STRSTATE',
           barmode='group')


df = data.groupby(['type_store', 'MONTH']).size().reset_index().rename(columns={0:'Count'})
plotly_bar(df,
           xcol='type_store',
           ycol='Count',
           title='Types of stores per state',
           xtitle=None,
           ytitle='Count',
           filename= proc_dir + '\Type_of_store_month',
           facetcol='MONTH',
           labels = {'type_store':''})


plotly_histogram(data,
                 xcol='county',
                 xname='County',
                 title='Distribution of Counties',
                 xaxis='Counties',
                 yaxis='Frequency',
                 filename= proc_dir + '\Counties',
                 marginal='box',
                 nbins=850)

plotly_histogram(data,
                 xcol='county',
                 xname='County',
                 title='Distribution of Counties and st',
                 xaxis='Counties',
                 yaxis='Frequency',
                 filename= proc_dir + '\Counties_st',
                 xcol2=data['st'],
                 name2='street',
                 secondary_y=True,
                 yrange2=[0,400],
                 opacity2=0.6)

def plotly_histogram(df, xcol, xname, title, xaxis, yaxis, filename, opacity=0.75,
                     marginal=None, color=['#273bd8'], log_y=False, log_x=False,
                     nbins=None, xcol2=None, name2=None, secondary_y=False, opacity2=None,
                     secondary_title=None, nbins2=None, yrange2=[0, 10]):