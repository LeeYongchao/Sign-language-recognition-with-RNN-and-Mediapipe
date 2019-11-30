import xlsxwriter
import os
import sys
import numpy as np
        
def convert_tuple(value):
    if not isinstance(value, tuple):
        return value

        return str(value)

def make_xlxs(input_file_path, worksheet_name):
    with open(input_file_path, mode = 'r') as t:
        text = list(t)
        string = " ".join(text)
        landmarks = string.split(" ")
    
    workbook = xlsxwriter.Workbook(worksheet_name)
    worksheet = workbook.add_worksheet()
    
    row=0
    col=0

    for landmark in landmarks:
        landmark_frame = map(convert_tuple, landmarks[row*42:(row*42)+42])
        print(landmark_frame)
        print("\n")
        worksheet.write_row(row,col, landmark_frame)
        row += 1
    
    workbook.close()
    print(workbook)

def return_frame(dirname):
    fr=[]
    listfile=os.listdir(dirname)
    for file in listfile:
        if "_" in file: #ignore mp4 files
            continue
        wordname=file
        textlist=os.listdir(dirname+wordname)
        for text in textlist:
            if "DS_" in text:
                continue
            textname=dirname+wordname+"/"+text
            with open(textname, mode = 'r') as t: #open txt files 
                numbers = np.array([float(num) for num in t.read().split()])
                #print(len(numbers)/42)
                fr.append(int(len(numbers)/42))
    print(fr)
                
    
    
def main():
    #make_xlxs("/Users/anna/SLR/sentenceOutput/Sentence/bird-like-apple.txt", 'bird-like-apple.xlsx')
    return_frame("/Users/anna/SLR/twenty/traindata/")
    
if __name__=="__main__":
    main()
