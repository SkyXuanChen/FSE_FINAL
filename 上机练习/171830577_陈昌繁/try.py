import copy

def change(string):
    m={}
    for i in string:
        if i in m:
            m[i]=m[i]+1
        else:
            m[i]=1
    stk=""
    for i in m:
        x=str(m[i])
        if m[i]==1:
            x=""
        stk=stk+x+i
    return stk

def plus(int_1,int_2):
    if len(int_2)>len(int_1):
        temp=int_2
        int_2=int_1
        int_1=temp
    for i in range(len(int_1)-len(int_2)):
        int_2="0"+int_2
    res=[]
    jingwei=0
    for i in range(len(int_1)):
        k=int(int_1[-i-1])+int(int_2[-i-1])+int(jingwei)
        jingwei=int(k/10)
        res.append(k%10)
    if k>10:
        res.append(int(k/10))
    for r in range(len(res)):
        print(res[-r-1],end="")
    return res

def buy(stock):
    stock=stock[1:-1]
    stock=stock.split(',')
    res=[]
    for i in range(len(stock)-1):
        if int(stock[i]) <int(stock[i+1]) :
            res.append(int(stock[i+1])-int(stock[i]))
    result=0
    for r in res:
        result+=r
    return result

def num(lists):
    def convert(k):
        k= k[2:-2]
        k=k.split("],[")
        res=[]
        for i in k:
            temp=[]
            i=i.split(',')
            for j in i:
                temp.append(int(j))
            res.append(temp)
        return res
    lists=convert(lists)
    def sumOf(lis,C):
        for i in range(len(lis)):
            temp=0
            for j in range(i):
                temp+=lis[j]
            if C==temp:
                return True
        return False
    k=sum(lists[0])
    check_list=[]
    for i in range(k-1):
        check=0
        for m in range(len(lists)):
            if sumOf(lists[m],i+1):
                check+=1
        check_list.append(check)
    return k-max(check_list)

#坐标（高，宽）
def dfs(list0):
    def convert(k):
        k= k[2:-2]
        k=k.split("],[")
        res=[]
        for i in k:
            temp=[]
            i=i.split(',')
            for j in i:
                temp.append(int(j))
            res.append(temp)
        return res
    list0=convert(list0)
    height=len(list0)
    width=len(list0[0])
    def next_step(lists,l):
        next=[]
        if l[0]>0:
            if lists[l[0]-1][l[1]]==0 or lists[l[0]-1][l[1]]==2:
                next.append([l[0]-1,l[1]])
        if l[0]<height-1:
            if lists[l[0]+1][l[1]]==0 or lists[l[0]+1][l[1]]==2:
                next.append([l[0]+1,l[1]])
        if l[1]>0:
            if lists[l[0]][l[1]-1]==0 or lists[l[0]][l[1]-1]==2:
                next.append([l[0],l[1]-1])
        if l[1]<width-1:
            if lists[l[0]][l[1]+1]==0 or lists[l[0]][l[1]+1]==2:
                next.append([l[0],l[1]+1])
        return next
    
    def measure(point,lists,path):       
        path.append(point)
        lists_copy=copy.deepcopy(lists)
        lists_copy[point[0]][point[1]]=-1
        res=[]
        point_next=next_step(lists,point)
        if len(point_next)==0:
            return [path]
        for i in point_next:
            path_copy=copy.deepcopy(path)
            res.extend(measure(i,lists_copy,path_copy))

        return res
    k=[]
    count=0
    for i in range(width):
        for j in range(height):
            if list0[j][i]==0:
                count+=1
    for i in range(width):
        for j in range(height):
            if list0[j][i]==1:
                k=measure([j,i],list0,[])
    for i in k:
        j=list0[i[-1][0]][i[-1][1]]
        if len(i)==count+2 and list0[i[-1][0]][i[-1][1]]==2:
            print(i)

#第一题
def one():
    while True:
        k=input("string:")
        print(change(k))

def two():
    while True:
        int_1=input("int_1:")
        int_2=input("int_2:")
        print(plus(int_1,int_2))

def three():
    while True:
        stock=input("stock:")
        print(buy(stock))

def Four():
    while True:
        lists=input("lists:")
        print(num(lists))

def Five():
    while True:
        list0=input("lists:")
        dfs(list0)

#上面不标了，例子：
Four()
#输入[[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]


