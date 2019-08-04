# -*- coding: utf-8 -*-
#import libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def missing_values(data, cmap = 'viridis'):
    """
    Given the data, this function will return a graph for missing values
    
    Parameters
    ----------
    data : Pandas dataframe.
    cmap : matplotlib colormap name or object, or list of colors, optional
    The mapping from data values to color space. If not provided, the
    default is 'viridis'.
    
    """
    return sns.heatmap(data.isnull(),yticklabels=False,cbar=False,cmap='viridis')

