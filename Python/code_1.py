from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
# from functions import randomValue
# # Datos de ejemplo
# arrList = []
# i=0
# while i<500:
#     arrList.append([randomValue(),randomValue()])
#     i+=1

X = np.array([
    [1, 2], [1.5, 1.8], [5, 8], 
    [8, 8], [1, 0.6], [9, 11],
    [2, 2.5], [1.2, 1.9], [4, 7], 
    [7, 7], [1.8, 1.2], [10, 12], 
    [6, 6], [3, 5], [6.5, 9], 
    [8.2, 7.5], [0.8, 1.4], [5.5, 7.5], 
    [7.8, 8.2], [9, 9.8], [4.5, 7.2], 
    [3.7, 6.3], [5.2, 8.3], [6, 5], 
    [8.5, 9], [7.1, 6.9], [2.8, 3.4],
    [1.3, 2.1], [6.1, 7.6], [9.5, 10],
    [3.1, 4.5], [2.6, 3.2], [6.8, 8.1],
    [7.9, 6.7], [4.4, 6.6], [8.1, 9.3],
    [2.2, 4.1], [5.7, 7.8], [4.8, 6.2],
    [9.3, 9.9], [5.4, 6.7], [1.1, 1.5],
    [3.9, 5.5], [2.4, 3.9], [6.9, 8.2],
    [7.5, 8.6], [9.2, 10.4], [5.1, 7.3],
    [8.8, 9.1], [1.7, 2.8], [4.3, 5.6],
    [9.7, 10.1], [6.2, 7.9], [3.3, 4.8],
    [8.4, 7.4], [7.2, 8.5], [4.9, 6.9],
    [5.6, 7.1], [8.9, 9.5], [6.4, 7.4],
    [9.4, 10.3], [3.8, 5.2], [5.3, 7.0],
    [7.7, 8.0], [2.9, 4.3], [9.6, 10.2],
    [6.6, 8.4], [8.7, 9.2], [5.8, 7.4],
    [9.1, 9.7], [2.3, 3.3], [3.6, 4.9],
    [7.3, 8.0], [8.3, 8.9], [4.7, 6.4],
    [5.9, 7.6], [6.3, 7.5], [7.4, 8.3],
    [9, 9.4], [2.7, 3.6], [8, 8.4],
    [4.6, 6.1], [3.4, 5.3], [7.6, 8.7],
    [9.8, 10.0], [2.5, 3.0], [8.6, 9.0],
    [6.7, 8.0], [1.9, 2.7], [7.0, 8.8]
])

# Crear modelo K-Means con 2 clusters
kmeans = KMeans(n_clusters=25, random_state=0)
kmeans.fit(X)

# Obtener las etiquetas (a qué grupo pertenece cada punto)
labels = kmeans.labels_

# Obtener las coordenadas de los centroides
centroids = kmeans.cluster_centers_

# Visualizar los clusters
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='rainbow')
plt.scatter(centroids[:, 0], centroids[:, 1], c='black', marker='x', s=200, label='Centroides')
plt.title("Clustering con K-Means")
plt.legend()
plt.show()