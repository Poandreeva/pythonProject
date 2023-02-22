import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import numpy as np


def move(x, a):
    moved_x = []
    for i in x:
        moved_x.append(i-a)
    return moved_x


def find_a(x, t):
    x_one = []
    for i in range(len(t[:1])):
        x_one.append(x[i])
    a = np.mean(x_one)
    return a


def integr(x):
    array = 0
    in_l = []
    for i in x:
        array += np.sum(i)
        in_l.append(array)
    return in_l


fs = 100
df = pd.read_excel('Accelerometer.xlsx')
x = df['X'].tolist()
y = df['Y'].tolist()
z = df['Z'].tolist()

t = []
for i in range(len(x)):
    t.append(i/fs)

a_x = find_a(x, t)
moved_x = move(x, a_x)
sp_x = integr(moved_x)

a_y = find_a(y, t)
moved_y = move(y, a_y)
sp_y = integr(moved_y)

a_z = find_a(z, t)
moved_z = move(z, a_z)
sp_z = integr(moved_z)


fig, axs = plt.subplots(3, figsize=(10, 10))
axs[0].plot(t, moved_x, linewidth=1, color='royalblue')
axs[1].plot(t, moved_y, linewidth=1, color='royalblue')
axs[2].plot(t, moved_z, linewidth=1, color='royalblue')
fig.suptitle('Укол одной рукой')
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
plt.savefig('Ускорение руки.png', dpi=100)
print('done 1')


fig, axs = plt.subplots(3, figsize=(10, 10))
axs[0].plot(t, sp_x, linewidth=1, color='royalblue')
axs[1].plot(t, sp_y, linewidth=1, color='royalblue')
axs[2].plot(t, sp_z, linewidth=1, color='royalblue')
fig.suptitle('Укол одной рукой')
axs[0].set_ylabel('Проекция скорости на ось Х')
axs[1].set_ylabel('Проекция скорости на ось Y')
axs[2].set_ylabel('Проекция скорости на ось Z')
for i in range(3):
    plt.axis()
    axs[i].set_xlabel('Время, с')
    axs[i].xaxis.set_major_locator(ticker.MultipleLocator(1))
    axs[i].grid(which='major',
                linewidth=0.5,
                linestyle=':',
                color='k')
fig.tight_layout()
plt.savefig('Скорость руки.png', dpi=100)
print('done 2')
