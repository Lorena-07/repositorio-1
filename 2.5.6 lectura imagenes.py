import numpy as np
from skimage import io
import matplotlib.pyplot as plt

photo = io.imread("golden.jpg")
print(type(photo))
print(photo.shape)

plt.imshow(photo)
plt.show()

plt.imshow(photo[::-1]) # [::-1] significa toma todo en esta dimencion pero alreves
plt.show()


plt.imshow(photo[:, ::-1]) #efecto espejo
plt.show()


plt.imshow(photo[:, :,::-1]) #significa cambiar de RGB a BGR
plt.show()

plt.imshow(photo[0:534, 0:500]) # recortar
plt.show()

plt.imshow(photo[::2, ::2]) # reducir a la mitad
print(photo[::2, ::2].shape)
plt.show()


photo_sin = np.round(np.abs(np.sin(photo) ),0)*260
print(photo_sin)

photo_msk = np.where(photo> 100, 255, 0)
plt.imshow(photo_msk)
plt.show()


plt.imshow(photo[:,:,2].T,cmap="jet")
plt.show()

