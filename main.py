import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import numpy as np


def move(x, a):
    moved_x = []
    for i in x:
        moved_x.append(i - a)
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
        array += i
        in_l.append(array)
    return in_l


l = [1, 2, 3, 4, 3, 2, 1, 0, -1, -2]
print(integr(l))

# TEST
test = pd.read_excel('Hyro_TEST.xlsx')
hyro_x = test['X'].tolist()
hyro_y = test['Y'].tolist()
hyro_z = test['Z'].tolist()

t_test = []
for i in range(len(hyro_x)):
    t_test.append(i)

sp_test_x = integr(hyro_x)
sp_test_y = integr(hyro_y)
sp_test_z = integr(hyro_z)

fig, axs = plt.subplots(2, 3, figsize=(40, 10))
axs[0, 0].plot(t_test, hyro_x, linewidth=1, color='royalblue')
axs[0, 1].plot(t_test, hyro_y, linewidth=1, color='royalblue')
axs[0, 2].plot(t_test, hyro_z, linewidth=1, color='royalblue')
axs[1, 0].plot(t_test, sp_test_x, linewidth=1, color='royalblue')
axs[1, 1].plot(t_test, sp_test_y, linewidth=1, color='royalblue')
axs[1, 2].plot(t_test, sp_test_z, linewidth=1, color='royalblue')
fig.suptitle('Test')
axs[0, 0].set_ylabel('Проекция углового ускорения на ось Х')
axs[0, 1].set_ylabel('Проекция углового ускорения на ось Y')
axs[0, 2].set_ylabel('Проекция углового ускорения на ось Z')
axs[1, 0].set_ylabel('Проекция угловой скорости на ось Х')
axs[1, 1].set_ylabel('Проекция угловой скорости на ось Y')
axs[1, 2].set_ylabel('Проекция угловой скорости на ось Z')
for i in range(2):
    for j in range(3):
        plt.axis()
        axs[i, j].xaxis.set_major_locator(ticker.MultipleLocator(100))
        axs[i, j].grid(which='major',
                       linewidth=0.5,
                       linestyle=':',
                       color='k')
fig.tight_layout()
plt.savefig('TEST.png', dpi=100)
print('done 0')
# TEST



fs = 100
df = pd.read_excel('Accelerometer.xlsx')
x = df['X'].tolist()
y = df['Y'].tolist()
z = df['Z'].tolist()

t = []
for i in range(len(x)):
    t.append(i / fs)

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
