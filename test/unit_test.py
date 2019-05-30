# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 16:08:32 2016

@author: Alan
"""
import nibabel as nib
import numpy as np
import Unwrap3d
from subprocess import call

all(['bash', 'run_before_unit_test.bash'])
good_result = np.load('unwrapped_result.npy')

img = nib.load('test_img.nii.gz').get_data()
mask=nib.load('test_img_mask.nii.gz').get_data()

img=np.asfortranarray(img,'float32')
mask=np.asfortranarray(mask,'bool')
result = Unwrap3d.unwrap3d(img,mask)
assert (result==good_result).all() 'algorithm failed with fortran style array'


img = np.ascontiguousarray(img,'float32')
mask=np.ascontiguousarray(mask,'bool')
result = Unwrap3d.unwrap3d(img,mask)
assert (result==good_result).all() 'algorithm failed with c style array'

#from vidi3d import compare3d
#compare3d((img,result))




