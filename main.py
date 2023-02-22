import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd

fs = 100
df = pd.read_excel('Accelerometer.xlsx')
x = df['X'].tolist()
y = df['Y'].tolist()
z = df['Z'].tolist()

t = []
for i in range(len(x)):
    t.append(i/fs)

fig, axs = plt.subplots(3, figsize=(10, 10))
axs[0].plot(t, x, linewidth=1, color='royalblue')
axs[1].plot(t, y, linewidth=1, color='royalblue')
axs[2].plot(t, z, linewidth=1, color='royalblue')
fig.suptitle('Выпрямление руки')
axs[0].set_ylabel('Проекция ускорения на ось Х')
axs[1].set_ylabel('Проекция ускорения на ось Y')
axs[2].set_ylabel('Проекция ускорения на ось Z')
for i in range(3):
    plt.axis()
    axs[i].set_xlabel('Время, с')
    axs[i].xaxis.set_major_locator(ticker.MultipleLocator(1))
    axs[i].grid(which='major',
                linewidth=0.5,
                linestyle=':',
                color='k')
fig.tight_layout()
plt.savefig('Выпрямление руки.png', dpi=100)
print('done 1')
