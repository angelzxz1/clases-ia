from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import matplotlib.pyplot as plt

# Datos de entrenamiento: [peso, altura]
X = np.array([
    [60, 1.70], [65, 1.75], [70, 1.80],   # Clase 0 (por ejemplo: Deportistas)
    [80, 1.60], [85, 1.65], [90, 1.70],   # Clase 1 (por ejemplo: No deportistas)
    [55, 1.55], [58, 1.60], [53, 1.50]    # Clase 0 también
])

# Etiquetas de clase (0 o 1)
y = np.array([0, 0, 0, 1, 1, 1, 0, 0, 0])

# Crear el modelo KNN con K=3
modelo = KNeighborsClassifier(n_neighbors=4)

# Entrenar el modelo
modelo.fit(X, y)

# Nuevo dato para predecir
nuevo_dato = np.array([[75, 1.72]])

# Predecir clase
prediccion = modelo.predict(nuevo_dato)

print(f"La clase predicha para el nuevo dato es: {prediccion[0]}")

# Visualización
for i in range(len(y)):
    color = 'blue' if y[i] == 0 else 'red'
    plt.scatter(X[i, 0], X[i, 1], c=color, label=f'Clase {y[i]}' if i < 2 else "", s=100)

# Nuevo punto
plt.scatter(nuevo_dato[0, 0], nuevo_dato[0, 1], c='green', marker='x', s=200, label='Nuevo dato')

plt.xlabel('Peso (kg)')
plt.ylabel('Altura (m)')
plt.title('Clasificación con KNN (k=3)')
plt.legend()
plt.grid(True)
plt.show()