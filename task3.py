import nibabel as nib
import numpy as np

filepath= 'hippocampus_001.nii.gz'  #filepath
img=nib.load(filepath)  #laoding image
data=img.get_fdata()  #getting image data

slice1=data[0,:,:]   #axis wise slices
slice2=data[:,0,:]
slice3=data[:,:,0]

import matplotlib.pyplot as plt

plt.imshow(slice1) #plotting the image and showing axis wise
plt.show()
plt.imshow(slice2)
plt.show()
plt.imshow(slice3)
plt.show()

