import BasicInfo as bs
import TreeBuild as tb


def update(i1, i2, i3, i4, i5, i6):  # 江:更改操作  #桂：i1姓名 i2序号 i3新信息 i4修改亲属的名字 i5是否要修改亲属关系 i6描述新关系
    
    print("->已选择 更新成员记录")
    name = i1
    result = bs.circle("姓名", i1)
    if result == -1:
        str1 = "您所查询的成员不存在。"
        return str1
    else:
        if len(result) > 1:
            print("查询到多位成员，请输入其对应的编号以选择成员：")
            for i in result:
                print(i)
                print(bs.alist[i])
            idx = input("显示完毕，请选择：")
            idx = int(idx)
        else:
            idx = result[0]
#         print("请输入需更改的信息编号")
        func = i2
        func = int(func)
        if func == 0:
            return
        elif func == 9:
#             tmp = input("请输入要更改的亲属：")
            tmp = i4
#             j = input('是否更改与该亲属的关系（1.是 2.否）')
            j = i5
            j = int(j)
            if j == 2:
                rela_idx = bs.alist[idx]['关系']
                str1 = search_tree_idx(rela_idx,idx, name, tmp)
                return str1
            elif j == 1:
#                 rela_idx = input("请输入上述亲属为该成员的（0.配偶 1.父亲/母亲 2.儿子/女儿）：")
                rela_idx = i6
                str1 = search_tree_idx(rela_idx, idx, name, tmp)
                return str1
#         elif func == 10:
#             tmp = bs.alist[idx]['亲属']
#             E = format(tmp)
# #             rela_idx = input("请输入{}为该成员的（0.配偶 1.父亲/母亲 2.儿子/女儿）：".format(tmp))
#             rela_idx = i7
#             search_tree_idx(rela_idx, idx, name, tmp)
        else:
#             str = "请输入要更改的{}：".format(bs.title[func - 1])
#             tmp = input(str)
            tmp = i3
            bs.alist[idx][bs.title[func - 1]] = tmp
            tb.buildTree(bs.alist)
            save_file(bs.alist)
            str1 = "修改成功！"
            return str1


def find_rela(name,rela_name):
    
    if (rela_name == 'null'):
        return None
    else:
        for i in range(len(tb.family)):
            if (bs.alist[tb.family[i].idx]['姓名'] == rela_name):
                return i
    #print(rela_name)
    print("{}的相关亲属不存在。".format(name))
    return None

def search_tree_idx(rela_idx,idx,name,tmp):
    rela = find_rela(name, tmp)
    if rela != None:
        if rela_idx == 0:
            if tb.family[rela].spouse == -1:  # 不存在配偶方可修改
                bs.alist[idx]["亲属"] = tmp
                bs.alist[idx]["关系"] = rela_idx
                tb.buildTree(bs.alist)
                save_file(bs.alist)
                str1 = "修改成功！"
                return str1
            else:
                str1 = "该亲属已存在配偶"
                return str1
        else:  # 其他情况可直接修改
            bs.alist[idx]["亲属"] = tmp
            bs.alist[idx]["关系"] = rela_idx
            tb.buildTree(bs.alist)
            save_file(bs.alist)
            str1 = "修改成功！"
            return str1 


def delete(e1):#e1.姓名  
    print("->已选择 删除成员记录")
#     print("请选择操作:")
    name = e1
    result = bs.circle("姓名", name)
    if result == -1:
        str1 = "您所查询的成员不存在。"
        return str1
    else:
        if len(result) > 1:
            print("查询到多位成员，请输入其对应的编号以选择成员：")
            for i in result:
                print(i)
                print(bs.alist[i])
            idx = input("显示完毕，请选择：")
            idx = int(idx)
        else:
            idx = result[0]
        if bs.alist[idx]["性别"] == "女":   # 情况1：删除对象为女性
            del bs.alist[idx]
            save_file(bs.alist)
            tb.buildTree(bs.alist)
            str1 = "删除成功！"
            return str1
        else:
            if tb.family[idx].kids == []:
                if tb.family[idx].spouse == -1:  # 情况2：删除对象无后代，无配偶，直接删除
                    del bs.alist[idx]
                    save_file(bs.alist)
                    tb.buildTree(bs.alist)
                    str1 = "删除成功！"
                    return str1
                else:  # 情况3：删除对象无后代，有配偶，一并删除
                    del bs.alist[idx]
                    spouse = tb.family[idx].spouse
                    if spouse > idx:                      # 5.30：判断spouse在列表中的位置
                        del bs.alist[spouse - 1]
                    else:
                        del bs.alist[spouse]
                    save_file(bs.alist)
                    tb.buildTree(bs.alist)
                    str1 = "删除成功！"
                    return str1
            else:
                clist = []
                if tb.family[idx].spouse == -1:
                    if len(tb.family[idx].kids) == 1:  # 情况4：删除对象有后代，无配偶，只有一个孩子，孩子做根节点
                        search_kids_and_spouse(idx,clist)
                        del bs.alist[idx]
                        for i in range(len(clist)):
                            bs.alist.remove(clist[i])
                        str1 = save_new_file(clist, bs.alist)
                        return str1
                    else:  # 情况5：删除对象有后代，无配偶，有多个孩子，该对象做根节点
                        clist.append(bs.alist[idx])
                        search_kids_and_spouse(idx,clist)
                        for i in range(len(clist)):
                            bs.alist.remove(clist[i])
                        str1 = save_new_file(clist, bs.alist)
                        return str1
                else:  # 情况6：删除对象有后代，有配偶，配偶做根节点
                    spouse = tb.family[idx].spouse
                    search_kids_and_spouse(idx, clist)
                    del bs.alist[idx]
                    for i in range(len(clist)):
                        bs.alist.remove(clist[i])
                    str1 = save_new_file(clist, bs.alist)
                    return str1


def search_kids_and_spouse(idx,clist):
    if tb.family[idx].spouse != -1:
        spouse = tb.family[idx].spouse
        clist.append(bs.alist[spouse])
    if tb.family[idx].kids == []:
        return clist
    else:
        for i in range(len(tb.family[idx].kids)):
            kid = tb.family[idx].kids[i]
            clist.append(bs.alist[kid])
            search_kids_and_spouse(kid,clist)


def save_new_file(l1,l2):
    print("生成新家谱：")
    print(l1)
    dataframe = bs.pd.DataFrame(l1)
#     f = input("请输入新家谱名：")
    dataframe.to_csv("new_data.csv", mode='w+', index=False)
    save_file(l2)
    str1 = "删除成功！因删除对象有后代，已经生成新的家谱文件“new data.csv”"
    return str1


def save_file(li):
    print("->已选择 存储文件")
#     func = input("1.使用默认文件名存储文件 2.使用自定义文件名存储文件 0.退出功能")
#     if (func == "1"):
    dataframe = bs.pd.DataFrame(li)
    if bs.os.path.exists('data.csv'):
        print("enter in ...........")
        dataframe.to_csv('data.csv', mode='w+', index=False, header=True)
        return
    dataframe.to_csv(bs.cur_filename, mode='w+', index=False)
#     elif (func == "2"):
#         f = input("请输入要读取的文件名：")
#         filename = "{}.csv".format(f)
#         dataframe = bs.pd.DataFrame(li)
#         dataframe.to_csv(filename, mode='w+', index=False)
#     elif (func == "0"):
#         return


# bs.read_file()
# tb.buildTree(bs.alist)
# update()
# delete()
