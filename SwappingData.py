import os 
import shutil
def swapfiles():
    file1= input("Enter the name of first file: ")
    file2= input("Enter the name of second file: ")
    with open (file1,'r') as A:
        dataA= A.read()
    with open (file2,'r') as B:
        dataB= B.read()
    with open (file1,'w') as A:
        A.write(dataB)
    with open (file2,'w') as B:
        B.write(dataA)   
    print("Swapped Successfully")     
swapfiles()    
    
