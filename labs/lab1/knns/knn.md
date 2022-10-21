# Part 1: k Nearest Neighbors (kNNs)

In this part of the lab, you will get familiar with the practical use of the k nearest neighbor algorithm (kNN). 

kNN is considered a non-parametric method given that it makes few assumptions about the form of the data distribution. This approach is *memory-based* as it requires no model to be fit. Nearest-neighbor methods use the observations from the training set closest in input space to $x$ to form $\hat{y}$. It is based on the assumption that if a sample's features are similar to the ones of points of one particular class then it belongs to that class. These points are known as nearest neighbors.

The specific case where $k=1$ is denoted the nearest neighbor algorithm. Here $\hat{y}$ is assigned the value $y_{l}$ of the closest point $x_{l}$ to $x$ in the training data. This corresponds to a *Voronoi tessellation* of the training data. 

### Learning goals

After running this notebook, you should be able to:

1. Have a better understanding of the mechanisms behind the k nearest neighbor algorithm
2. Be aware of the problems associated with the curse of dimensionality

### Algorithm (Classification)
Given a query point $\mathbf{x}_0$ and a training set $\mathcal{D}=(\mathbf{x}_i, y_i)$, $i = 1,..., N$:<br>
1- Compute the distance $d(\mathbf{x}_0, \mathbf{x}_i)$ between $\mathbf{x}_0$ and all $\mathbf{x}_i \in \mathcal{D}$.<br>
2- Sort all $ \mathbf{x}_i$ using $d(\mathbf{x}_0, \mathbf{x}_i)$ as sorting criterion. Sort for increasing distance<br>
3- Select the first $k$ points. This points are denoted the k-neighborhoods of $\mathbf{x}_0,\, \mathcal{S}_k(\mathbf{x}_0)$. <br>
4- Assign $\hat{y}$ based on majority voting:
\begin{equation}
\hat{y} = h(\mathbf{x}_0) = \arg\max_{y} \sum_{\mathbf{x}_i \in \mathcal{S}_{\mathbf{x}_0}} I(y = y_i)
\end{equation}

### Hands-On
Open the [k-Nearest Neighbors Jupyter notebook](./knn.ipynb) and start working on the required tasks.


