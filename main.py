"""
企业编码生成系统的主程序模块主要实现对各任务功能的选择和管理。

"""
import re
import time
from securitycodegen import *
from barorqrcodegen import *
from lottery import *


def menu():
    print('''\033[1;35m
        ****************************************************
                          企业编码生成系统
        ****************************************************
            1.生成6位数字防伪编码(213563型)
            2.生成9位系列产品数字防伪编码(879-335439型)
            3.生成25位混合产品系列号(B2R12-N7TE8-9IET2-FE350-DW2K4型)
            4.生成含数据分析功能的防伪编码(5A61M0583D2)
            5.智能批量生成带数据分析功能的防伪码
            6.后续补加生成防伪码(5A61M0583D2)
            7.EAN-13条形码批量生成
            8.二维码批量输出
            9.企业粉丝防伪码抽奖
            0.退出系统
        ****************************************************
        说明：通过数字键选择菜单
        ****************************************************
        \033[0m''')

def main():
    #通过循环控制用户对程序功能的选择
    ctrl=True
    while ctrl:
        #调入程序主界面菜单
        menu()
        #键盘输入需要操作的选项
        choice=input("\033[1;32m 请输入您要操作的菜单选项:\33[0m")
        choice_str=re.sub("\D","",choice)
        if choice_str in ['0','1','2','3','4','5','6','7','8','9']:
            choice=int(choice_str)
            if choice==1:
                scode1(str(choice))                #调用scode1()函数生成防伪码
            if choice==2:
                scode2(str(choice))                           #调用scode2()函数生成9位系列产品数字防伪编码
            if choice==3:
                scode3(str(choice))                           #调用scode3()函数生成25位混合产品序列号
            if choice==4:
                scode4(str(choice))                           #调用scode4()函数生成含有数据分析功能的防伪编码
            if choice==5:
                scode5(str(choice))                           #调用scode5()函数智能批量生成带数据分析功能的防伪码
            if choice==6:
                scode6(str(choice))                           #调用scode6()函数后续补加生成防伪码
            if choice==7:
                scode7()                           #调用scode7()函数批量生成条形码
            if choice==8:
                scode8()                           #调用scode8()函数批量生成二维码
            if choice==9:
                scode9()                           #调用scode9()函数实现企业粉丝抽奖
            if choice==0:                          #选择菜单0，退出系统
                print("正在退出系统")
                ctrl=False
        else:
            print("\033[1;31;40m  输入非法，请重新输入!! \033[0m")
            time.sleep(2)
                
main()



