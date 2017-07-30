from .csv2LaTeX import *
import doctest
import sys
if __name__=="__main__":
    args=sys.argv
    if len(args)>1:
        if args[1].upper()=="TEST":
            doctest.testfile("test.py",verbose=True)
        else:
            print("Bad Input")
    else:
        check_update()
        print(signature())
        list_of_files=os.listdir()
        csv_files=[]
        make_dir()
        for i in list_of_files:
            if i.find(".csv")!=-1:
                csv_files.append(i)
        if len(csv_files)==0:
            print("There is no csv file in this folder (Please copy your csv files here)")
            print("Current Directory : "+str(os.getcwd()))
            sys.exit()
        else:
            print(str(len(csv_files))+" CSV file found in this folder! ;-) ")
            for item in csv_files:
                create_latex(item)