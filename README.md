# Data Visualization Comparision for face images

This repo compares the representation of different face categories across layers of DCNN, from low pooling layers for fully connected layers to see when categories are clearly represented.

To this end, we use common visualization (or dimension redcution) methods including:
1. [**PCA: **](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)
2. [**t-SNE: **] Developed by [Laurens van der Maaten](http://lvdmaaten.github.io/) and [Geoffrey Hinton](http://www.cs.toronto.edu/~hinton/) (see the [original paper here](http://jmlr.csail.mit.edu/papers/volume9/vandermaaten08a/vandermaaten08a.pdf))
3. [**UMAP: **] The details for the underlying mathematics can be found [**here: **](https://arxiv.org/abs/1802.03426), and documentation is `available via ReadTheDocs <https://umap-learn.readthedocs.io/>`_. 
