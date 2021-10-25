"""
条形码/二维码的生成：
1.EAN-13产品条形码批量生成
2.产品服务二维码批量生成
"""
import os
import random
from pystrich.ean13 import EAN13Encoder
import qrcode
from securitycodegen import inputbox

number='1234567890'
file_EAN="barcode"
file_QR="qrcode"
url="www.mingrisoft.com/book/"

'''
1.EAN-13产品条形码批量生成
条形码可以获得商品的生产国家、生产企业、商品名称、价格等信息。EAN-13是欧洲物品编码的简写，共计13位。 
1~3位为国家代码，4~7位为企业代码，8~12位为商品代码，13位是校验码。
13位校验码计算方法：c3=3*(前12位的偶数位之和)+前12位奇数位之和；取c3的个位数；10-个位数；将得到的结果再取个位数，即为校验位
'''
def scode7():
    countryId=inputbox("\033[1;32m  请输入EN13的国家代码(3位)：\33[0m",3,3)
    while int(countryId) == 0:
        countryId=inputbox("\033[1;32m  请输入EN13的国家代码(3位)：\33[0m",3,3)
    compId=inputbox("\033[1;32m  请输入EN13的企业代码(4位)：\33[0m",3,4)
    while int(compId)==0:
        compId=inputbox("\033[1;32m  请输入EN13的企业代码(4位)：\33[0m",3,4)
    incount=inputbox("\033[1;32m  请输入要生成的条形码数量：\33[0m",1,0)
    while int(incount)==0:
        incount=inputbox("\033[1;32m  请输入要生成的条形码数量：\33[0m",1,0)
    if not os.path.exists(file_EAN):
        os.mkdir(file_EAN)          #判断保存条形码的文件是否存在，不存在则创建
    for j in range(int(incount)):    #批量生成条形码
        strone=''                    #清空保存单条条形码的变量
        for i in range(5):           #生成条形码的5位数字
            strone=strone + str(random.choice(number))
        barcode=countryId + compId + strone    #组合代码
        #计算条形码的校验位
        evensum=int(barcode[1])+int(barcode[3])+int(barcode[5])+int(barcode[7])+int(barcode[9])+int(barcode[11])
        oddsum=int(barcode[0])+int(barcode[2])+int(barcode[4])+int(barcode[6])+int(barcode[8])+int(barcode[10])
        checkbit=int((10-(evensum*3+oddsum)%10)%10)
        barcode=barcode+str(checkbit)   #组成完整的EAN13条形码的13位数字
        encoder=EAN13Encoder(barcode)
        encoder.save("barcode\\" + barcode + ".png")


'''
2.二维码批量生成
二维码是用某种特定的几何图形按一定规律在平面(二维方向上)分布的黑白相间记录数据的图形符号信息
黑色方块表示1，白色方块表示0，相应的组合表示了一系列的信息，QR码是目前使用最广的二维码
'''
def scode8():           #本函数生成固定的12位二维码
    #输入要生成的二维码数量
    incount=inputbox("\033[1;32m  请输入要生成的12位数字二维码数量：\33[0m",1,0)
    while int(incount)==0:
        incount=inputbox("\033[1;32m  请输入要生成的12位数字二维码数量：\33[0m",1,0)
    if not os.path.exists(file_QR):
        os.mkdir(file_QR)       #判断保存二维码的文件夹是否存在
    for j in range(int(incount)):
        strone=""               #清空存储单个二维码的变量
        for i in range(12):     #生成单条二维码数字
            strone=strone + str(random.choice(number))
            strone1=url + strone + ".html"
            encoder=qrcode.make(strone1)      #生成二维码
            encoder.save("qrcode\\" + strone + ".png")  #保存二维码图片到文件
