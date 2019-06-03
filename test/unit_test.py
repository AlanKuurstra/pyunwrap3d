# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 16:08:32 2016

@author: Alan
"""
#make the module and install it in the test directory
from distutils.core import run_setup
import os
import glob
from shutil import copyfile

old_dir = os.getcwd()
os.chdir('..')
run_setup('setup.py',script_args=['build'])
lib_file = os.path.abspath(glob.glob('build/*lib*/Unwrap3d*')[0])
os.chdir(old_dir)
copyfile(lib_file,os.path.basename(lib_file))

import Unwrap3d
import os
import nibabel as nib
import numpy as np

fdir=os.path.dirname(__file__)
good_result = np.load(os.path.join(fdir,'unwrapped_result.npy'))

img = nib.load(os.path.join(fdir,'test_img.nii.gz')).get_data()
mask=nib.load(os.path.join(fdir,'test_img_mask.nii.gz')).get_data()

img=np.asfortranarray(img,'float32')
mask=np.asfortranarray(mask,'bool')
result = Unwrap3d.unwrap3d(img,mask)
assert (result==good_result).all(), 'algorithm failed with fortran style array'


img = np.ascontiguousarray(img,'float32')
mask=np.ascontiguousarray(mask,'bool')
result = Unwrap3d.unwrap3d(img,mask)
assert (result==good_result).all(), 'algorithm failed with c style array'

#from vidi3d import compare3d
#compare3d((img,result))




