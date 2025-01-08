#1/ A function allNeg(L) which returns True if all the numbers in L are negative.
def allNeg(L):
    for i in L:
        if i>=0:
            return False
    return True
#2/ A function antiMode(L) that takes a list of numbers as input and finds the element that occurs the least.
def antiMode(L):
    adict={}
    for i in L:
        adict[i]=adict.get(i,0)+1
    for i in adict:
        if adict.get(i)==min(adict.values()):
            return i
print(antiMode([3,2,1,3,2,2,3]))
#3/ A function my cos(x,n) which computes an approximation to cos(x)
def my_cos(x,n):
    result=0
    tab=1
    for i in range(0,2*n+1,2):
        denom=1
        for k in range(1,i+1):
            denom=denom*k
        result=result+(((x**i)/denom)*tab)
        tab=tab*(-1)
    return result
#4/ A function that takes two lists as input and returns a list of elements that are common to both lists without duplicates
def check_list(a,b):
    mydict1={}
    mydict2={}
    for i in a:
        mydict1[i]=mydict1.get(i,0)+1
    for i in b:
        mydict2[i]=mydict2.get(i,0)+1
    alist=[]
    for i in mydict1:
        for k in mydict2:
            if i==k:
                alist.append(i)
    return alist
#5/ A list of tuples where each tuple consists of a name and a score, e.g., [(’Alice’, 90), (’Bob’, 78), (’Carol’, 85)], write a Python function that returns the name of the person with the highest score
def check_tuples(a):
    biggest=-99999999
    for i in range(len(a)):
        if a[i][1]>biggest:
            biggest=a[i][1]
    for i in range(len(a)):
        if a[i][1]==biggest:
            return a[i][0]
#6/ A recursive function list min(L) which returns the minimal element of a list of number L.
def list_min(L):
    if len(L)==0:
        return None
    if len(L)==1:
        return L[0]
    else:
        if L[0]>=L[1]:
            return list_min(L[1:])
        else:
            L.pop(1)
            return list_min(L)

def pizza(L):
    if len(L) == 0:
        return [[]]
    else:
        first = L[0]
        rest = L[1:]
        rest_pizzas = pizza(rest)
        result = []
        for way in rest_pizzas:
            result.append(way)
        for way in rest_pizzas:
            result.append([first] + way)
        return result
all_ways = pizza(["spinach", "olives", "mushrooms"])
print(all_ways)
