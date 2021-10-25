"""
防伪码/验证码生成：
(1)6位数字防伪验证码；(2)系列产品数字防伪码；(3)25位产品序列码/防伪码；(4)带数据分析功能的防伪码；(5)智能批量防伪码生成；(6)批量补充防伪码/验证码
"""
import os
import random
import tkinter
import tkinter.filedialog
import tkinter.messagebox
from string import digits

root = tkinter.Tk()  # 标准图形界面接口
randstr = []
number = "1234567890"
letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

'''
6位数字防伪码标签的生成：
当用户在主程序界面中输入数字"1"菜单项时，将进入"生成6位数字防伪编码(213563型)"的功能执行任务；
此时要求输入生成防伪码的数量，根据需要输入生成防伪码的数量即可；
生成后系统将提示用户生成防伪码的数量、生成文件夹位置信息等。
'''


def scode1(schoice):
    incount = inputbox("\033[1;32m 请输入您要生成防伪码的数量：\33[0m", 1, 0)
    while int(incount) == 0:  # 如果输入为字母或数字0，则要求重新输入
        incount = inputbox("\033[1;32m 请输入您要生成防伪码的数量：\33[0m", 1, 0)
    randstr.clear()  # 清空保存批量防伪码信息的变量randstr
    for j in range(int(incount)):  # 根据输入的防伪码数量循环批量生成防伪码
        randfir = ''  # 存储单条防伪码的变量
        for i in range(6):  # 循环生成单条防伪码
            randfir = randfir + random.choice(number)  # choice()可以一次产生一个随机数，产生的随机数可以重复
        randfir = randfir + "\n"
        randstr.append(randfir)
    wfile(randstr, "scode" + str(schoice) + ".txt", "", "已生成6位防伪码共计：" + str(len(randstr)), "codepath")


'''
多系列产品的防伪码生成：
在主程序界面中输入数字"2"菜单项时，将执行"生成9位系列产品数字防伪编码"的功能
如在产品系列起始编码输入中输入"235"，在系列产品数量中输入"5"，在每个系列生成数量中输入"10000",开始生成防伪码
'''


def scode2(schoice):
    ordstart = inputbox("\033[1;32m 请输入系列产品的数字起始号(3位): \33[0m", 3, 3)
    # 如果输入的系列产品起始号不是三位数字，则要求重新输入
    while int(ordstart) == 0:
        ordstart = inputbox("\033[1;32m 请输入系列产品的数字起始号(3位): \33[0m", 3, 3)
    ordcount = inputbox("\033[1;32m 请输入产品系列的数量: ", 1, 0)
    # 如果输入的产品系列数量小于1或大于9999，则要求重新输入
    while int(ordcount) < 1 or int(ordcount) > 9999:
        ordcount = inputbox("\033[1;32m 请输入产品系列的数量: ", 1, 0)
    incount = inputbox("\033[1;32m 请输入要生成的每个系列产品的防伪码数量:\33[0m ", 1, 0)
    while int(incount) == 0:
        incount = inputbox("\033[1;32m 请输入您要生成防伪码的数量:\33[0m ", 1, 0)
    randstr.clear()  # 清空保存批量防伪码信息的变量randstr
    for m in range(int(ordcount)):  # 分类产品编号
        for j in range(int(incount)):  # 产品防伪码编号
            randfir = ''
            for i in range(6):  # 生成一个不包含类别的产品防伪码
                randfir = randfir + random.choice(number)  # 每次生成一个随机因子
            # 将生成的单条防伪码添加到防伪码列表
            randstr.append(str(int(ordstart) + m) + randfir + "\n")
    # 调用函数wfile(),实现生成的防伪码在屏幕输出和文件输出
    wfile(randstr, "scode" + str(schoice) + ".txt", "", "已生成9位系列产品防伪码共计：" + str(len(randstr)), "codepath")


'''
生成25位混合产品系列号式防伪码：
混合产品系列码式防伪码，是包含字母和数字和"-"号组成的25位防伪码。
在主程序界面输入3菜单项时，将进入"生成25位混合产品系列码"的功能执行。
'''


def scode3(schoice):
    incount = inputbox("\033[1;32m  请输入要生成的25位混合产品序列号数量：\33[0m", 1, 0)
    while int(incount) == 0:
        incount = inputbox("\033[1;32m  请输入要生成的25位混合产品序列号数量：\33[0m", 1, 0)
    randstr.clear()  # 清空保存批量防伪码信息的变量
    for j in range(int(incount)):  # 按输入数量生成防伪码
        strone = ''  # 保存生成的单条防伪码，不带横线"-"，循环时清空
        for i in range(25):
            # 每次产生一个随机因子，也就是每次产生单条防伪码的一位
            strone = strone + random.choice(letter)
        # 将生成的防伪码每隔5位添加"-"
        strtwo = strone[:5] + "-" + strone[5:10] + "-" + strone[10:15] + "-" + strone[15:20] + "-" + strone[
                                                                                                     20:25] + "\n"
        randstr.append(strtwo)  # 添加防伪码到防伪码列表
    wfile(randstr, "scode" + str(schoice) + ".txt", "", "已生成25混合防伪系列码共计：" + str(len(randstr)), "codepath")


'''
生成含数据分析功能的防伪编码
主要由3位字母和6位数字编码组成：
3位字母的位置虽然是随机的，但相对位置是按照首字母对应不同地区，次字母对应产品颜色，尾字母对应产品批次的规则排列生成
用户在输入防伪码的时候，通过后台的数据分析，就可以很容易知道哪些地区卖的好，哪些颜色卖的好，卖的产品都是哪个批次的，也很容易对销售地区进行统计分析。
'''


def scode4(schoice):
    intype = inputbox("\033[1;32m 请输入数据分析编码(3位字母)：\33[0m", 2, 3)
    # 验证输入是否为3位的字母
    while not str.isalpha(intype) or len(intype) != 3:
        intype = inputbox("\033[1;32m 请输入数据分析编码(3位字母)：\33[0m", 2, 3)
    incount = inputbox("\033[1;32m 输入要生成的带数据分析功能的防伪码数量：\33[0m", 1, 0)
    # 验证输入是否是大于0的整数
    while int(incount) == 0:
        incount = inputbox("\033[1;32m 输入要生成的带数据分析功能的防伪码数量：\33[0m", 1, 0)
    ffcode(incount, intype, "", schoice)


'''
智能批量生成带数据分析功能的防伪码
'''


def scode5(schoice):
    default_dir = r"codeauto.mri"  # 设置默认打开的文件名
    # 打开文件选择对话框，指定打开的文件名称为"codeauto.aut"，扩展名为".mri",可以使用记事本打开和编辑
    file_path = tkinter.filedialog.askopenfilename(filetypes=[("Text file", "*.mri")], title=u"请选择智能批量处理文件：",
                                                   initialdir=(os.path.expanduser(default_dir)))
    with open(file_path, 'r') as rfile:
        codelist = rfile.read()
        codelist = codelist.split("\n")  # 以换行符为分隔符将读取的信息内容转换成列表
        print(codelist)
        for item in codelist:  # 按读取的信息循环生成防伪码
            codea = item.split(",")[0]  # 信息用","分割，","前面的信息存储防伪码标准信息
            codeb = item.split(",")[1]  # 信息用","分割，","后面的信息存储防伪码生成的数量
            ffcode(codeb, codea, "", schoice)


'''
实现防伪码补充生成功能
在原有防伪码的基础上补充生成防伪码，保证防伪码之间没有重复的问题出现
'''


def scode6(schoice):
    default_dir = r"abdscode5.txt"
    file_path = tkinter.filedialog.askopenfilename(title=u"请选择已经生成的防伪码文件", initialdir=(os.path.expanduser(default_dir)))
    with open(file_path, 'r') as rfile:
        codelist = rfile.read()
        codelist = codelist.split("\n")  # 以换行符为分隔符将读取的信息内容转换为列表
        codelist.remove("")  # 删除列表中的空行
        strset = codelist[0]  # 读取一行数据，以便获取原验证码的字母标志信息
        # 用maketrans()方法创建删除数字的字符映射转化表
        remove_digits = strset.maketrans("", "", digits)
        # 根据字符映射转换表删除该条防伪码中的数字，获取字母标志信息
        res_letter = strset.translate(remove_digits)
        nres_letter = list(res_letter)  # 把信息用列表变量nres_letter存储
        strarea = nres_letter[0]  # 从列表变量中取得第一个字母，即区域分析码
        strcolor = nres_letter[1]  # 从列表变量中取得第二个字母，即颜色分析码
        strver = nres_letter[2]  # 从列表变量中取得第三个字母，即版本分析码
        # 去除信息中的括号和引号
        nres_letter = strarea.replace(''''','').replace(''''', '') + strcolor.replace(
            ''''','').replace(''''', '') + strver.replace(''''','').replace(''''', '')
        card = set(codelist)  # 将原有防伪码放到集合变量card中
        # 利用tkinter的messagebox提示用户之前生成的防伪码数量
        tkinter.messagebox.showinfo("提示", "之前的防伪码共计：" + str(len(card)))
        root.withdraw()  # 关闭提示信息框
        incount = inputbox("请输入补充防伪码生成的数量：", 1, 0)
        # 最大值按输入生成数量的2倍生成新防伪码
        # 防止新生成防伪码与原有防伪码重复造成新生成的防伪码数量不够
        for j in range(int(incount) * 2):
            randfir = random.sample(number, 3)  # 随机产生3位不重复的数字
            randsec = sorted(randfir)  # 对产生的数字排序
            addcount = len(card)  # 记录集合中防伪码的总数量
            strone = ''  # 清空存储单条防伪码的变量
            for i in range(9):  # 生成9位数字防伪码
                strone = strone + random.choice(number)
            # 将三个字母按randsec变量中存储的位置值添加到数字防伪码中，并放到sim变量中
            sim = str(strone[0:int(randsec[0])]) + strarea + str(
                strone[int(randsec[0]):int(randsec[1])]) + strcolor + str(
                strone[int(randsec[1]):int(randsec[2])]) + strver + str(strone[int(randsec[2]):9]) + "\n"
            card.add(sim)  # 防伪码到集合
            # 如果添加到集合，证明生成的防伪码与原有的防伪码没有产生重复
            if len(card) > addcount:
                randstr.append(sim)  # 添加新生成的防伪码到新防伪码列表
                addcount = len(card)  # 记录新生成防伪码集合的防伪码数量
            if len(randstr) >= int(incount):  # 如果新防伪码数量达到输入的防伪码数量
                print(len(randstr))  # 输出已生成防伪码数量
                break
    wfile(randstr, nres_letter + "ncode" + str(schoice) + ".txt", nres_letter, "生成后补防伪码共计：" + str(addcount), "codeadd")


# inputbox()函数实现对输入数字、字母和位数的验证。
# 如果输入正确，则返回输入值；错误，则返回值为"0",要求用户重新输入。
def inputbox(showstr, showorder, length):  # showstr为输入提示文字；showorder为输入类型的内容；length为输入内容的位数，0表示不限制位数
    instr = input(showstr)  # 使用input函数要求用户输入信息。
    if len(instr) != 0:  # 输入数据的长度不为0
        # 分为三种验证方式：1.数字，不限位数 2.字母 3.数字且有位数要求
        if showorder == 1:  # 验证方式1，数字格式，不限位数，大于0的整数
            if str.isdigit(instr):  # 验证是否为数字
                if instr == "0":  # 验证数字是否为0，如果是要求重新输入，返回值为"0"
                    print("\033[1;31;40m 输入为零，请重新输入！\033[0m")  # 要求重新输入
                    return "0"
                else:
                    return instr  # 将输入的数据传给函数返回值
            else:  # 如果输入不是数字，要求用户重新输入，函数返回值为"0"
                print("\033[1;31;40m输入非法，请重新输入！\033[0m")  # 要求重新输入
                return "0"
        if showorder == 2:  # 验证方式2.字母格式且是指定字母
            if str.isalpha(instr):  # 判断输入是否为字母
                if len(instr) != length:  # 判断输入位数
                    print("\033[1;31;40m必须输入" + str(length) + "个字母，请重新输入！\033[0m")
                    return "0"
                else:
                    return instr
            else:
                print("\033[1,31,40m输入非法，请重新输入！\033[0m")
                return "0"
        if showorder == 3:  # 验证方式3，数字格式且输入数字位数有要求
            if str.isdigit(instr):  # 判断是否为数字
                if len(instr) != length:
                    print("\033[1;31;40m输入必须为" + str(length) + "个数字，请重新输入！\033[0m")
                    return "0"
                else:
                    return instr
            else:
                print("\033[1;31;40m输入非法，请重新输入！\033[0m")  # 要求重新输入
                return "0"
    else:
        print("\033[1;31;40m输入为空，请重新输入！\033[0m")
        return "0"


# wfile()函数主要实现读取已经生成的防伪编码信息，然后通过屏幕输出和文件输出防伪码的功能。
# 输出完成后，提示已经生成的防伪码数量和保存防伪码的文件存放路径。
def wfile(sstr, sfile, typeis, smsg,datapath):  # sstr:生成的防伪码；sfile:保存防伪码的文件名；typeis:是否显示提示框,""显示，no不显示;smsg:提示框中的内容；datapath:保存防伪码的路径
    if not os.path.exists(datapath):
        os.mkdir(datapath)  # 创建文件夹
    datafile = datapath + "\\" + sfile  # 设置保存防伪码的文件(包括路径)
    file = open(datafile, 'w')  # 打开保存防伪码的文件，如果不存在，则创建该文件
    wrlist = sstr  # 将防伪码信息赋值给wrlist
    pdata = ''  # 存储屏幕输出的防伪码信息
    #wdata = ''  # 存储保存到文本文件的防伪码信息
    for i in range(len(wrlist)):  # 按条循环读取防伪码数据
        wdata = str(wrlist[i].replace('[', '')).replace(']', '')  # 去掉字符的中括号
        wdata = wdata.replace(''''',').replace(''''', '')  # 去掉字符的引号
        file.write(str(wdata))  # 写入保存防伪码的文件
        pdata = pdata + wdata  # 将单条防伪码存储到pdata变量
    file.close()
    print("\033[1;31" + pdata + "\033[0m")  # 屏幕输出生成的防伪码信息
    if typeis != 'no':  # 是否显示信息提示框，值为"no"不显示
        tkinter.messagebox.showinfo("提示", smsg + "\n 防伪码文件存放位置：" + datafile)
        root.withdraw()  # 关闭辅助窗口


# 生成含有数据分析功能防伪编码函数：参数scount为要生成的防伪码数量；typestr为数据分析字符；
# 参数ismessage在输出完成时是否显示提示信息，为'no'不显示，为其他值显示
def ffcode(scount, typestr, ismessage, schoice):
    randstr.clear()  # 清空保存批量防伪码信息的变量
    # 按数量生成含数据分析功能防伪码
    for j in range(int(scount)):
        strarea = typestr[0].upper()  # 取得三个字母中的第一个字母，并转化为大写，区域分析码
        strcolor = typestr[1].upper()  # 取得三个字母中的第二个字母，并转化为大写，颜色分析码
        strversion = typestr[2].upper()  # 取得三个字母中的第三个字母，并转化为大写，版本分析码
        randfir = random.sample(number, 3)  # 随机抽取防伪码中的三个位置，不分先后
        randsec = sorted(randfir)  # 对抽取的位置进行排序并赋值给randsec
        letterone = ""  # 存储单条防伪码的变量
        for i in range(9):  # 生成9位数字防伪码
            letterone = letterone + random.choice(number)
            # 将3个字母按randsec中存储的位置值添加到数字防伪码中，并保存到sim变量中
        sim = str(letterone[0:int(randsec[0])]) + strarea + str(
            letterone[int(randsec[0]):int(randsec[1])]) + strcolor + str(
            letterone[int(randsec[1]):int(randsec[2])]) + strversion + str(letterone[int(randsec[2]):9]) + "\n"
        randstr.append(sim)  # 将组合生成的新防伪码添加到randstr变量
    wfile(randstr, typestr + "scode" + str(schoice) + ".txt", ismessage, "生成含数据分析功能的防伪码共计：" + str(len(randstr)),
          "codepath")
