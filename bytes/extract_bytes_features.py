
# import library
import os
import shutil
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import csv
import random as r
import multiprocess
import codecs
from multiprocess import Process

# path to the directory
path = 'C:\\Users\\Vipul Singh\\Desktop\\train (1)\\train'
dist_bytes = 'C:\\Users\\Vipul Singh\\Desktop\\train (1)\\bytes'
dist_asm = 'C:\\Users\\Vipul Singh\\Desktop\\train (1)\\asm'

# make bytes and asm folder 
os.mkdir(dist_bytes, mode=511)
os.mkdir(dist_asm, mode=511)


# fuction to seperate perticular extention file.
def file_seperator(ext, source_path, dist_path):
    '''move all the files having extension <ext> from the source directory to the dist_path'''
    for f_name in os.listdir(source_path):
        if f_name.endswith(ext):
            file_path = source_path + '\\' + f_name
            shutil.move(file_path,dist_path)


# seperating .byter and .asm files
file_seperator('.bytes',path, dist_bytes)
file_seperator('asm',path, dist_asm)

# load trainLabels
Y = pd.read_csv('C:\\Users\\Vipul Singh\\Desktop\\train (1)\\trainLabels.csv')

def generate_size_data(Y, path):
    Y = Y.set_index('Id')
    file_size = []
    file_name = []
    classes = []
    for f in os.listdir(path):
        name = f.split('.')[0]
        size = os.path.getsize(path + '\\' + f)
        c = Y.to_dict()['Class'][name]
        file_name.append(name)
        file_size.append(size)
        classes.append(c)
    return file_name, file_size, classes

# generate size data for bytes file
file_name, file_size, classes = generate_size_data(Y, dist_bytes)
df_size_bytes = pd.DataFrame({'ID': file_name , 'size_bytes' : file_size, 'Class': classes})


bytes = pd.read_csv('C:\\Users\\Vipul Singh\\Desktop\\train (1)\\result.csv')
bytes = bytes.drop('ID', axis = 1)

# concate features and size data
data = pd.concat([bytes, df_size_bytes], axis = 1)

#Reorder columns
df = data.reindex(columns=['ID', '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '0a', '0b', '0c', '0d', '0e', '0f', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '1a', '1b', '1c', '1d', '1e', '1f', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '2a', '2b', '2c', '2d', '2e', '2f', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '3a', '3b', '3c', '3d', '3e', '3f', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '4a', '4b', '4c', '4d', '4e', '4f', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '5a', '5b', '5c', '5d', '5e', '5f', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '6a', '6b', '6c', '6d', '6e', '6f', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '7a', '7b', '7c', '7d', '7e', '7f', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '8a', '8b', '8c', '8d', '8e', '8f', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '9a', '9b', '9c', '9d', '9e', '9f', 'a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'aa', 'ab', 'ac', 'ad', 'ae', 'af', 'b0', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'ba', 'bb', 'bc', 'bd', 'be', 'bf', 'c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'ca', 'cb', 'cc', 'cd', 'ce', 'cf', 'd0', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'da', 'db', 'dc', 'dd', 'de', 'df', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'ea', 'eb', 'ec', 'ed', 'ee', 'ef', 'f0', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'fa', 'fb', 'fc', 'fd', 'fe', 'ff', '??', 'size_bytes', 'Class'])

df.to_csv('C:\\Users\\Vipul Singh\\Desktop\\train (1)\\Bytes.csv', index=False)

