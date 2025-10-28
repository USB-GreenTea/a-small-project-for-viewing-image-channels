import numpy as np
import matplotlib.pyplot as plt
from imageio import imread


kit = imread(r"path_to_path_to_image.png(or_jpg)")


fig, axs = plt.subplots(1, 5, figsize=(20, 5))


# Original image (4 channels)
axs[0].imshow(kit)
axs[0].set_title("Original")
axs[0].axis('off')


# Red channel
axs[1].imshow(kit[:, :, 0], cmap='Reds')
axs[1].set_title("Red channel")
axs[1].axis('off')


# Green channel
axs[2].imshow(kit[:, :, 1], cmap='Greens')
axs[2].set_title("Green channel")
axs[2].axis('off')


# Blue channel
axs[3].imshow(kit[:, :, 2], cmap='Blues')
axs[3].set_title("Blue channel")
axs[3].axis('off')


# Alpha (transparency)
if kit.shape[2] == 4:
    axs[4].imshow(kit[:, :, 3], cmap='Greys')
    axs[4].set_title("Alpha channel")
    axs[4].axis('off')
else:
    axs[4].axis('off')  # If alpha channel is missing, hide the axis


plt.show()
