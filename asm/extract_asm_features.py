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

# generate size data for asm files
file_name, file_size, classes = generate_size_data(Y, dist_asm)
df_size_asm = pd.DataFrame({'ID': file_name , 'size_asm' : file_size, 'Class': classes})


# Since the size of all the asm files are large so to reduce the time of preprocessing we will 
# distribute the files into 5 parts and use multiprocessing to process all the folders simultaneously.

folder_1 ='first'
folder_2 ='second'
folder_3 ='third'
folder_4 ='fourth'
folder_5 ='fifth'
folder_6 = 'output'


# creating 5 folders  
os.mkdir('C:\\Users\\Vipul Singh\\Desktop\\train (1)\\asm_distributed\\'+folder_1)
os.mkdir('C:\\Users\\Vipul Singh\\Desktop\\train (1)\\asm_distributed\\'+folder_2)
os.mkdir('C:\\Users\\Vipul Singh\\Desktop\\train (1)\\asm_distributed\\'+folder_3)
os.mkdir('C:\\Users\\Vipul Singh\\Desktop\\train (1)\\asm_distributed\\'+folder_4)
os.mkdir('C:\\Users\\Vipul Singh\\Desktop\\train (1)\\asm_distributed\\'+folder_5)


asm_distributed ='C:\\Users\\Vipul Singh\\Desktop\\train (1)\\asm_distributed\\'
source = 'C:\\Users\\Vipul Singh\\Desktop\\train (1)\\asm\\'

# moving the files randomly to the five folders

files = os.listdir(dist_asm)
data=list(range(0,10868))
r.shuffle(data)
count=0
for i in range(0,10868):
    if i % 5==0:
        shutil.move(source+files[data[i]],asm_distributed+folder_1)
    elif i%5==1:
        shutil.move(source+files[data[i]],asm_distributed+folder_2)
    elif i%5 ==2:
        shutil.move(source+files[data[i]],asm_distributed+folder_3)
    elif i%5 ==3:
        shutil.move(source+files[data[i]],asm_distributed+folder_4)
    elif i%5 ==4:
        shutil.move(source+files[data[i]],asm_distributed+folder_5)


# features for asm files based on various research papers and blogs.
prefixes = ['ID','HEADER:','.text:','.Pav:','.idata:','.data:','.bss:','.rdata:','.edata:','.rsrc:','.tls:','.reloc:','.BSS:','.CODE']
opcodes = ['jmp', 'mov', 'retf', 'push', 'pop', 'xor', 'retn', 'nop', 'sub', 'inc', 'dec', 'add','imul', 'xchg', 'or', 'shr', 'cmp', 'call', 'shl', 'ror', 'rol', 'jnb','jz','rtn','lea','movzx']
keywords = ['.dll','std::',':dword']
registers=['edx','esi','eax','ebx','ecx','edi','ebp','esp','eip']
features_asm = prefixes + opcodes + keywords + registers




#process 1
def extract_feature_asm1():
    asm_distributed = 'C:\\Users\\Vipul Singh\\Desktop\\train (1)\\asm_distributed\\'
    folder = 'first'
    feature_list = features_asm
    asm_feature_file1=open(asm_distributed+folder+'.csv','w')
    asm_writer1 = csv.writer(asm_feature_file1, delimiter=',', quotechar='"')
    asm_writer1.writerow(feature_list)
    for idx, f in enumerate(os.listdir(asm_distributed+folder)):
        freq_features = dict(zip(feature_list, [0 for i in range(len(feature_list))]))
        freq_features['name'] = f.split('.')[0]
        with codecs.open(asm_distributed + folder+'//'+f, encoding='cp1252',errors ='replace') as file:
            for line in file.readlines():
                for word in line.split(' '):
                    for feature in feature_list[2:]:
                        if feature in  word:
                            freq_features[feature] +=1
        asm_writer1.writerow(list(freq_features.values()))
    asm_feature_file1.close()
     

#  process 2
def extract_feature_asm2():
    asm_distributed = 'C:\\Users\\Vipul Singh\\Desktop\\train (1)\\asm_distributed\\'
    folder ='second'
    feature_list = features_asm
    asm_feature_file2=open(asm_distributed+folder+'.csv','w')
    asm_writer2 = csv.writer(asm_feature_file2, delimiter=',', quotechar='"')
    asm_writer2.writerow(feature_list)
    for idx, f in enumerate(os.listdir(asm_distributed+folder)):
        freq_features = dict(zip(feature_list, [0 for i in range(len(feature_list))]))
        freq_features['name'] = f.split('.')[0]
        with codecs.open(asm_distributed + folder+'//'+f, encoding='cp1252',errors ='replace') as file:
            for line in file.readlines():
                for word in line.split(' '):
                    for feature in feature_list[2:]:
                        if feature in  word:
                            freq_features[feature] +=1
        asm_writer2.writerow(list(freq_features.values()))
    asm_feature_file2.close()
     
# process 3        
def extract_feature_asm3():
    asm_distributed = 'C:\\Users\\Vipul Singh\\Desktop\\train (1)\\asm_distributed\\'
    folder ='third'
    feature_list = features_asm
    asm_feature_file3=open(asm_distributed+folder+'.csv','w')
    asm_writer3 = csv.writer(asm_feature_file3, delimiter=',', quotechar='"')
    asm_writer3.writerow(feature_list)
    for idx, f in enumerate(os.listdir(asm_distributed+folder)):
        freq_features = dict(zip(feature_list, [0 for i in range(len(feature_list))]))
        freq_features['name'] = f.split('.')[0]
        with codecs.open(asm_distributed + folder+'//'+f, encoding='cp1252',errors ='replace') as file:
            for line in file.readlines():
                for word in line.split(' '):
                    for feature in feature_list[2:]:
                        if feature in  word:
                            freq_features[feature] +=1
        asm_writer3.writerow(list(freq_features.values()))
    asm_feature_file3.close()
     
# process 4        
def extract_feature_asm4():
    asm_distributed = 'C:\\Users\\Vipul Singh\\Desktop\\train (1)\\asm_distributed\\'
    folder ='fourth'
    feature_list = features_asm
    asm_feature_file4=open(asm_distributed+folder+'.csv','w')
    asm_writer4 = csv.writer(asm_feature_file4, delimiter=',', quotechar='"')
    asm_writer4.writerow(feature_list)
    for idx, f in enumerate(os.listdir(asm_distributed+folder)):
        freq_features = dict(zip(feature_list, [0 for i in range(len(feature_list))]))
        freq_features['name'] = f.split('.')[0]
        with codecs.open(asm_distributed + folder+'//'+f, encoding='cp1252',errors ='replace') as file:
            for line in file.readlines():
                for word in line.split(' '):
                    for feature in feature_list[2:]:
                        if feature in  word:
                            freq_features[feature] +=1
        asm_writer4.writerow(list(freq_features.values()))
    asm_feature_file4.close()
     
# process 5            
def extract_feature_asm5():
    asm_distributed = 'C:\\Users\\Vipul Singh\\Desktop\\train (1)\\asm_distributed\\'
    folder ='fifth'
    feature_list = features_asm
    asm_feature_file5=open(asm_distributed+folder+'.csv','w')
    asm_writer5 = csv.writer(asm_feature_file5, delimiter=',', quotechar='"')
    asm_writer5.writerow(feature_list)
    for idx, f in enumerate(os.listdir(asm_distributed+folder)):
        freq_features = dict(zip(feature_list, [0 for i in range(len(feature_list))]))
        freq_features['name'] = f.split('.')[0]
        with codecs.open(asm_distributed + folder+'//'+f, encoding='cp1252',errors ='replace') as file:
            for line in file.readlines():
                for word in line.split(' '):
                    for feature in feature_list[2:]:
                        if feature in  word:
                            freq_features[feature] +=1
        asm_writer5.writerow(list(freq_features.values()))
    asm_feature_file5.close()
     


def main():
    #the below code is used for multiprogramming
    #the number of process depends upon the number of cores present System
    #process is used to call multiprogramming
    manager=multiprocessing.Manager() 	
    p1=Process(target=extract_feature_asm1())
    p2=Process(target=extract_feature_asm2())
    p3=Process(target=extract_feature_asm3())
    p4=Process(target=extract_feature_asm4())
    p5=Process(target=extract_feature_asm5)
    #p1.start() is used to start the thread execution
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    #After completion all the threads are joined
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()

if __name__=="__main__":
    main()


# read the csv files gnerated by 5 processes
asm_data1 = pd.read_csv('C:\\Users\\Vipul Singh\\Desktop\\train (1)\\asm_distributed\\first.csv')
asm_data2 = pd.read_csv('C:\\Users\\Vipul Singh\\Desktop\\train (1)\\asm_distributed\\second.csv')
asm_data3 = pd.read_csv('C:\\Users\\Vipul Singh\\Desktop\\train (1)\\asm_distributed\\third.csv')
asm_data4 = pd.read_csv('C:\\Users\\Vipul Singh\\Desktop\\train (1)\\asm_distributed\\fourth.csv')
asm_data5 = pd.read_csv('C:\\Users\\Vipul Singh\\Desktop\\train (1)\\asm_distributed\\fifth.csv')

# concat all the files 
asm_data = pd.concat([asm_data1, asm_data2, asm_data3, asm_data4, asm_data5], axis = 0)

# merge the size feature 
asm = pd.merge(asm_data, df_size_asm, on='ID', how='left')

# save the asm data to csv 
asm.to_csv('C:\\Users\\Vipul Singh\\Desktop\\train (1)\\Asm.csv', index = False)



