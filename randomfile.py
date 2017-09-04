## Generate Random file and RandomContent for each path
##
##  Auth HuangYZ
##  usage:
##      python randomfile.py rootdir maxsize(in MB)
##      python randomfile.py rootdir clear
## 

import os
import os.path
import random
import sys

filenameext_table=[".idext",".ccfba",".jgeff",".ppav1",".edbin",".c_db"];

def generate_random(path):
    #generate random filename
    filename_table="abcdefghijklnmopqrstuvwxyz"
    random.shuffle(filenameext_table);
    file_name = "";
    for i in range(0,random.randint(5,10)):
        randidx = random.randint(0,len(filename_table));
        file_name += filename_table[randidx:randidx+1];
    file_name +=random.choice(filenameext_table);
    
    #genrandomecontent
    content = ""
    for i in range(10,random.randint(50,1000)):
        randidx = random.randint(0,len(filename_table));
        content+=filename_table[randidx:randidx+1]
        
    #content into file
    absfile = path + file_name
    print(absfile)
    if os.path.exists(absfile)==0:
        file_object = open(absfile,"w")
        file_object.write(content)
        file_object.close()
    
    return len(content)

def generate_random_files(path):
    maxsize = 0
    num = random.randint(1,1000)
    for i in range(0,num):
        maxsize +=generate_random(path);
    
    return maxsize;
    


def mainfunc(rootdir,sizemb):
    maxsize = 0;
    sizelmt = sizemb<<20;  #MB to BYTES
    print(sizelmt)
    for parent,dirnames,filenames in os.walk(rootdir):    
        for dirname in  dirnames:
            if maxsize < sizelmt:
                abspath = parent + '/' + dirname + '/'
                maxsize+=generate_random_files(abspath)
    
    return maxsize;


def doClear(rootdir):
    global filenameext_table
    count = 0;
    for parent,dirnames,filenames in os.walk(rootdir):
        for file in filenames:
            ext = os.path.splitext(file)[1]
            if ext in filenameext_table:
                absfile = parent + "/" + file;
                print(absfile)
                if os.path.exists(absfile)!=0:
                    print(absfile);
                    os.remove(absfile);
                    count+=1
    
    return count

#usage:
#      python randomfile.py rootdir maxsize
#      python randomfile.py rootdir clear
if __name__=="__main__":
    #rootdir = "./res"
    if len(sys.argv)!=3:
        print(len(sys.argv))
        print "usage:";
        print "     python randomfile.py rootdir maxsize";
        print "     python randomfile.py rootdir clear";
    elif len(sys.argv)==3:
        if sys.argv[2]=="clear":
            print("delete " + str(doClear(sys.argv[1])) + " files");
        else:
            sz = mainfunc(sys.argv[1],int(sys.argv[2]));
            print str(sz) + " BYTES";
        






