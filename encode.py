from turtle import position
import numpy as np

def betweenParantheses(str,inting):
    i=0
    while str[i]!='(' :
        i+=1
    a=""
    i+=1
    while str[i]!=',' :
        a+=str[i]
        i+=1
    b=""
    i+=1
    while str[i]!=')' :
        b+=str[i]
        i+=1
    if inting:
        return (int(a),int(b))
    else:
        return (a,b)

def distance(indexA,indexB,coords):
    return np.sqrt((coords[indexB][0]-coords[indexA][0])**2+(coords[indexB][1]-coords[indexA][1])**2)

def encode(N,file):
    with open(file,'r') as f:
        str=f.readlines()
    vertices=[]
    coords=[]
    edges=[]
    eCount=0
    for i in range(len(str)):
        if str[i][0]=='R' :
            vertices+=['R']
            coords+=[betweenParantheses(str[i],True)]
        else :
            try:
                int(str[i][0])
                j=0
                vertice=''
                while (str[i][j]!=' ') :
                    vertice+=str[i][j]
                    j+=1
                vertices+=[vertice]
                coords+=[betweenParantheses(str[i],True)]
            except:
                None
    for i in range(len(str)):
        if str[i][0]=='E' :
            eCount=1
            a,b=betweenParantheses(str[i],False)
            aver = vertices.index(a)
            bver = vertices.index(b)
            edges+=[(aver,bver)]
            edges+=[(bver,aver)]
    if eCount==0:
        for i in range(len(vertices)):
            for j in range(len(vertices)):
                if i!=j:
                    edges+=[(i,j)]
    listAdj=[[] for i in range(len(vertices))]
    for i in range(len(vertices)):
        for j in range(len(edges)):
            if edges[j][0]==i :
                listAdj[i]+=[["R% s" % edges[j][1],distance(edges[j][0],edges[j][1],coords)]]
    return listAdj, coords

print(encode(50,"./test.txt"))




