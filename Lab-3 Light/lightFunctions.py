import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as imageio
from cycler import cycler

photoName = 'red_spec.jpg'
plotName = 'red.png'
surface = 'Красный лист'
def readIntensity(photoName, plotName, lamp, surface):
    photo = imageio.imread(photoName)
    background = photo[896:1111, 664:1093, 0:3]

    cut = photo[896:1111, 664:1093, 0:3]
    rgb = np.mean(cut, axis=(0))
    luma = 0.2989 * rgb[:, 0] + 0.5866 * rgb[:, 1] + 0.1144 * rgb[:, 2]

    plt.rc('axes', prop_cycle=(cycler('color', ['r', 'g', 'b'])))

    fig = plt.figure(figsize=(10, 5), dpi=200)

    plt.title('Интенсивность отражённого излучения\n' + '{} / {}'.format(lamp, surface))
    plt.xlabel('Относительный номер пикселя')
    plt.ylabel('Яркость')

    plt.plot(rgb, label=['r', 'g', 'b'])
    plt.plot(luma, 'w', label='I')
    plt.legend()

    plt.imshow(background, origin='lower')
    plt.savefig(plotName)
    plt.show()

    return luma

readIntensity(photoName, plotName, 'Hg', surface)