import os
import numpy as np
import nibabel as nib

scans = "./brai mri/Task04_Hippocampus/imagesTr" #for giving scans the data
dirs = os.listdir( scans ) #creating directory

for file in dirs:
    image_path = os.path.join(scans, file)
    img=nib.load(image_path)
    data=img.get_fdata()
    print("Image info:"+str(dirs))
    print("Data shape:"+str(data.shape))
    print("Maximum voxel value:"+str(np.amax(data)))
    print("Minimum voxel value:"+str(np.amin(data)))
