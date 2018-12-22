#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: liaoshengyou
# datetime: 2018/10/1 下午9:58
# software: PyCharm
# File: Parse_Xml.py
import sys
sys.path.append("..")
import xml.etree.ElementTree as ET
import sys
import os


# print 'root_tag:%s' %(root.tag)
# print 'root_attrib:%s' %(root.attrib)
# print 'root_text:%s' %(root.text)


def Get_Tag(Tag):
    name = Tag.split("}")[1]
    return name


def check_txt(lable):
    if lable:
        return lable
    else:
        return "None"


def get_in_dict(result, a, b):
    if a:
        if a != "":
            result.append(a, b)


def Get_Dict(Sample_Dict, child_name, check_txt):
    if child_name == "":
        print "%s is None " % (child_name)
    else:
        if child_name not in Argv_List:
            Argv_List.append(child_name)

        if child_name not in Sample_Dict:
            Sample_Dict[child_name] = []
            Sample_Dict[child_name].append(check_txt.strip())
        else:
            Sample_Dict[child_name].append(check_txt.strip())


def main(File, Sample_Dict):
    tree = ET.parse(File)
    root = tree.getroot()
    for child in root:
        child_name = Get_Tag(root.tag)
        Get_Dict(Sample_Dict, child_name, check_txt(root.text))
        # print "%s	%s" %(child_name,check_txt(root.text))
        for sub in child:
            sub_name = Get_Tag(sub.tag)
            Get_Dict(Sample_Dict, sub_name, check_txt(sub.text))
            # sub_name = child_name+"-"+Get_Tag(sub.tag)
            # print "%s	%s" %(sub_name,check_txt(sub.text))
            for zi in sub:
                zi_name = Get_Tag(zi.tag)
                # zi_name = child_name+"-"+sub_name+"-"+Get_Tag(zi.tag)
                Get_Dict(Sample_Dict, zi_name, check_txt(zi.text))
                # print "%s	%s" %(zi_name,check_txt(zi.text))
                # '''
                for zizi in zi:
                    zizi_name = Get_Tag(zizi.tag)
                    # zizi_name = child_name+"-"+sub_name+"-"+zi_name+"-"+Get_Tag(zizi.tag)
                    Get_Dict(Sample_Dict, zizi_name, check_txt(zizi.text))
                    # print "%s	%s" %(zizi_name,check_txt(zizi.text))
                    for zizizi in zizi:
                        zizizi_name = Get_Tag(zizizi.tag)
                        # zizi_name = child_name+"-"+sub_name+"-"+zi_name+"-"+Get_Tag(zizi.tag)
                        Get_Dict(
                            Sample_Dict, zizizi_name, check_txt(
                                zizizi.text))
                        # print "%s	%s" %(zizi_name,check_txt(zizi.text))
                        for zizizizi in zizizi:
                            zizizizi_name = Get_Tag(zizizizi.tag)
                            # zizi_name = child_name+"-"+sub_name+"-"+zi_name+"-"+Get_Tag(zizi.tag)
                            Get_Dict(
                                Sample_Dict, zizizizi_name, check_txt(
                                    zizizizi.text))
                            # print "%s	%s" %(zizi_name,check_txt(zizi.text))
                # '''
    return Sample_Dict


def Check_Num_Empty(List):
    temp = list(set(List))
    if len(temp) == 1 and (temp[0] == "" or temp[0] == "None"):
        return ""
    else:
        return ",".join([str(b) for b in File_Name_value[i]])


if __name__ == '__main__':
    FileList = sys.argv[1]
    Argv_List = ["Flie_Name", "TCGA_Name"]
    #
    Sample_Dict = {}
    for i in open(FileList, 'r'):
        if i.startswith("id"):
            continue
        Nline = i.strip().split('\t')
        Path = os.getcwd()
        Flie_Name = Nline[0]
        TCGA_Name = Nline[1].split('.')[3]
        File = "/".join([Path, Flie_Name, Nline[1]])
        # print File
        Sample_Dict[Flie_Name] = {}

        Sample_Dict[Flie_Name]["TCGA_Name"] = TCGA_Name
        Sample_Dict[Flie_Name]["Flie_Name"] = Flie_Name
        main(File, Sample_Dict[Flie_Name])

    print "\t".join([str(b) for b in Argv_List])

    for File_Name, File_Name_value in Sample_Dict.items():
        key_value = []
        for i in Argv_List:
            # print i,File_Name_value[i]
            if i not in File_Name_value:
                key_value.append("")
            else:
                # print type(File_Name_value[i])
                if isinstance(File_Name_value[i], list):
                    key_value.append(Check_Num_Empty(File_Name_value[i]))
                else:
                    key_value.append(File_Name_value[i])
                # print key_value
        print "\t".join([b for b in key_value])
