import pandas as pd
import matplotlib.pyplot as plt

file_path = 'D:\data.csv' 
data = pd.read_csv(file_path)

plt.figure(figsize=(10, 6))
for column in data.columns:
    plt.plot(data[column], label=column)
plt.title('Toate valorile')
plt.legend()
plt.show()

X=8
plt.figure(figsize=(10, 6))
for column in data.columns:
    plt.plot(data[column][:X], label=column)
plt.title(f'Primele {X} valori')
plt.legend()
plt.show()

Y=12
selected_data = data[['Durata', 'Puls']][-Y:]

plt.figure(figsize=(10, 6))
plt.plot(selected_data['Durata'], label='Durata')
plt.plot(selected_data['Puls'], label='Puls')
plt.title(f'Ultimele {Y} valori pentru Durata și Puls')
plt.legend()
plt.show()