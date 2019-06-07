# Data Visualization Comparision for face images

This repo compares the representation of different face categories across layers of DCNN, from low pooling layers for fully connected layers to see when categories are clearly represented.

To this end, I used common visualization (or dimension reduction) methods including:
1. [**PCA:**](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)
2. [**t-SNE:**](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html) Developed by [Laurens van der Maaten](http://lvdmaaten.github.io/) and [Geoffrey Hinton](http://www.cs.toronto.edu/~hinton/) (see the [original paper here](http://jmlr.csail.mit.edu/papers/volume9/vandermaaten08a/vandermaaten08a.pdf))
3. [**UMAP:**](https://github.com/lmcinnes/umap) The details for the underlying mathematics can be found [**here:**](https://arxiv.org/abs/1802.03426), and documentation is `available via ReadTheDocs <https://umap-learn.readthedocs.io/>`_. 

To start with, we first compare the performance of these three methods on [**MNIST-Fashion**](https://github.com/zalandoresearch/fashion-mnist):

(MNIST_Fashion_visualization.png)
