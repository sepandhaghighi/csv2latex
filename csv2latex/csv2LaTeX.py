import os
from .params import *
import sys
import requests

def check_update(DEBUG=False):
    '''
    This function check csv2latex site for newversion
    :param DEBUG: Flag for using Debug mode
    :type DEBUG:bool
    :return: True if new version is available
    '''
    try:
        new_version=requests.get(UPDATE_URL).text
        if float(new_version)>float(version):
            print("New Version ("+new_version+") Of csv2latex is available (visit github page)")
    except Exception as e:
        if DEBUG==True:
            print(str(e))

def line(number,char="-"):
    '''
    :param number: number of items to print
    :param char: each item of printed line
    :return: line string
    '''
    response=""
    i=0
    while(i<number):
        response+=char
        i+=1
    return response
def logo_handler():
    '''
    :return: None (print logo)
    '''
    try:
        print(logo)
        print("Version : "+str(version))
    except:
        pass
def signature(frame=41):
    '''
    :param frame: number of items in line
    :return: header string
    '''
    logo_handler()
    sign=line(frame,char="%")
    sign = sign + "\n"
    sign = sign + "For more info please visit : https://github.com/sepandhaghighi/csv2latex\n"
    sign=sign+line(frame,"%")
    return sign
    #% "ModernCV" CV and Cover Letter
    #% LaTeX Template
    #% Version 1.1 (9/12/12)

def escape_char(lines_list):
    '''

    :param lines_list: list of lines as input (list of strings)
    :return: list of lines after escape character
    '''
    for i,item_1 in enumerate(lines_list):
        for j,item_2 in enumerate(item_1):
            for char in char_list:  # instead of using for use a list to find and replace
                lines_list[i][j]=item_2.replace(char,"\\"+char)
    return lines_list


def white_space(line_list):
    '''

    :param line_list: list of lines as input (list of strings)
    :return: list of comma seperated item in plain text for spacing in next step
    '''
    len_list = []
    for line in line_list:
        if len(len_list)==0:
            len_list.extend(list(map(len,line)))
        else:
            if len(line) <= len(len_list):
                for i,item in enumerate(line):
                    if len(item) > len_list[i]:
                        len_list[i] = len(item)
    return len_list


def header_handler(file,col_num,caption="my-caption",label="my-label"):
    '''

    :param file: input latex file
    :param col_num: number of col
    :param caption: caption for table
    :param label: label for table
    :return: None
    '''
    file.write(header["static_1"])
    file.write(header["static_2"])
    file.write(header["caption"]+"{"+caption+"}\n")
    file.write(header["label"]+"{"+label+"}\n")
    file.write(header["align"]+"{"+"c"*col_num+"}\n")

def footer_handler(file):
    '''

    :param file: latex file
    :return: None
    '''
    file.write(footer+"\n")


def read_csv(file_name):
    '''

    :param file_name: csv file name (as string)
    :return: list of csv file lines
    '''
    csv_file=open(file_name,"r")
    csv_lines=[]
    for line in csv_file:
        splited_line=line.split(",")
        csv_lines.append(splited_line)
    csv_file.close()
    return csv_lines

def create_latex(file_name,dir_folder="LaTeX",empty_space=True):

    '''

    :param file_name: file name of latex file 9(as string)
    :param dir_folder: output folder name (as string)
    :param empty_space: boolean paramter (True-->modify empty space)
    :return:  None
    '''
    try:
        print("\nCreate LaTeX table for "+file_name+" . . .")
        latex_file=open(os.path.join(os.getcwd(),dir_folder,file_name[:-4]+".tex"),"w")
        csv_read=read_csv(file_name)
        csv_lines=csv_read  # continue using csv_read without declairing csv_lines

        col_num=len(csv_lines[0])
        header_handler(latex_file,col_num=col_num) # col_num is useless here
        escape_out=escape_char(csv_lines)
        list_len = white_space(escape_out)
        for item in escape_out :
            for i,item_2 in enumerate(item):
                if i<len(item)-1:
                    latex_file.write(item_2)
                    if empty_space==True:
                        latex_file.write(" " * (list_len[i]-len(item_2)))
                    latex_file.write("&")
                    if empty_space==True:
                        latex_file.write(" "*list_len[i])
                else:
                    latex_file.write(item_2[:-1])
            latex_file.write("\\\\"+"\n")
        footer_handler(latex_file)
        latex_file.close()
        print("Done!")
        print(line(70, "*"))
    except:
        print("Error In LaTeX Creation")

def make_dir():
    '''

    :return: None
    '''
    if "LaTeX" not in os.listdir():
        try:
            os.mkdir("LaTeX")
        except:
            print("Access Error")
            sys.exit()










