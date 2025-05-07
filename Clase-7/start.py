import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Datos del ejemplo
data = {
    'Estudiante': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Asistencia': [90, 80, 95, 75, 85, 70, 95, 85, 75, 100],
    'Puntaje': [75, 60, 85, 55, 80, 50, 90, 82, 55, 95]
}

df = pd.DataFrame(data)

# Crear gráfico
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Asistencia', y='Puntaje', s=100, color='blue')
sns.regplot(data=df, x='Asistencia', y='Puntaje', scatter=False, color='red')  # Línea de tendencia
plt.title('Relación entre Nivel de Asistencia y Puntaje en Examen', fontweight='bold')
plt.xlabel('Nivel de Asistencia (%)')
plt.ylabel('Puntaje en Examen')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()