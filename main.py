#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os
from tkinter import * 
import tkinter.messagebox 
import tkinter.font as tkFont
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import BasicInfo as info
from Statistic import *
from Update_Delete import *
from TreeShow import *
import TreeBuild as tb
LARGE_FONT= ("Verdana", 25)

class APP(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("家谱系统")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)#side:停靠在窗口的那个位置 ，fill:填充，expand:true为扩展整个空白区
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree,PageFour,PageFive,PageSix):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")  # 四个页面的位置都是 grid(row=0, column=0), 位置重叠，只有最上面的可见
                
        self.show_frame(StartPage)
   
           
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise() # 切换
            
            
#主页面
class StartPage(tk.Frame):
    '''主页'''
    def __init__(self, parent, root):
        super().__init__(parent)
        label = tk.Label(self, text="家谱系统",font=LARGE_FONT)
        label.pack(pady=100)
        ft2=tkFont.Font(size=16)
        Button(self, text="添加成员信息",command=lambda: root.show_frame(PageOne),width=30,height=2,fg='white',bg='gray',activebackground='black',activeforeground='white').pack()
        Button(self, text="删除成员信息",command=lambda: root.show_frame(PageTwo),width=30,height=2).pack()
        Button(self, text="修改成员信息",command=lambda: root.show_frame(PageThree),width=30,height=2,fg='white',bg='gray',activebackground='black',activeforeground='white').pack()
        Button(self, text="亲戚关系查询成员信息",command=lambda: root.show_frame(PageFour),width=30,height=2).pack()
        Button(self, text="基本信息查询成员信息",command=lambda: root.show_frame(PageFive),width=30,height=2,fg='white',bg='gray',activebackground='black',activeforeground='white').pack()
        Button(self, text="统计成员信息",command=lambda: root.show_frame(PageSix),width=30,height=2).pack()
        Button(self,text='树形显示',command=self.TS, width=30,height=2,fg='white',bg='gray',activebackground='black',activeforeground='white').pack()
        Button(self, text="退出系统",command=root.destroy,width=30,height=2).pack()
            
    def TS(self):
        info.read_file()
        ft3=tkFont.Font(size=14)
        tb.buildTree(bs.alist)
        tree_search(family[0],0)
        Label(self,text='树形图已经显示在代码下方运行结果区域',font=ft3).pack(side=TOP)
        info.alist = []
        tb.family=[]
            
#添加信息
class PageOne(tk.Frame):
    def __init__(self, parent, root,font=LARGE_FONT):
        super().__init__(parent)
        label = tk.Label(self, text="添加成员信息",)
        label.pack(pady=10)
        ft3=tkFont.Font(size=14)
        ft4=tkFont.Font(size=12)
        
        Label(self,text='姓名：',font=ft3).pack(side=TOP)
        global  name
        name=StringVar()
        self.name_ety = Entry(self, width=60, textvariable=name, font=ft3, bg='Ivory')
        self.name_ety.pack(side=TOP)
        
        Label(self,text='出生地：',font=ft3).pack(side=TOP)
        global born_place
        born_place=StringVar()
        self.born_place_ety = Entry(self,width=60,textvariable=born_place,font=ft3,bg='Ivory')
        self.born_place_ety.pack(side=TOP)
        
        Label(self,text='出生日期（如：20001212）：',font=ft3).pack(side=TOP)
        global born_date
        born_date=StringVar()
        self.born_date_ety = Entry(self,width=60,textvariable=born_date,font=ft3,bg='Ivory')
        self.born_date_ety.pack(side=TOP)
        
        Label(self,text='如已过世请输入死亡日期（如：20150301），否则输入 0',font=ft3).pack(side=TOP)
        global dead_date
        dead_date=StringVar()
        self.dead_date_ety = Entry(self,width=60,textvariable=dead_date,font=ft3,bg='Ivory')
        self.dead_date_ety.pack(side=TOP)
    
        Label(self,text='身高（如：180.5）：',font=ft3).pack(side=TOP)
        global height
        height=StringVar()
        self.height_ety = Entry(self,width=60,textvariable=height,font=ft3,bg='Ivory')
        self.height_ety.pack(side=TOP)
        
        Label(self,text='学历（请填： 小学 /初中 /高中 /本科 /研究生 /博士）：',font=ft3).pack(side=TOP)
        global edu_bg
        edu_bg=StringVar()
        self.edu_bg_ety = Entry(self,width=60,textvariable=edu_bg,font=ft3,bg='Ivory')
        self.edu_bg_ety.pack(side=TOP)
        
        Label(self,text='职业：',font=ft3).pack(side=TOP)
        global pos
        pos=StringVar()
        self.pos_ety = Entry(self,width=60,textvariable=pos,font=ft3,bg='Ivory')
        self.pos_ety.pack(side=TOP)
        
        Label(self,text='最高职务：',font=ft3).pack(side=TOP)
        global top_pos
        top_pos=StringVar()
        self.top_pos_ety = Entry(self,width=60,textvariable=top_pos,font=ft3,bg='Ivory')
        self.top_pos_ety.pack(side=TOP)
        
        Label(self,text='亲属姓名（还未生成家谱首次添加成员请勿填写）：',font=ft3).pack(side=TOP)
        global born_rela
        born_rela=StringVar()
        self.born_rela_ety = Entry(self,width=60,textvariable=born_rela,font=ft3,bg='Ivory')
        self.born_rela_ety.pack(side=TOP)
        
        Label(self,text='与该亲属的关系（还未生成家谱首次添加成员请勿填写）（0.是该亲属配偶 1.是该亲属子代 ）：',wraplength = 650,font=ft3).pack(side=TOP)
        global rela_ship
        rela_ship=StringVar()
        self.rela_ship_ety = Entry(self,width=60,textvariable=rela_ship,font=ft3,bg='Ivory')
        self.rela_ship_ety.pack(side=TOP)
        
        Label(self,text='性别：',font=ft3).pack(side=TOP)
        global sex
        sex=StringVar()
        self.sex_ety = Entry(self,width=60,textvariable=sex,font=ft3,bg='Ivory')
        self.sex_ety.pack(side=TOP)
        
        
        Button(self, text="返回首页",width=8,font=ft4,command=lambda: root.show_frame(StartPage)).pack(pady=20)
        Button(self, text="确定保存",width=8,font=ft4,command=self.save).pack(side=TOP)
        


    def save(self):
        info.blist = []
        info.add(name.get(), born_place.get(), born_date.get(), dead_date.get(), height.get(), edu_bg.get(), pos.get(), top_pos.get(), born_rela.get(), rela_ship.get(), sex.get())
        info.save_file(info.blist)
        self.clean()
        tkinter.messagebox.showinfo('提示','已存储成员信息，可继续添加')


    def clean(self):
        self.name_ety.delete(0, 'end')
        self.born_place_ety.delete(0, 'end')
        self.born_date_ety.delete(0, 'end')
        self.dead_date_ety.delete(0, 'end')
        self.height_ety.delete(0, 'end')
        self.edu_bg_ety.delete(0, 'end')
        self.pos_ety.delete(0, 'end')
        self.top_pos_ety.delete(0, 'end')
        self.born_rela_ety.delete(0, 'end')
        self.rela_ship_ety.delete(0, 'end')
        self.sex_ety.delete(0, 'end')


            
            
#删除学生信息
class PageTwo(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        label = tk.Label(self, text="删除成员信息")
        label.pack(pady=10)
        ft3=tkFont.Font(size=14)
        ft4=tkFont.Font(size=12)
        
        Label(self,text='请输入你要删除的成员姓名：',font=ft3).pack(side=TOP)
        global e1
        e1=StringVar()
        self.name_ety = Entry(self,width=30,textvariable=e1,font=ft3,bg='Ivory')
        self.name_ety.pack()
        
        Button(self, text="确定删除",width=8,font=ft4,command=self.dell).pack(pady=20)
        Button(self, text="返回首页",width=8,font=ft4,command=lambda: root.show_frame(StartPage)).pack(pady=10)

    def dell(self):
        info.read_file()
        tb.buildTree(info.alist)
        ft4=tkFont.Font(size=12)
        strn = delete(e1.get())
        Label(self,text=strn,font=ft4).pack()
        info.alist = []
        tb.family=[]

    def clean(self):
        self.name_ety.delete(0, 'end')


#修改成员信息
class PageThree(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        tk.Label(self, text="修改成员信息").pack(pady=10)
        ft3=tkFont.Font(size=14)
        ft4=tkFont.Font(size=12)
        
        Label(self,text='请输入成员姓名：',font=ft3).pack(side=TOP)
        global i1
        i1=StringVar()
        self.name_ety = Entry(self,width=30,textvariable=i1,font=ft3,bg='Ivory')
        self.name_ety.pack(side=TOP)
        
        
        Label(self,text='请输入需要更改的信息编号（1.姓名 2.出生地 3.出生日期 4.死亡日期 5.身高 6.学历 7.职业 8.最高职务 9.亲属 11.性别）：',wraplength = 650,font=ft3).pack(side=TOP)
        global i2
        i2=StringVar()
        self.num_ety = Entry(self,width=30,textvariable=i2,font=ft3,bg='Ivory')
        self.num_ety.pack(side=TOP)
        
        Label(self,text='请输入新的信息（修改1-8/11请填写这里））：',font=ft3).pack(side=TOP)
        global i3
        i3=StringVar()
        self.val_ety = Entry(self,width=30,textvariable=i3,font=ft3,bg='Ivory')
        self.val_ety.pack(side=TOP)
        
        Label(self,text='修改该人的亲属（序号9）请填以下信息：',font=ft4, justify=LEFT).pack(pady=50)
        Label(self,text='请输入该亲属名字：',font=ft3, justify=LEFT).pack(side=TOP)
        global i4
        i4=StringVar()
        self.rela_name_ety= Entry(self,width=30,textvariable=i4,font=ft3,bg='Ivory')
        self.rela_name_ety.pack(side=TOP)
        
        Label(self,text='是否要修改与该亲属的关系：（1.是 2.否）',font=ft3, justify=LEFT).pack(side=TOP)
        global i5
        i5=StringVar()
        self.choice_ety = Entry(self,width=30,textvariable=i5,font=ft3,bg='Ivory')
        self.choice_ety.pack(side=TOP)
        
        Label(self,text='若要修改与该亲属关系，请输入该亲属是该成员的（0.配偶 1.父亲/母亲 ）',font=ft3).pack(side=TOP)
        global i6
        i6=StringVar()
        self.rela_ety = Entry(self,width=30,textvariable=i6,font=ft3,bg='Ivory')
        self.rela_ety.pack(side=TOP)

        Button(self, text="确定修改",width=8,font=ft4, command=self.up).pack(pady=20)
        Button(self, text="返回首页",width=8,font=ft4,command=lambda: root.show_frame(StartPage)).pack()
        
    def up(self):
        info.read_file()
        tb.buildTree(info.alist)
        ft4=tkFont.Font(size=12)
        str0 = update(i1.get(), i2.get(), i3.get(), i4.get(), i5.get(), i6.get())
        Label(self,text=str0,font=ft4).pack()
        info.alist = []
        tb.family=[]

    def clean(self):
        self.name_ety.delete(0, 'end')
        self.num_ety.delete(0, 'end')
        self.val_ety.delete(0, 'end')
        self.rela_name_ety.delete(0, 'end')
        self.choice_ety.delete(0, 'end')
        self.rela_ety.delete(0, 'end')
        
        
        
#亲戚关系查询成员信息
class PageFour(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        label = tk.Label(self, text="按照亲戚关系查询成员")
        label.pack(pady=10)
        ft3=tkFont.Font(size=14)
        ft4=tkFont.Font(size=12)
        self.signal = 0
        
        Label(self,text='请输入要查询的成员姓名：',font=ft3, justify=LEFT).pack(side=TOP)
        global p1
        p1=StringVar()
        self.name_ety = Entry(self,width=30,textvariable=p1,font=ft3,bg='Ivory')
        self.name_ety.pack(side=TOP)
        
        Label(self,text='请输入要查询的成员亲属关系：1.父代查询 2.子代查询 3.配偶查询',font=ft3, justify=LEFT).pack(side=TOP)
        global p2
        p2=StringVar()
        self.rela_ety = Entry(self,width=30,textvariable=p2,font=ft3,bg='Ivory')
        self.rela_ety.pack(side=TOP)
        
        Label(self,text='父代查询和子代查询请填以下信息（配偶查询请直接点击“确定查询”）：',font=ft4, justify=LEFT).pack(pady=40)
        Label(self,text='请输入目标查询亲属与目标成员的相隔代数：',font=ft3, justify=LEFT).pack(side=TOP)
        global p3
        p3=StringVar()
        self.num_ety = Entry(self,width=30,textvariable=p3,font=ft3,bg='Ivory')
        self.num_ety.pack(side=TOP)
        
        Label(self,text='请选择要查询亲属的性别：0.不限 1.男 2.女',font=ft3, justify=LEFT).pack(side=TOP)
        global p4
        p4=StringVar()
        self.sex_ety = Entry(self,width=30,textvariable=p4,font=ft3,bg='Ivory')
        self.sex_ety.pack(side=TOP)
        
        Button(self, text="确定查询",width=8,font=ft4, command = self.searchA).pack(pady=20)
        Button(self, text="返回首页",width=8,font=ft4,command=lambda: root.show_frame(StartPage)).pack(pady=10)
        
    def searchA(self):
        info.read_file()
        tb.buildTree(info.alist)
        ft4=tkFont.Font(size=12)
        str2 = tb.search_rela_info(p1.get(), p2.get(), p3.get(), p4.get())
        if self.signal == 0:
            self.result = Label(self,text=str2,wraplength = 1300,font=ft4)
            self.result.pack()
            self.signal = self.signal + 1
        elif self.signal > 0:
            self.deleteLabel()
            self.result = Label(self, text=str2, wraplength=1300, font=ft4)
            self.result.pack()
            self.signal = 1
        self.clean()
        info.alist = []
        tb.family=[]

    def deleteLabel(self):
        self.result.pack_forget()
        self.signal = 0

    def clean(self):
        self.name_ety.delete(0, 'end')
        self.rela_ety.delete(0, 'end')
        self.num_ety.delete(0, 'end')
        self.sex_ety.delete(0, 'end')

#基本信息查询成员
class PageFive(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        label = tk.Label(self, text="按照成员信息查询成员")
        label.pack(pady=10)
        ft3=tkFont.Font(size=14)
        ft4=tkFont.Font(size=12)
        self.signal = int(0)
        
        Label(self,text='请选择要按照成员的 1.姓名 2.出生地 3.出生日期 4.死亡日期 5.身高 6.学历 7.职业 8.最高职务 9.性别 查询',wraplength = 650,font=ft3, justify=LEFT).pack(side=TOP)
        global p5
        p5=StringVar()
        self.num_ety = Entry(self,width=30,textvariable=p5,font=ft3,bg='Ivory')
        self.num_ety.pack(side=TOP)
        
        Label(self,text='请输入带查询成员的姓名/出生地/出生日期/死亡日期/身高/学历/职业/最高职务/性别 ',font=ft3, justify=LEFT).pack(side=TOP)
        global p6
        p6=StringVar()
        self.val_ety = Entry(self,width=30,textvariable=p6,font=ft3,bg='Ivory')
        self.val_ety.pack(side=TOP)
        
        Button(self, text="确定查询",width=8,font=ft4, command = self.searchB).pack(pady=20)
        Button(self, text="返回首页",width=8,font=ft4,command=lambda: root.show_frame(StartPage)).pack(side=TOP)

        
    def searchB(self):
        info.read_file()
        ft4=tkFont.Font(size=12)
        str2 = info.search_basic(p5.get(), p6.get())
        if self.signal == 0:
            self.result = Label(self,text=str2,wraplength = 1300,font=ft4)
            self.result.pack()
            self.signal = self.signal + 1
        elif self.signal > 0:
            self.deleteLabel()
            self.result = Label(self, text=str2, wraplength=1300, font=ft4)
            self.result.pack()
            self.signal = 1
        self.clean()
        info.alist = []

    def deleteLabel(self):
        self.result.pack_forget()
        self.signal = 0

    def clean(self):
        self.num_ety.delete(0, 'end')
        self.val_ety.delete(0, 'end')
            
#统计成员信息
class PageSix(tk.Frame):

    def __init__(self, parent, root):

        super().__init__(parent)
        label = tk.Label(self, text="统计")
        label.pack(pady=10)
        ft3=tkFont.Font(size=14)
        ft4=tkFont.Font(size=12)
        Button(self, text="统计平均身高",width=16,font=ft4,command=self.averageH).pack(pady=10)     
        Button(self, text="统计平均学历",width=16,font=ft4,command=self.averageE).pack(pady=10)
        Button(self, text="统计最高学历",width=16,font=ft4,command=self.highE).pack(pady=10)
        Button(self, text="统计最低学历",width=16,font=ft4,command=self.lowE).pack(pady=10)
        Button(self, text="统计男女比例",width=16,font=ft4,command=self.p).pack(pady=10)
        Button(self, text="统计平均寿命",width=16,font=ft4,command=self.averageA).pack(pady=10)
        Button(self, text="统计家庭平均人口",width=16,font=ft4,command=self.averageP).pack(pady=10)
        Button(self, text="返回首页",width=8,font=ft4,command=lambda: root.show_frame(StartPage)).pack(pady=40)
            
    def averageH(self):
        ft4=tkFont.Font(size=12)
        str1=avg_height()
        Label(self,text=str1,font=ft4).pack()
    def averageE(self):
        ft4=tkFont.Font(size=12)
        str2=avg_edu_bg()
        Label(self,text=str2,font=ft4).pack()
    def lowE(self):
        ft4=tkFont.Font(size=12)
        str3=lowest_edu_bg()
        Label(self,text=str3,font=ft4).pack()
    def highE(self):
        ft4=tkFont.Font(size=12)
        str4=highest_edu_bg()
        Label(self,text=str4,font=ft4).pack()
    def p(self):
        ft4=tkFont.Font(size=12)
        str5=male_female()
        Label(self,text=str5,font=ft4).pack()
    def averageA(self):
        ft4=tkFont.Font(size=12)
        str6=avg_age()
        Label(self,text=str6,font=ft4).pack()
    def averageP(self):
        info.read_file()
        tb.buildTree(info.alist)
        ft4=tkFont.Font(size=12)
        str6=avg_people()
        Label(self,text=str6,font=ft4).pack()
        info.alist = []
        tb.family=[]
        
            
if __name__ == '__main__':
    app = APP()
    # 主消息循环:
    app.mainloop()
    df = pd.read_csv('data.csv')
    df


# In[ ]:




