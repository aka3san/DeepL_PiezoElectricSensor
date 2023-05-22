#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import preprocess as pp
import featureValue as fv
import math
import glob
import os
#import deepL
#import nitime.algorithms as tsa
import subprocess

#FeatureValueクラスのリストとそれに対応する目的変数のリストから特徴量を取得して、csvファイルで出力する。返り値はDataFlame

def exportCSV(FeatureValueList, targetVarList, name):
    data = pd.DataFrame()
    idx = 0
    for featureValue in FeatureValueList:   
        #最初にDataFrameオブジェクトを作成する
        if idx == 0:
            data = pd.DataFrame({"A'G'": featureValue.AG, "A'E'/A'G'": featureValue.AE_AG, "E'G'/A'G'": featureValue.EG_AG, "A'C'/A'G'": featureValue.AC_AG, "C'E'/A'G'": featureValue.CE_AG, "A'B'/A'C'": featureValue.AB_AC, "B'C'/A'C'": featureValue.BC_AC, "C'D'/C'E'": featureValue.CD_CE, "D'E'/C'E'": featureValue.DE_CE, "E'F'/E'G'": featureValue.EF_EG, "F'G'/E'G'": featureValue.FG_EG, "H": featureValue.H, "f/H": featureValue.f_H, "g/H": featureValue.g_H, "i/H": featureValue.i_H, "H/A'B'": featureValue.H_AB, "S": featureValue.S, "S_sys/S": featureValue.S_sys, "S_dia/S": featureValue.S_dia}, index=[idx])
            """
            for i in range(0, 20):
                exec(f"data[\"PSD{i+1}\"] = featureValue.PSD{i+1}")
            """
            data["SBP"] = targetVarList[idx][0], 
            data["DBP"] = targetVarList[idx][1]
            idx += 1
            continue
        data_tmp = pd.DataFrame({"A'G'": featureValue.AG, "A'E'/A'G'": featureValue.AE_AG, "E'G'/A'G'": featureValue.EG_AG, "A'C'/A'G'": featureValue.AC_AG, "C'E'/A'G'": featureValue.CE_AG, "A'B'/A'C'": featureValue.AB_AC, "B'C'/A'C'": featureValue.BC_AC, "C'D'/C'E'": featureValue.CD_CE, "D'E'/C'E'": featureValue.DE_CE, "E'F'/E'G'": featureValue.EF_EG, "F'G'/E'G'": featureValue.FG_EG, "H": featureValue.H, "f/H": featureValue.f_H, "g/H": featureValue.g_H, "i/H": featureValue.i_H, "H/A'B'": featureValue.H_AB, "S": featureValue.S, "S_sys/S": featureValue.S_sys, "S_dia/S": featureValue.S_dia}, index=[idx])
        """
        for i in range(0, 20):
                exec(f"data_tmp[\"PSD{i+1}\"] = featureValue.PSD{i+1}")            
        data_tmp["SBP"] = targetVarList[idx][0]
        """
        data_tmp["DBP"] = targetVarList[idx][1]
        data = pd.concat([data, data_tmp])
        idx += 1
    data.to_csv(name, sep=',', encoding='utf-8')
    return data

#BPDatas配下の各ファイルから特徴量と目的変数を取得する

path_list=glob.glob(r"C:\Users\azlab\OneDrive - 国立大学法人東海国立大学機構\ドキュメント\PZT圧電センサ\BPDatas" + '/*')
fValueList = []
targetVarList = []
#各データをFV（特徴量）に変換
for path in path_list:
    csv = pd.read_csv(path)
    print("↓"+path)
    fValue = fv.convertToFV(csv, plot=True, fileName=os.path.basename(path).split('.', 1)[0])
    fValueList.append(fValue)
    targetVarList.append([csv["SBP"][0], csv["DBP"][0]])
    
data = exportCSV(fValueList, targetVarList, "out0512.csv")

#data = pd.read_csv("out4.csv")
#deepL.deepL(data)



# In[ ]:





# In[ ]:



