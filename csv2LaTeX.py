import os
from params import *
import sys
def line(number,char="-"):
    response=""
    for i in range(number):
        response=response+char
    return response

def escape_char(lines_list):
    for i in range(len(lines_list)):
        for j in range(len(lines_list[i])):
            for char in char_list:
                lines_list[i][j]=lines_list[i][j].replace(char,"\\"+char)
    return lines_list



def header_handler(file,col_num,caption="my-caption",label="my-label"):
    file.write(header["static_1"])
    file.write(header["static_2"])
    file.write(header["caption"]+"{"+caption+"}\n")
    file.write(header["label"]+"{"+label+"}\n")
    file.write(header["align"]+"{"+"c"*col_num+"}\n")
def footer_handler(file):
    file.write(footer+"\n")


def read_csv(file_name):
    csv_file=open(file_name,"r")
    csv_lines=[]
    for line in csv_file:
        csv_lines.append(line.split(","))
    csv_file.close()
    return csv_lines

def create_latex(file_name,dir_folder="LaTeX"):
    print("\nCreate LaTeX table for "+file_name+" . . .")
    latex_file=open(os.path.join(os.getcwd(),dir_folder+"\\")+file_name[:-4]+".tex","w")
    csv_lines=read_csv(file_name)
    col_num=len(csv_lines[0])
    header_handler(latex_file,col_num=col_num)
    for item in escape_char(csv_lines):
        for i in range(len(item)):
            latex_file.write(item[i])
            if i<len(item)-1:
                latex_file.write("&")
        latex_file.write("\\\\"+"\n")
    footer_handler(latex_file)
    latex_file.close()
    print("Done!")
    print(line(70, "*"))
def make_dir():
    if "LaTeX" not in os.listdir():
        os.mkdir("LaTeX")
if __name__=="__main__":
    list_of_files=os.listdir()
    csv_files=[]
    make_dir()
    for i in list_of_files:
        if i.find(".csv")!=-1:
            csv_files.append(i)
    if len(csv_files)==0:
        print("There is no csv file")
        sys.exit()
    else:
        for item in csv_files:
            create_latex(item)








