import pandas as pd
import os 
alist = []
blist = []
title = ["姓名", "出生地", "出生日期", "死亡日期", "身高", "学历", "职业", "最高职务", "性别"]
pd.set_option("display.max_rows", None)
cur_filename = "data.csv"
#df = pd.read_csv("data.csv", encoding="utf-8")

class Info:
    def __init__(self, name, born_place, born_date, dead_date, height, edu_bg, pos, top_pos, born_rela, rela_ship, sex):
        self.name = name
        self.born_place = born_place
        self.born_date = born_date
        self.dead_date = dead_date
        self.height = height
        self.edu_bg = edu_bg
        self.pos = pos
        self.top_pos = top_pos
        self.born_rela = born_rela
        self.rela_ship = rela_ship
        self.sex = sex
        self.datas = {"姓名": name, "出生地": born_place, "出生日期":born_date, "死亡日期":dead_date,
                      "身高":height, "学历":edu_bg, "职业":pos, "最高职务":top_pos,  
                      "亲属":born_rela, "关系":rela_ship, "性别":sex}
        
    def edit(self):
        pass

    def print_info(self):
        print("{}: {}".format(self.name, self.born_place))
        pass


def add(name, born_place, born_date, dead_date, height, edu_bg, pos, top_pos, born_rela, rela_ship, sex): #将新增的信息存入list中，但还没有存入文件中
    person = Info(name, born_place, born_date, dead_date, height, edu_bg, pos, top_pos, born_rela, rela_ship, sex)
    
    add_in_list(blist, person.datas)
    print("信息添加成功")
    #return blist


def add_in_list(li, person):
    li.append(person)

def read_file():#将文件里面的信息读取出来存到list里面
    print("->已选择 读取文件")
    df = pd.read_csv(cur_filename)
    csv_to_list(df)


def csv_to_list(df):
    length = len(df)
    i = 0
    while i < length:
        tmp = Info(df.loc[i, "姓名"], df.loc[i, "出生地"], df.loc[i, "出生日期"], df.loc[i, "死亡日期"], df.loc[i, "身高"], 
                   df.loc[i, "学历"], 
                   df.loc[i, "职业"], df.loc[i, "最高职务"],df.loc[i, "亲属"], df.loc[i, "关系"], df.loc[i, "性别"])
        alist.append(tmp.datas)
        i += 1



def save_file(li):
    print("->已选择 存储文件")
    dataframe = pd.DataFrame(li)
    if os.path.exists('data.csv'):
        print("enter in ...........")
        dataframe.to_csv('data.csv',mode='a',index=False,header=False)
        return

    dataframe.to_csv(cur_filename, mode='w+', index=False)


def search_basic(p5, p6):
    print("->已选择 查询基本信息")
    func = int(p5)
    tmp = p6
    if func==3 or func == 4 or func == 5:
        tmp = int(tmp)
    result = circle(title[func - 1], tmp)
    if result == -1:
        return "您所查询的成员不存在哦"
    else:
        str0 = "您所查询的成员信息："
        str1=''
        for i in result:
            str1 += (str(alist[i])+'\n')
        return (str0+'\n'+str1)


def circle(str, tmp):
    tmp_list = []
    for i in range(len(alist)):
        if alist[i][str] == tmp:
            tmp_list.append(i)
    if len(tmp_list) != 0:
        return tmp_list
    else:
        return -1



