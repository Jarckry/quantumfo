#encoding=utf-8
#这是一个易经的启卦程序，在windows下的python3.3下创建'
#启卦要本着易的四原则，无事不占，不动不占，无疑不占.不能乱占。

def qigua():
    import random
    banyao = range(1,385)
    #获取1到384的随机数。
    fz = []
    #爻的阴阳列表
    fx = []
     
    #爻符列表
    fy = ["初","二","三","四","五","上"]
     
    #爻位列表
    fu = []
     
    #爻的阴阳列表用数字表示。
    fq = {'010': '上离', '011': '上艮', '111': '上坤',
          '110': '上震', '100': '上兑', '101': '上坎',
          '001': '上巽', '000': '上乾'}
    fp = {'111': '下坤', '110': '下震', '100': '下兑',
          '101': '下坎', '001': '下巽', '000': '下乾',
          '010': '下离', '011': '下艮'}
     
    #卦号字典，三个爻的阴阳对应的八卦。
    fa = {'101': '6', '100': '2',
          '110': '4', '111': '8',
          '000': '1', '001': '5',
          '011': '7', '010': '3'}
    # 三个爻号对应的卦序。
     
     
    #定义以上这些列表和字典，以供下面的代码使用。
    def qg():
        suiji = random.sample(banyao,1)
        jiou = suiji[0] % 2
         
        if jiou == 0:
            fx.append('  一')
            fz.append('九')
            fu.append(0)
        else:
            fx.append('  --')
            fz.append('六')
            fu.append(1)
             
     
    #定义一个函数，获取一个随机数写到上面建好的列表中.
    for i in range(0,6):
        qg()
     
    #运行6次上面的函数。得到一整卦。
     
    for j in range(0,6):
        fr = open("t.txt",'a')
        fr.write (fy[j]+fz[j]+fx[j] + "\n")
        fr.close()
     
    #组合上面列表数据写到一个文件中。
     
    for n in range(0,6):
        fl = open("fl.txt",'a')
        fl.write(str(fu[5-n]))
        fl.close()
     
     
    #从最后向前读列表数字并写到文件fl中。
     
     
     
    for an in open("fl.txt",'r'):
       print (fq[an[0:3]])
       print (fp[an[3:6]])
     
     
    #把fl文件数据分成两部分，分别用这部分去对应字典fq和fp中的值，并输出。
     
     
    for ai in open("fl.txt",'r'):
        f2 = open("f2.txt",'a')
        f2.write(str(fa[ai[0:3]]))
        f2.close()
        f2 = open("f2.txt",'a')
        f2.write(str(fa[ai[3:6]]))
        f2.close()    
     
     
     
     
    #再把地fl文件分成两部分，去对应字典fa，把数据写入文件f2.txt中。
    for al in open("f2.txt",'r'):
        ac =int(al)
         
    #读出f2.txt文件中的数据，不做操做。    
     
     
     
    def fm():
        for i in range(0,6):
            fr = open("t.txt",'r')
            print (fr.readlines()[5 - i])
            fr.close()
    #定义函数fm，把t.txt的内容从最后一行读到第一行
    fm()
    #运行这个函数。
     
     
     
     
    an = {"23":"1","00":"1","01":"2","02":"2","03":"3","04":"3","05":"3","06":"4",
          "07":"4","08":"5","09":"5","10":"6","11":"6","12":"7","13":"7","14":"8",
          "15":"8","16":"9","17":"9","18":"10","19":"11","20":"11","21":"12","22":"12"}
     
    #创建字典 an，把时间对应的参数写到字典里。
    import time
    am = (time.strftime("%H"))
    #print (time.strftime("%H"))
    #获取当前小时数
    if am in an:
        ax = an[am]
        ay = (int(ax) + ac) % 6
        print ("变爻为",int(ay))
         
    #用当前小时数对应的参数加上对应的卦数除以6取余，就是获得的变爻数。
     
    fv = fu[:]
     
    ba = fv[ay-1]
    if ba == 0:
        fv[ay-1] = 1
    else:
        fv[ay-1] = 0
     
    #复制fu列表，并把对应的变爻卦符改变。
    #print (fu)
    #print (fv)    
     
     
    for na in range(0,6):
        fi = open("fi.txt",'a')
        fi.write(str(fv[5-na]))
        fi.close()
    #把fv列表内容反向写入 fi.txt文件中。
    for ao in open("fi.txt",'r'):
       print (fq[ao[0:3]])
       print (fp[ao[3:6]])
     
    for aj in open("fi.txt",'r'):
        f3 = open("f3.txt",'a')
        f3.write(str(fa[aj[0:3]]))
        f2.close()
        f3 = open("f3.txt",'a')
        f3.write(str(fa[aj[3:6]]))
        f3.close()
     
     
     
     
     
    for aq in open("f3.txt",'r'):
        j = aq
         
     
    ff = {'74': '27', '34': '21', '88': '2', '86': '7', '33': '30',
          '84': '24', '85': '46', '82': '19', '83': '36', '54': '42',
          '21': '43', '22': '58', '23': '49', '24': '17', '25': '28',
          '26': '47', '27': '31', '28': '45', '68': '8', '73': '22',
          '58': '20', '71': '26', '77': '52', '76': '4', '75': '18',
          '38': '35', '37': '56', '36': '64', '35': '58', '52': '61',
          '55': '57', '32': '38', '57': '53', '56': '59', '87': '15',
          '72': '41', '66': '29', '15': '44', '14': '25', '17': '33',
          '16': '6', '11': '1', '13': '13', '12': '10', '81': '11',
          '18': '12', '64': '3', '65': '48', '48': '16', '67': '39',
          '61': '5', '62': '60', '63': '63', '42': '54', '43': '55',
          '41': '34', '46': '40', '47': '62', '44': '51', '45': '32',
          '51': '9', '78': '23', '31': '14', '53': '37'}
     
    #上面这个字典是把上下卦的组合号转换成卦号，这个也可以不改，这里不改京要改经文的文件名。
     
    import os
    os.remove("t.txt")
    os.remove("fl.txt")
    os.remove("f2.txt")
    os.remove("fi.txt")
    os.remove("f3.txt")
    del fu[:]
    #清除上面生成的文件和列表
     
    #u = str(ff[j]) + ".txt"
     
    #z = open(u,'r')
    #print (z.read())
    #z.close()
     
    #输出对应的文件 u 。
    return
