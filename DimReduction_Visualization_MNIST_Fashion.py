# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:30:11 2019

@author: masoudg
"""

# import some libraries
import numpy as np
import time
from utils import mnist_reader  # you need to clone from here: https://github.com/zalandoresearch/fashion-mnist

from sklearn.decomposition import PCA  # PCA dimension reduction
from sklearn.manifold import TSNE      # T-NSE dimension reduction
import umap                            # UMAP for dimension reduction, clone from: https://github.com/lmcinnes/umap

# matplotlib for graphics.
import matplotlib.pyplot as plt
import matplotlib.patheffects as PathEffects

# seaborn to make nice plots.
import seaborn as sns
sns.set_style('darkgrid')
sns.set_palette('muted')
sns.set_context("notebook", font_scale=1.5,
                rc={"lines.linewidth": 2.5})

# set directories
result_path  = '../..'

  
def scatter(x, colors, ax, titl):
    # a function for plotting scatter plots
    # We choose a color palette with seaborn.
    palette = np.array(sns.color_palette("hls", 10))

    # We create a scatter plot.
    sc = ax.scatter(x[:,0], x[:,1], lw=0, s=40,
                    c=palette[colors.astype(np.int)])
    plt.xlim(-25, 25)
    plt.ylim(-25, 25)
    plt.title(titl)
    ax.axis('off')
    ax.axis('tight')
    
    # We add the labels for each class.
    txts = []
    for i in range(10):  # loop over all 10 classes
        # Position of each label.
        xtext, ytext = np.median(x[colors == i, :], axis=0)
        txt = ax.text(xtext, ytext, "FC " + str(i+1), fontsize=24)
        txt.set_path_effects([
            PathEffects.Stroke(linewidth=5, foreground="w"),
            PathEffects.Normal()])
        txts.append(txt)

    return ax, sc, txts


# calculate dimension reduction
X_train, y_train = mnist_reader.load_mnist('data/fashion', kind='train')  # load the data, only train is enough
num_dimension    = 2  # we need 2 dimensions, should be enough

X          = np.array(X_train)/ 255.0 # data
y          = np.array(y_train)        # labels

print("Starting PCA...")
start_time = time.time()
y_pca      = PCA(n_components=num_dimension).fit_transform(X)                            # apply PCD
print(f"PCA is done! Epalsed time {time.time() - start_time} sec")

print("Starting TSNE...")
start_time = time.time()
y_tsne     = TSNE(n_components=num_dimension).fit_transform(X)                           # apply t-SNE
print(f"TSNE is done! Epalsed time {time.time() - start_time} sec")

print("Starting UMAP")
start_time = time.time()
y_umap     = umap.UMAP(n_neighbors=3, min_dist=0.3, metric='correlation').fit_transform(X)  # apply Umap
print(f"UMAP is done! Epalsed time {time.time() - start_time} sec")

# visualization
fig, ax    = plt.subplots(nrows=1, ncols=3, sharex='col', sharey='row', figsize=(20, 7))
ax         = plt.subplot(1, 3, 1, aspect='equal')
scatter(y_pca, y, ax, "PCA")


ax         = plt.subplot(1, 3, 2, aspect='equal')
scatter(y_tsne, y, ax, "t-SNE ")

ax         = plt.subplot(1, 3, 3, aspect='equal')
scatter(y_umap, y, ax, "Umap")

# save the image
plt.savefig(result_path + "/"  + "MNIST_Fashion_visualization", dpi=300)