# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:30:11 2019

@author: masoudg
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 12:04:23 2019

@author: masoudg
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 17:34:07 2019

@author: masoudg
"""

# import some libraries
import os
import numpy as np
import mnist_reader

from PIL import Image as PImage        # python image libraray

from sklearn.decomposition import PCA  # PCA dimension reduction
from sklearn.manifold import TSNE      # T-NSE dimension reduction
import umap                            # UMAP for dimension reduction

# matplotlib for graphics.
import matplotlib.pyplot as plt
import matplotlib.patheffects as PathEffects

# seaborn to make nice plots.
import seaborn as sns
sns.set_style('darkgrid')
sns.set_palette('muted')
sns.set_context("notebook", font_scale=1.5,
                rc={"lines.linewidth": 2.5})

# set image directories
img_main_dir = '//ad.monash.edu/home/User098/masoudg/Desktop/faces/images'
result_path  = '//ad.monash.edu/home/User098/masoudg/Desktop/faces'


