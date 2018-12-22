import json
import copy
import sys
import os

def analysis_recursive(obj, rDic, resultList):

    recordDic = copy.deepcopy(rDic)
    if isinstance(obj,dict):
        flag = True
        for k,v in obj.iteritems():
            if not (isinstance(v, dict) or isinstance(v, list)):
                recordDic[k] = v
            else:
                flag = False

        if flag:
            resultList.append(recordDic)
            return

        for k,v in obj.iteritems():
            if isinstance(v,dict) or isinstance(v,list):
                analysis_recursive(v, recordDic, resultList)


    if isinstance(obj,list):
        for v in obj:
            analysis_recursive(v, recordDic, resultList)

def file_step(in_File, out_File):
    resultList = []
    with open(in_File,'r') as f:
        obj = json.load(f)
        # json_step(obj)
        analysis_recursive(obj,{}, resultList)


    print(len(resultList))
    resultSet = set()
    for item in resultList:
        resultSet.update(item.keys())

    colName = list(resultSet)
    with open(out_File, "w") as f:
        f.write("\t".join(colName) + "\n")
        for item in resultList:
            templist = [str(item.get(col, "")) for col in colName]
            f.write("\t".join(templist) + "\n")

# def json_step(obj):
#
#     recordList = []
#     for item in obj:
#         recordDict = {}
#         caseID = item["case_id"]
#         recordDict["case_id"] = caseID
#         samplesList= item["samples"]
#         print len(samplesList)
#         for sampleDic in samplesList:
#             portionsList = sampleDic['portions']
#             for portionDic in portionsList:
#                 print portionDic.keys()
#                 analytesList = portionDic["analytes"]
#                 for analyteDic in analytesList:
#                     aliquotsList = analyteDic['aliquots']
#                     for aliquotDic in aliquotsList:
#                         continue

if __name__ == '__main__':
    # filepath = "TCGA-THYM_biospecimen.project-TCGA-THYM.2017-09-22T18-13-27.943934.json"
    # outdir = "./"
    in_File = sys.argv[1]
    out_File = sys.argv[2]
    file_step(in_File, out_File)
