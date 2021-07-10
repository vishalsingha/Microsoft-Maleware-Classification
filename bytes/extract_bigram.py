import tqdm
import os
import itertools
import collections
import multiprocessing
from multiprocess import Process

files = os.listdir('byteFiles')


# unigram feature list
hexcode_list = ['00', '11', '22', '33', '44', '55', '66', '77', '88', '99', '0A', '0B', '0C', '0D', '0E', '0F', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '1A', '1B', '1C', '1D', '1E', '1F', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '2A', '2B', '2C', '2D', '2E', '2F', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '3A', '3B', '3C', '3D', '3E', '3F', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '4A', '4B', '4C', '4D', '4E', '4F', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '5A', '5B', '5C', '5D', '5E', '5F', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '6A', '6B', '6C', '6D', '6E', '6F', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '7A', '7B', '7C', '7D', '7E', '7F', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '8A', '8B', '8C', '8D', '8E', '8F', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '9A', '9B', '9C', '9D', '9E', '9F', 'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'BA', 'BB', 'BC', 'BD', 'BE', 'BF', 'C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'CA', 'CB', 'CC', 'CD', 'CE', 'CF', 'D0', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'DA', 'DB', 'DC', 'DD', 'dE', 'DF', 'E0', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'EA', 'EB', 'EC', 'ED', 'EE', 'Ef', 'F0', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'FA', 'FB', 'FC', 'FD', 'FE', 'FF', '??']

# combination of unigram feature taken two at a time
bigrams_features = list(itertools.combinations(hexcode_list, 2))


# function to process folder1

def fun1():
    print('fun1 started...')

    byte_feature_file=open('result_bigram1.csv','w+')
    byte_feature_file.write('filename,')
    # write bigram features names
    byte_feature_file.write(','.join(['_'.join(list(name)) for name in bigrams_features]))
    
        
    # iterate for each file of .bytes file
    for file in os.listdir('bytes/bytes1'):
        byte_feature_file.write("\n")
        byte_feature_file.write(file+",")
        if(file.endswith("txt")):
            # open file
            with open('bytes/bytes1/'+file,"r") as byte_flie:
                # read the file
                content = byte_flie.readlines()
                # replace \n and space from content
                content = [line.replace('\n', '').rstrip().split(" ") for line in content]
                content = [' '.join(line) for line in content]
                # finding all the bigrams for content
                bigram_content = [b for l in content for b in zip(l.split(" ")[:-1], l.split(" ")[1:])]
                # counting each bigram in content
                counter_dict = collections.Counter(bigram_content)
                bigram_feature_val = []
                for idx in range(len(bigrams_features)):
                    try:
                        bigram_feature_val.append(str(counter_dict[bigrams_features[idx]]))
                    except:
                        bigram_feature_val.append(str(0))
                if len(bigram_feature_val)==len(bigrams_features):
                    byte_feature_file.write(','.join(bigram_feature_val))
                else:
                    print("Got the list of length",len(bigram_feature_val), "and expected", len(bigrams_features))
                    break
                    
# function to process folder2

def fun2():
    print('fun2 started...')
    
    byte_feature_file=open('result_bigram2.csv','w+')
    byte_feature_file.write('filename,')

    # write bigram features names
    byte_feature_file.write(','.join(['_'.join(list(name)) for name in bigrams_features]))
    
    # iterate for each file of .bytes file
    for file in os.listdir('bytes/bytes2'):
        byte_feature_file.write("\n")
        byte_feature_file.write(file+",")
        if(file.endswith("txt")):
            # open file
            with open('bytes/bytes2/'+file,"r") as byte_flie:
                # read the file
                content = byte_flie.readlines()
                # replace \n and space from content
                content = [line.replace('\n', '').rstrip().split(" ") for line in content]
                content = [' '.join(line) for line in content]
                # finding all the bigrams for content
                bigram_content = [b for l in content for b in zip(l.split(" ")[:-1], l.split(" ")[1:])]
                # counting each bigram in content
                counter_dict = collections.Counter(bigram_content)
                bigram_feature_val = []
                for idx in range(len(bigrams_features)):
                    try:
                        bigram_feature_val.append(str(counter_dict[bigrams_features[idx]]))
                    except:
                        bigram_feature_val.append(str(0))
                if len(bigram_feature_val)==len(bigrams_features):                                                                                                           byte_feature_file.write(','.join(bigram_feature_val))
#                     byte_feature_file.write("\n")
                else:
                    print("Got the list of length",len(bigram_feature_val), "and expected", len(bigrams_features))
                    break
                
# function to process folder3
                
def fun3():
    print('fun3 started...')
    byte_feature_file=open('result_bigram3.csv','w+')
    byte_feature_file.write('filename,')

    # write bigram features names
    byte_feature_file.write(','.join(['_'.join(list(name)) for name in bigrams_features]))
    
    
    # iterate for each file of .bytes file
    for file in os.listdir('bytes/bytes3'):
        byte_feature_file.write("\n")
        byte_feature_file.write(file+",")
        if(file.endswith("txt")):
            # open file
            with open('bytes/bytes3/'+file,"r") as byte_flie:
                # read the file
                content = byte_flie.readlines()
                # replace \n and space from content
                content = [line.replace('\n', '').rstrip().split(" ") for line in content]
                content = [' '.join(line) for line in content]
                # finding all the bigrams for content
                bigram_content = [b for l in content for b in zip(l.split(" ")[:-1], l.split(" ")[1:])]
                # counting each bigram in content
                counter_dict = collections.Counter(bigram_content)
                bigram_feature_val = []
                for idx in range(len(bigrams_features)):
                    try:
                        bigram_feature_val.append(str(counter_dict[bigrams_features[idx]]))
                    except:
                        bigram_feature_val.append(str(0))
                if len(bigram_feature_val)==len(bigrams_features):   
                    byte_feature_file.write(','.join(bigram_feature_val))
                else:
                    print("Got the list of length",len(bigram_feature_val), "and expected", len(bigrams_features))
                    break
                    
# function to process folder4

def fun4():
    print('fun4 started...')

    byte_feature_file=open('result_bigram4.csv','w+')
    byte_feature_file.write('filename,')

    
    # write bigram features names
    byte_feature_file.write(','.join(['_'.join(list(name)) for name in bigrams_features]))
    byte_feature_file.write("\n")
    
    # iterate for each file of .bytes file
    for file in os.listdir('bytes/bytes4'):
        byte_feature_file.write("\n")
        byte_feature_file.write(file+",")
        if(file.endswith("txt")):
            # open file
            with open('bytes/bytes4/'+file,"r") as byte_flie:
                # read the file
                content = byte_flie.readlines()
                # replace \n and space from content
                content = [line.replace('\n', '').rstrip().split(" ") for line in content]
                content = [' '.join(line) for line in content]
                # finding all the bigrams for content
                bigram_content = [b for l in content for b in zip(l.split(" ")[:-1], l.split(" ")[1:])]
                # counting each bigram in content
                counter_dict = collections.Counter(bigram_content)
                bigram_feature_val = []
                for idx in range(len(bigrams_features)):
                    try:
                        bigram_feature_val.append(str(counter_dict[bigrams_features[idx]]))
                    except:
                        bigram_feature_val.append(str(0))
                if len(bigram_feature_val)==len(bigrams_features): 
                    byte_feature_file.write(','.join(bigram_feature_val))
                else:
                    print("Got the list of length",len(bigram_feature_val), "and expected", len(bigrams_features))
                    break
                    
# function to process folder5

def fun5():
    print('fun5 started...')
    byte_feature_file=open('result_bigram5.csv','w+')
    byte_feature_file.write('filename,')
    
    # write bigram features names
    byte_feature_file.write(','.join(['_'.join(list(name)) for name in bigrams_features]))
    
    # iterate for each file of .bytes file
    for file in os.listdir('bytes/bytes5'):
        byte_feature_file.write("\n")
        byte_feature_file.write(file+",")
        if(file.endswith("txt")):
            # open file
            with open('bytes/bytes5/'+file,"r") as byte_flie:
                # read the file
                content = byte_flie.readlines()
                # replace \n and space from content
                content = [line.replace('\n', '').rstrip().split(" ") for line in content]
                content = [' '.join(line) for line in content]
                # finding all the bigrams for content
                bigram_content = [b for l in content for b in zip(l.split(" ")[:-1], l.split(" ")[1:])]
                # counting each bigram in content
                counter_dict = collections.Counter(bigram_content)
                bigram_feature_val = []
                for idx in range(len(bigrams_features)):
                    try:
                        bigram_feature_val.append(str(counter_dict[bigrams_features[idx]]))
                    except:
                        bigram_feature_val.append(str(0))
                if len(bigram_feature_val)==len(bigrams_features):
                    byte_feature_file.write(','.join(bigram_feature_val))
                else:
                    print("Got the list of length",len(bigram_feature_val), "and expected", len(bigrams_features))
                    break


# function to process folder6

def fun6():
    print('fun6 started...')


    byte_feature_file=open('result_bigram6.csv','w+')
    byte_feature_file.write('filename,')
 
    # write bigram features names
    byte_feature_file.write(','.join(['_'.join(list(name)) for name in bigrams_features]))
        
    # iterate for each file of .bytes file
    for file in os.listdir('bytes/bytes6'):
        byte_feature_file.write("\n")
        byte_feature_file.write(file+",")
        if(file.endswith("txt")):
            # open file
            with open('bytes/bytes6/'+file,"r") as byte_flie:
                # read the file
                content = byte_flie.readlines()
                # replace \n and space from content
                content = [line.replace('\n', '').rstrip().split(" ") for line in content]
                content = [' '.join(line) for line in content]
                # finding all the bigrams for content
                bigram_content = [b for l in content for b in zip(l.split(" ")[:-1], l.split(" ")[1:])]
                # counting each bigram in content
                counter_dict = collections.Counter(bigram_content)
                bigram_feature_val = []
                for idx in range(len(bigrams_features)):
                    try:
                        bigram_feature_val.append(str(counter_dict[bigrams_features[idx]]))
                    except:
                        bigram_feature_val.append(str(0))
                if len(bigram_feature_val)==len(bigrams_features):
                    byte_feature_file.write(','.join(bigram_feature_val))
                else:
                    print("Got the list of length",len(bigram_feature_val), "and expected", len(bigrams_features))
                    break
                    
# function to process folder7

def fun7():
    print('fun7 started...')

    
    byte_feature_file=open('result_bigram7.csv','w+')
    byte_feature_file.write('filename,')

    # write bigram features names
    byte_feature_file.write(','.join(['_'.join(list(name)) for name in bigrams_features]))
    
    # iterate for each file of .bytes file
    for file in os.listdir('bytes/bytes7'):
        byte_feature_file.write("\n")
        byte_feature_file.write(file+",")
        if(file.endswith("txt")):
            # open file
            with open('bytes/bytes7/'+file,"r") as byte_flie:
                # read the file
                content = byte_flie.readlines()
                # replace \n and space from content
                content = [line.replace('\n', '').rstrip().split(" ") for line in content]
                content = [' '.join(line) for line in content]
                # finding all the bigrams for content
                bigram_content = [b for l in content for b in zip(l.split(" ")[:-1], l.split(" ")[1:])]
                # counting each bigram in content
                counter_dict = collections.Counter(bigram_content)
                bigram_feature_val = []
                for idx in range(len(bigrams_features)):
                    try:
                        bigram_feature_val.append(str(counter_dict[bigrams_features[idx]]))
                    except:
                        bigram_feature_val.append(str(0))
                if len(bigram_feature_val)==len(bigrams_features):                                                                                                           byte_feature_file.write(','.join(bigram_feature_val))
#                     byte_feature_file.write("\n")
                else:
                    print("Got the list of length",len(bigram_feature_val), "and expected", len(bigrams_features))
                    break
                
# function to process folder8
                
def fun8():
    print('fun8 started...')

    byte_feature_file=open('result_bigram8.csv','w+')
    byte_feature_file.write('filename,')

    # write bigram features names
    byte_feature_file.write(','.join(['_'.join(list(name)) for name in bigrams_features]))
    
    
    # iterate for each file of .bytes file
    for file in os.listdir('bytes/bytes8'):
        byte_feature_file.write("\n")
        byte_feature_file.write(file+",")
        if(file.endswith("txt")):
            # open file
            with open('bytes/bytes8/'+file,"r") as byte_flie:
                # read the file
                content = byte_flie.readlines()
                # replace \n and space from content
                content = [line.replace('\n', '').rstrip().split(" ") for line in content]
                content = [' '.join(line) for line in content]
                # finding all the bigrams for content
                bigram_content = [b for l in content for b in zip(l.split(" ")[:-1], l.split(" ")[1:])]
                # counting each bigram in content
                counter_dict = collections.Counter(bigram_content)
                bigram_feature_val = []
                for idx in range(len(bigrams_features)):
                    try:
                        bigram_feature_val.append(str(counter_dict[bigrams_features[idx]]))
                    except:
                        bigram_feature_val.append(str(0))
                if len(bigram_feature_val)==len(bigrams_features):   
                    byte_feature_file.write(','.join(bigram_feature_val))
                else:
                    print("Got the list of length",len(bigram_feature_val), "and expected", len(bigrams_features))
                    break
                    
# function to process folder9

def fun9():
    print('fun9 started...')

    byte_feature_file=open('result_bigram9.csv','w+')
    byte_feature_file.write('filename,')

    
    # write bigram features names
    byte_feature_file.write(','.join(['_'.join(list(name)) for name in bigrams_features]))
    byte_feature_file.write("\n")
    
    # iterate for each file of .bytes file
    for file in os.listdir('bytes/bytes9'):
        byte_feature_file.write("\n")
        byte_feature_file.write(file+",")
        if(file.endswith("txt")):
            # open file
            with open('bytes/bytes9/'+file,"r") as byte_flie:
                # read the file
                content = byte_flie.readlines()
                # replace \n and space from content
                content = [line.replace('\n', '').rstrip().split(" ") for line in content]
                content = [' '.join(line) for line in content]
                # finding all the bigrams for content
                bigram_content = [b for l in content for b in zip(l.split(" ")[:-1], l.split(" ")[1:])]
                # counting each bigram in content
                counter_dict = collections.Counter(bigram_content)
                bigram_feature_val = []
                for idx in range(len(bigrams_features)):
                    try:
                        bigram_feature_val.append(str(counter_dict[bigrams_features[idx]]))
                    except:
                        bigram_feature_val.append(str(0))
                if len(bigram_feature_val)==len(bigrams_features): 
                    byte_feature_file.write(','.join(bigram_feature_val))
                else:
                    print("Got the list of length",len(bigram_feature_val), "and expected", len(bigrams_features))
                    break
                    
# function to process folder10

def fun10():
    print('fun10 started...')

    byte_feature_file=open('result_bigram10.csv','w+')
    byte_feature_file.write('filename,')
    
    # write bigram features names
    byte_feature_file.write(','.join(['_'.join(list(name)) for name in bigrams_features]))
    
    # iterate for each file of .bytes file
    for file in os.listdir('bytes/bytes10'):
        byte_feature_file.write("\n")
        byte_feature_file.write(file+",")
        if(file.endswith("txt")):
            # open file
            with open('bytes/bytes10/'+file,"r") as byte_flie:
                # read the file
                content = byte_flie.readlines()
                # replace \n and space from content
                content = [line.replace('\n', '').rstrip().split(" ") for line in content]
                content = [' '.join(line) for line in content]
                # finding all the bigrams for content
                bigram_content = [b for l in content for b in zip(l.split(" ")[:-1], l.split(" ")[1:])]
                # counting each bigram in content
                counter_dict = collections.Counter(bigram_content)
                bigram_feature_val = []
                for idx in range(len(bigrams_features)):
                    try:
                        bigram_feature_val.append(str(counter_dict[bigrams_features[idx]]))
                    except:
                        bigram_feature_val.append(str(0))
                if len(bigram_feature_val)==len(bigrams_features):
                    byte_feature_file.write(','.join(bigram_feature_val))
                else:
                    print("Got the list of length",len(bigram_feature_val), "and expected", len(bigrams_features))
                    break
                    
                    
                    
def main():
    #the below code is used for multiprogramming
    #the number of process depends upon the number of cores present System
    #process is used to call multiprogramming
    manager=multiprocessing.Manager() 
    p1=Process(target=fun1)
    p2=Process(target=fun2)
    p3=Process(target=fun3)
    p4=Process(target=fun4)
    p5=Process(target=fun5)
    p6=Process(target=fun6)
    p7=Process(target=fun7)
    p8=Process(target=fun8)
    p9=Process(target=fun9)
    p10=Process(target=fun10)

    #p1.start() is used to start the thread execution
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    p9.start()
    p10.start()

    #After completion all the threads are joined
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    p8.join()
    p9.join()
    p10.join()
    print('Done')


if __name__=="__main__":
    main()

                    