"""
本模块根据用户的信息(如购物小票、用户名、用户电话等)进行抽奖
"""
import random
import os
import tkinter.filedialog
from securitycodegen import inputbox

def scode9():
    default_dir=r"lottery.ini"
    #选择包含用户抽奖信息票号的文件，扩展名位".ini"
    file_path=tkinter.filedialog.askopenfilename(filetypes=[("Ini file","*.ini")],
        title=u"请选择包含抽奖号码的抽奖文件：",initialdir=(os.path.expanduser(default_dir)))
    with open(file_path,'r',encoding='utf-8') as rfile:
        codelist=rfile.read()
    codelist=codelist.split("\n")    #通过换行符把抽奖信息分割成抽奖列表
    incount=inputbox("\033[1;32m  请输入要生成的抽奖数量：\33[0m",1,0)
    while int(incount)==0 or len(codelist)<int(incount):
        incount=inputbox("\033[1;32m  请输入要生成的抽奖数量：\33[0m",1,0)
    strone=random.sample(codelist,int(incount))   #根据输入的中奖数量进行抽奖
    print("\033[1;35m   抽奖信息名单发布：  \33[0m")
    for i in range(int(incount)):
        #将抽奖数列的中括号去掉
        wdata=str(strone[i].replace('[','')).replace(']','')
        wdata=wdata.replace(''''','').replace(''''','')   #将抽奖数列的引号去掉
        print("\033[1;32m       " + wdata + "\33[0m")
