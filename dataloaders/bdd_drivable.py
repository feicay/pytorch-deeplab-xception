import os
import sys
sys.path.append(os.getcwd())
import torch
import numpy as np
from PIL import Image
from torch.utils import data
from mypath import Path

class bdd_drivable_map(data.Dataset):
    def __init__(self, root=Path.db_root_dir('bdd_drivable'), split="train", transform=None):
        self.root = root
        self.transform = transform
        self.split = split
        self.imagedir = root + '/images/100k/' + self.split
        self.labeldir = root + '/drivable_maps/labels/' + self.split
        self.ignore_index = 255
        self.class_names = ['unlabelled', 'directly,', 'alternatively']
        image_list = os.listdir(self.imagedir)
        print('dataset ' + split + ': %d images'%(len(image_list)))
        self.image_list = []
        self.label_list = []
        for i in range(len(image_list)):
            name = image_list[i].split('.')[0]
            label_name = name + '_drivable_id.png'
            self.image_list.append(self.imagedir + '/' + image_list[i])
            self.label_list.append(self.labeldir + '/' + label_name)
            
    def __len__(self):
        return len(self.image_list)
    
    def __getitem__(self, index):
        image_path = self.image_list[index]
        label_path = self.label_list[index]
        img = Image.open(image_path).convert('RGB')
        target = Image.open(label_path)
        sample = {'image': img, 'label': target}

        if self.transform:
            sample = self.transform(sample)
        return sample


if __name__ == '__main__':
    bdd_drivable_map()