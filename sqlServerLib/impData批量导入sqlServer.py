"""
作者：车邦赞
项目：Excel导入到数据库
日期：2020/12/9
改造：E酱
"""
import pandas as pd
import pyodbc
import win32ui
import win32con

import time

def getTime(s = ''):
    print(s + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


#获取字段名称以及字段类型
def GetColumns(data):
    l=[]
    for col in data.columns:
        if str(type(data[col].values[0])).find("float")>0:
            l.append('"{}" numeric(18,2)'.format(col))
        elif str(type(data[col].values[0])).find("int")>0:
            l.append('"{}" bigint'.format(col))
        else:
            m = max([len(str(x)) for x in data[col].values ])
            # sql server中汉字占2字节，长度需要设得更长
            m=int(m * 2 / 10) * 10 + 10
            
            l.append('"{}" varchar({})'.format(col,m))
    return ",\n".join(l)

#创建表
def createtable(conn,tablename,columns):
    cur= conn.cursor()
    cur.execute("SELECT * FROM sys.tables WHERE (name='{}' or name='{}') AND type_desc='USER_TABLE'".format(tablename.upper(),tablename))
    row=cur.fetchone()           
    
    if row:
        try:            
            cur.execute('drop table "{}"'.format(tablename))
            conn.commit() 
        except Exception as E:
            pass
        try:            
            cur.execute('drop table {}'.format(tablename))
            conn.commit() 
        except Exception as E:
            pass
    cur.close()
    
    
    r=True
    try:
        cur= conn.cursor()
        cur.execute('create table "{}"\n({})'.format(tablename,columns))
        
        conn.commit()
        cur.close()
       
    except Exception as E:
        
        cur.close()
        print(2,E)
        r=False
    return r

def opencsv(file):
    data=[]
    with open(file,"rb") as f:
        text=f.read()
        f.close()
        if text[:3]==b'\xef\xbb\xbf':
            # 如果是UTF8格式，则以UTF8格式打开
            data = pd.read_csv(file,encoding="utf8")
        else:
            # 如果是ANSI 格式，则以 GBK 格式打开
            data = pd.read_csv(file,encoding="gbk")
        
    return data
    

def impdata(conn,file,count):
        
    
    #取文件名称作为表名称
    l=file.split("\\")
    if len(l)>0:
        l=l[-1].split(".")
        tablename=l[0]
        if l[1].upper() in ["XLSX","XLS"]:
            data = pd.read_excel(file)
            getTime('finish read excel at ')
        elif l[1].upper() in ["TXT","CSV"]:
            data = opencsv(file)
        else:
             return False
    else:
        return False
    
    
    if len(data)==0:
        return False
    
    data = data.fillna("")
    
    columns=GetColumns(data)
    if createtable(conn, tablename, columns)==False:
        return False
    getTime('finish create table at ')
    cur = conn.cursor()
    result=True
    try:
        c=0
        for row in range(len(data)):
            values=["'"+str(data.iloc[row,col]) +"'" for col in range(len(data.columns))]
            columns = ",".join(['"' + col + '"' for col in data.columns])
            values = ",".join(values)
            if c%count==0:
                sql='insert into [{}]({})values({})'.format(tablename,columns,values)
            else:
                sql += ', \n({})'.format(values)
            # getTime('finish sql format at ')
            if (c+1)%count==0 or row==(len(data)-1):
                cur.execute(sql)
                conn.commit()
            c +=1
            # getTime('finish sql execute at ')
    except:
        result = False
        print(sql)
     
    cur.close()
    
    #重命名表名称 去掉双引号
    cur = conn.cursor()
    try:
        cur.execute('sp_rename "{}", {}'.format(tablename,tablename.upper()))
        conn.commit()
    except:
        cur.execute('rollback')
        conn.commit()
           
    cur.close()
    
     #重命名列名称 去掉双引号
    
    for col in  data.columns:
        
        cur = conn.cursor()
        try:
            cur.execute("sp_rename '{0}.{1}', {2}, 'column'".format(tablename.upper(),col,col.upper()))
            # cur.execute('ALTER TABLE {0} RENAME "{1}" TO {2}'.format(tablename.upper(),col,col.upper()))
            conn.commit()
        except:           
            cur.execute('rollback')
            conn.commit()  
        cur.close()
       
        
    getTime('finished at ')
    
    return result


if __name__=="__main__":
    getTime('start at ')
    openFlags = win32con.OFN_ALLOWMULTISELECT
    fspec = "Type (*.xlsx, *.xls)|*.xlsx;*.xls|Type (*.csv)|*.csv|All Files (*.*)|*.*||"
    dlg = win32ui.CreateFileDialog(1, None, None, openFlags, fspec)
    conn = pyodbc.connect("DRIVER={SQL Server};Server=localhost;Port=1433;database=test;UserName=sa;password=123456")
    if dlg.DoModal() == win32con.IDOK:
        fileList=dlg.GetPathNames()

        for i in fileList:
            
            if impdata(conn,i,100):
                
                print(i,"导入成功!")
            else:
                print(i,"导入失败!")
            
    conn.close()



