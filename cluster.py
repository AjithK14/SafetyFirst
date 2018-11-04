import numpy as np
from sklearn.cluster import KMeans
arr=np.empty((0,2),float)
arr=np.append(arr,np.array([[3.0,5.0]]),axis=0)
arr=np.append(arr,np.array([[3.0,5.0]]),axis=0)
print(arr)
X = np.array([[1, 2],
              [1.5, 1.8],
              [5, 8],
              [8, 8],
              [1, 0.6],
              [9, 11]])
print(X)
clf = KMeans(n_clusters=2)
clf.fit(X)
centroids = clf.cluster_centers_
print(centroids)