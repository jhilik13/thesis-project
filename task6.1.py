import os

img_folder='./brain mri/Task04_Hippocampus/imagesTr/' 
label_folder='./brain mri/Task04_Hippocampus/labelsTr/' 

filename='hippocampus_001.nii.gz' 

scanPath=os.path.join(img_folder,filename) 
labelPath=os.path.join(label_folder,filename) 

sliceno=20 

import nibabel as nib

scanimg=nib.load(scanPath) 
data1=scanimg.get_fdata() 
img=data1[sliceno,:,:] 

scanlbl=nib.load(labelPath)  
data2=scanlbl.get_fdata() 
lbl=data2[sliceno,:,:] 

import h5py

h5file = h5py.File("task.h5","w")
h5file.create_dataset("image", img.shape)
h5file["image"][...] = img

#h5file = h5py.File("task.h5","w")
h5file.create_dataset("label", lbl.shape)
h5file["label"][...] = lbl

h5file.close()

