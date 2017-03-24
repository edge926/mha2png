#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import skimage.io
import matplotlib.pyplot as plt
import os
import argparse


def mha2png(file_path, dest_dir, slices=None):
    ''' 
        @convert .mha file to .png files
        @parm:file_path: path to .mha file
              dest_dir: directory to store .png file
              slices: [m n]
    '''

    img = skimage.io.imread(fname=file_path, plugin='simpleitk')

    if slices == None:
        slice_min = 0
        slice_max = img.shape[0]
    else:
        slice_min = slices[0]
        slice_max = slices[1]

    filename = file_path.split('/')[-1].split('.')[-2]
    for slicer in range(slice_min,slice_max):
        plt.imsave(dest_dir + '/' + filename+ '_' + str(slicer) + '.png', img[slicer], cmap='gray',format='png')



if __name__=='__main__':
   
    parser = argparse.ArgumentParser(prog='mha2png')
    parser.add_argument('mha_files_dir', type=str, help='directory contains .mha files')
    parser.add_argument('-s','--slices', metavar = ('m','n'), type=int, nargs=2, help='specify the numbers of slices')

    output_file = 'output'
    os.mkdir(output_file)

    args = parser.parse_args()
    #find all .mha files
    for root, dirs, files in os.walk(args.mha_files_dir):
        for filename in files:
            f_rootext = os.path.splitext(filename)
            
            if f_rootext[1] == '.mha':
                
                os.mkdir(output_file +'/' + f_rootext[0])
                mha2png(os.path.join(root,filename), output_file + '/' + f_rootext[0], args.slices)


