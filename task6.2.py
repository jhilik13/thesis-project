import os

img_folder='./brain mri/Task04_Hippocampus/imagesTr/' #image folder path
label_folder='./brain mri/Task04_Hippocampus/labelsTr/' #label folder path 

filename='hippocampus_001.nii.gz' #file we will work on

scanPath=os.path.join(img_folder,filename) #joining image folder and file name
labelPath=os.path.join(label_folder,filename)  #joining label folder and file name

sliceno=20 

import nibabel as nib

scanimg=nib.load(scanPath) #loading scanpath into scanimg
data1=scanimg.get_fdata() #geeting the data from scanimg to data1
img=data1[sliceno,:,:] #slice into x asis

scanlbl=nib.load(labelPath)  #loading labelpath into scanlbl
data2=scanlbl.get_fdata() #getting data of label into data2
lbl=data2[sliceno,:,:] #slice of x axis

import h5py

h5file = h5py.File("task.h5","r") #reading into the h5 file we created
#h5file.create_dataset("image", img.shape)
img=h5file["image"][...]

#h5file = h5py.File("task.h5","w")
#h5file.create_dataset("label", lbl.shape)
lbl = h5file["label"][...]

h5file.close()

import matplotlib.pyplot as plt

plt.figure() #plotting figure
plt.subplot(1,2,1) #subplotting for showing result side by side
plt.imshow(img) #showing plot
plt.title("MRI scan")

plt.subplot(1,2,2) #for 2nd result
plt.imshow(lbl)
plt.title("Label")

plt.show()