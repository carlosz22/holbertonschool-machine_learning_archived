#!/usr/bin/env python3
"""3D Scatter plot"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
 
data = np.load("data.npy")
labels = np.load("labels.npy")

data_means = np.mean(data, axis=0)
norm_data = data - data_means
_, _, Vh = np.linalg.svd(norm_data)
pca_data = np.matmul(norm_data, Vh[:3].T)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
cmplasma = plt.get_cmap("plasma")
colors={0: 'red', 1: 'green', 2: 'blue'}

for i in range(len(pca_data)):
    ax.scatter(pca_data[i, 0], pca_data[i, 1],
     pca_data[i, 2], label=labels[i], c=colors.get(labels[i], 'white'),
      cmap=cmplasma)

plt.title('PCA of Iris Dataset')
plt.show()
