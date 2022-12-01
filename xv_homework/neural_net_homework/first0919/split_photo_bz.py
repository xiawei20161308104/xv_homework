'''
Descripttion: 
version: 
Author: MuzhiYing
Date: 2022-09-17 14:51:51
LastEditors: MuzhiYing
LastEditTime: 2022-09-17 15:12:30
'''
from PIL import Image as imim
import os
import time
from tkinter import *
import tkinter.filedialog
from tkinter import messagebox as msgbox
def xz():
    #选择图片
    img_path=tkinter.filedialog.askopenfilename()
    #判断是否选择
    if img_path != '':
        print (img_path)#图片路径
        #分割成1行
        sd = input("拆成几行：")    # 拆分行数
        img_split_row = int(sd)      #行数
        #分割成几列
        sp=input('拆成几份：')#输入拆分列数量
        img_split_col = int(sp)
        #要保存的图片路径(保存为png图片格式)
        if os.path.dirname(img_path) == "" :
            img_path = os.getcwd()+"//"+img_path
        img_save = os.path.dirname(img_path)+"//图片分割-"+os.path.splitext(os.path.basename(img_path))[0]+"//"
        if not os.path.exists(img_save):
            os.makedirs(img_save)
        #分割图片
        img_ext_name = os.path.splitext(os.path.basename(img_path))[1]
        img_now = imim.open( img_path )
        split_size_w = int( img_now.size[0]/img_split_col )
        split_size_h = int( img_now.size[1]/img_split_row )
        for r in range(img_split_row):
            for c in range(img_split_col):
                split_area = ( split_size_w*c, r*split_size_h, split_size_w*(c+1), split_size_h*(r+1) )
                #print( (r*img_split_col+c+1) );
                img_now.crop(split_area).save(img_save+str(r*img_split_col+c+1)+img_ext_name)
                time.sleep(0.5) #等待
        #结束
        print("图片分割结束，一共"+str(img_split_row*img_split_col)+"张图片（保存在"+img_save)

    else:
         msgbox.showwarning('操作警示', '未选择文件')

root = Tk()
root.title("图片拆分")
root.geometry('300x200+100+100')
btn=Button(root,text='选择要拆分的图片',command=xz)
btn.pack()
root.mainloop()

