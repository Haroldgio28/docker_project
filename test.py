
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('StressLevelDataset.csv')
df.head()


print(df.describe())


# Calcula la matriz de correlación
correlation_matrix = round(df.corr(),2)

# Visualiza la matriz de correlación con seaborn
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Matriz de Correlación')
plt.show()


