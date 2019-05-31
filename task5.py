import nibabel as nib
import numpy as np
import glob
import pandas as pd

img_fldr='./brain mri/Task04_Hippocampus/imagesTr/'
files=glob.glob(img_fldr + "*.gz")

datas=[]

for filePath in files:
    img=nib.load(filePath)
    data=img.get_fdata()
    #print("Data shape:"+str(data.shape))
    datas.append(data.shape)
    
df=pd.DataFrame(datas,columns=['Xsize','Ysize','Zsize'])
df.describe()
print(df.describe)