import numpy as np
import pickle
import os
import sys
import argparse
import random

def search(dirname):
    listfile=os.listdir(dirname)
    predict=[]
    maxlen=0
    listlength=[]
    for file in listfile:
        wordname=file
        textlist=os.listdir(dirname+wordname)
        #print(wordname)
        for namet in textlist:
            textnamed=dirname+wordname+"/"+namet
            with open(textnamed) as datad:
                lend=[[i for i in line.split(' ')][:-1] for line in datad.readlines()]
                listlength.append(len(lend[0]))
                #print(len(lend))
                #print(len(lend[0]))
        maxlen=max(listlength)
    #print("최대길이:")
    #print(maxlen)
    for file in listfile:
        wordname=file
        textlist=os.listdir(dirname+wordname)
        for text in textlist:
            textname=dirname+wordname+"/"+text
            with open(textname) as data:
                numbers = [[i for i in line.split(' ')][:-1] for line in data.readlines()]
                #print(len(numbers[0]))
                for i in range(len(numbers[0]),maxlen):
                    numbers[0].extend([0.000])
                numbers.append(wordname)
                #print(numbers[0][8735])
            predict.append(numbers)
    random.shuffle(predict)        
    return predict

def main(inputfile_path,output_path):
	ret=search(inputfile_path)
	np.shape(ret)
	out_file=output_path+'test_data.pkl'
	with open(out_file,'wb') as fout:
		pickle.dump(ret,fout)

if __name__=="__main__":
	parser = argparse.ArgumentParser(description='make pkl_file')
	parser.add_argument("--input_file_path",help=" ")
	parser.add_argument("--output_path",help=" ")
	args=parser.parse_args()
	input_file_path=args.input_file_path
	output_path=args.output_path
	main(input_file_path,output_path)



