#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 09:33:56 2017

@author: ubuntu
"""

import os
from shutil import copyfile

import glob
'''
def rename(dir=config.merged_dir,
           target='_manual1'):
    for fullpath in glob.glob(dir+'*'+target+'*'):
        os.rename(fullpath,fullpath.replace(target,''))
    
def chgname(selected=config.selected,
            tgt='_training',
            dst= ''):
    for fullpath in glob.glob(config.in_dir+'*.jpg'):
        newpath = fullpath.replace(config.in_dir_names[selected],
                                   config.merged_dir_names[selected])
        newpath = newpath.replace(tgt,dst)
        copyfile(fullpath,newpath)       
'''
def getcurrentdir():
    return os.path.dirname(os.path.abspath(__file__))

rootdir = getcurrentdir()
olddir = rootdir + "/" + "full" + "/"
newdir = rootdir + "/" + "renamed" + "/"

def mkdir(path=newdir):
    if not os.path.exists(path):
        os.mkdir(newdir,0755)    

def chgnameall(here=olddir,there=newdir):
    mkdir()
    for i,oldpath in enumerate(glob.glob(here+'*.jpg')):
        newpath = there+str(i)+".jpg"
        copyfile(oldpath,newpath)
def main():
    chgnameall()
    #rename()
if __name__ == '__main__':
    #print getcurrentdir()
    main()
            