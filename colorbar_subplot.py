#https://stackoverflow.com/questions/13784201/how-to-have-one-colorbar-for-all-subplots

import numpy as np
from matplotlib.colors import Normalize
import matplotlib.pyplot as plt
import matplotlib.cm as cm
fig, axes = plt.subplots(nrows=2, ncols=2)
cmap=cm.get_cmap('viridis')
normalizer=Normalize(0,4)
im=cm.ScalarMappable(norm=normalizer)
for i,ax in enumerate(axes.flat):
    ax.imshow(i+np.random.random((10,10)),cmap=cmap,norm=normalizer)
    ax.set_title(str(i))
fig.colorbar(im, ax=axes.ravel().tolist())
plt.show()
