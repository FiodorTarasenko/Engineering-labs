import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import imageio.v2 as imageio
from cycler import cycler


photoName = 'blue_spec.jpg'
plotName = 'Cal_blue.png'
surface = 'Синий лист'

o = []
with open(r'coefficients.txt') as f:
    for line in f:
        o.append(float(line))
k = o[0]
c = o[1]

def calib(x, pos):
    return int(x * k + c)
def readIntensity(photoName, plotName, lamp, surface):
    photo = imageio.imread(photoName)
    background = photo[896:1111, 664:1093, 0:3]

    cut = photo[896:1111, 664:1093, 0:3]
    rgb = np.mean(cut, axis=0)
    luma = 0.2989 * rgb[:, 0] + 0.5866 * rgb[:, 1] + 0.1144 * rgb[:, 2]

    plt.rc('axes', prop_cycle=(cycler('color', ['r', 'g', 'b'])))

    fig = plt.figure(figsize=(10, 5), dpi=200)
    ax = fig.add_subplot()

    plt.title('Интенсивность отражённого излучения\n' + '{} / {}'.format(lamp, surface))
    plt.xlabel('Длина волны [нм]')
    plt.ylabel('Яркость')
    plt.minorticks_on()
    plt.plot(rgb, label=['r', 'g', 'b'])
    plt.plot(luma, 'w', label='I')
    plt.legend()

    start, end = ax.get_xlim()
    ax.xaxis.set_ticks(((np.arange(((start * k + c) // 50 + 1) * 50, end * k + c, 50, dtype=int)) - c) / k)
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(calib))

    plt.imshow(background, origin='lower')
    plt.savefig(plotName)
    plt.show()

    return luma

readIntensity(photoName, plotName, 'Hg', surface)