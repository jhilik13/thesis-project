import os

img_folder='./brain mri/Task04_Hippocampus/imagesTr/' #brain image folder path
label_folder='./brain mri/Task04_Hippocampus/labelsTr/' #label folder path

filename='hippocampus_001.nii.gz' #file that will be worked on

scanPath=os.path.join(img_folder,filename) #joining folder and file name
labelPath=os.path.join(label_folder,filename) #joining label folder and file name

sliceno=20 #slice no that will be worekd on

import nibabel as nib

scanimg=nib.load(scanPath) #loading scan path variable
data1=scanimg.get_fdata() #getting data
img=data1[sliceno,:,:] #defining slice axis

scanlbl=nib.load(labelPath) #lodaing lable path 
data2=scanlbl.get_fdata() #getting label data
lbl=data2[sliceno,:,:] #slice axis

import matplotlib.pyplot as plt

plt.figure() #plotting figure
plt.subplot(1,2,1) #subplotting for showing result side by side
plt.imshow(img) #showing plot
plt.title("MRI scan")

plt.subplot(1,2,2) #for 2nd result
plt.imshow(lbl)
plt.title("Label")

plt.show()