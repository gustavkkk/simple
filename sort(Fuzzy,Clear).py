# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 05:00:54 2017

@author: Frank
"""

import os
import glob

classes=['Fuzzy','Clear']

ch2en={
       '模糊':classes[0]
       }

root_dir = os.path.dirname(os.path.abspath(__file__)) + "\\"
src_root_dir = root_dir + 'DB\\Src\\分公司微信平台案例照片'
dst_root_dir = root_dir + 'DB\\Dst'

def mkdir(dirname):
    if not os.path.exists(dirname):
        os.mkdir(dirname)

def init():
    mkdir(dst_root_dir)
    for dirname in classes:
        mkdir(dst_root_dir + '\\' + dirname)
    
def sort():
    
    fuzzy_count = 0
    clear_count = 0
    ## process "fuzzy"-tag images
    for key in ch2en.keys():
        for fullpath in glob.iglob(src_root_dir + '\\**\\' + '*' + key + '*.jpg', recursive=True):
            #print(fullpath)
            newpath = dst_root_dir+'\\'+ch2en[key] + '\\'
            if ch2en[key] == classes[0]:
                fuzzy_count += 1
                while os.path.exists(newpath + str(fuzzy_count) + '.jpg'):
                    fuzzy_count += 1
                newpath += str(fuzzy_count) + '.jpg'
                os.rename(fullpath,newpath)
    ## process other images        
    for fullpath in glob.iglob(src_root_dir + '\\**\\*.jpg', recursive=True):
        clear_count += 1
        newpath = dst_root_dir + '\\' + classes[1] + '\\' + str(clear_count) + '.jpg'
        os.rename(fullpath,newpath)
        
if __name__ == '__main__':
    init()
    sort()
                
    