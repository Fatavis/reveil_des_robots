from encode import *
import numpy as np
from time import sleep
from main import viewer

def strListToInt(adjacentList):
    for i in range(len(adjacentList)):
        for j in range(len(adjacentList[i])):
            adjacentList[i][j][0]=int(adjacentList[i][j][0][1::])
    return adjacentList

def intListToString(list):
    newlist=[]
    for i in range(len(list)):
        newlist+=["R%s" %list[i]]
    return newlist

# print(intListToString([1,3,8,10]))

def lowestInQ(dist,Q):
    min=np.inf
    verticeMin=-1
    for u in Q:
        if dist[u]<min:
            min=dist[u]
            verticeMin=u
    return verticeMin

# print(lowestInQ([3,7,4,1,2],[0,1,2,3,4]))
# print(lowestInQ([3,7,4,1,2],[0,2,3,4]))
# print(lowestInQ([3,7,4,1,2],[0,1,2,4]))

def removeFrom(Q,u,unique):
    newQ=[]
    for i in range(len(Q)):
        if Q[i]!=u:
            newQ+=[Q[i]]
        elif (Q[i]==u) & (unique):
            return newQ+Q[i+1::]
    return newQ

# print(removeFrom([0,1,2,3,3,5],5,False))
# print(removeFrom([0,1,2,3,3,5],3,False))
# print(removeFrom([0,1,2,3,3,5],3,True))
# print(removeFrom([0,1,2,3,3,5],0,False))

def neighbors(vertice, adjacentList):
    neighbors=[]
    for v in adjacentList[vertice]:
        neighbors+=[v[0]]
    return neighbors

# print(neighbors(2,strListToInt(encode(50,"./test.txt")[0])))

def distance(u,v,adjacentList):
    for vert in adjacentList[u]:
        if vert[0]==v:
            return vert[1]

# print(strListToInt(encode(50,"./test.txt")[0]))
# print(distance(0,2,strListToInt(encode(50,"./test.txt")[0])))

def djikstra(verticeDeb,adjacentList):
    dist=[np.inf for i in range(len(adjacentList))]
    prev=[-1 for i in range(len(adjacentList))]
    Q=[i for i in range(len(adjacentList))]
    dist[verticeDeb]=0
    while Q!=[]:
        # print("Q",Q)
        u=lowestInQ(dist,Q)
        Q=removeFrom(Q,u,False)
        for v in neighbors(u,adjacentList):
            if v in Q:
                alt = dist[u]+distance(u,v,adjacentList)
                if alt<dist[v]:
                    dist[v]=alt
                    prev[v]=u
    return dist,prev

# print(strListToInt(encode(50,"./test.txt")[0]))
# print(djikstra(0,strListToInt(encode(50,"./test.txt")[0])))

def furthestVertice(vertice,adjacentList,visitedVertices):
    max=0
    verticeMax=-1
    dist=djikstra(vertice,adjacentList)[0]
    for i in range(len(adjacentList)):
        if (i!=vertice) & (dist[i]>max) & (i not in visitedVertices):
            max=dist[i]
            verticeMax=i
    return (verticeMax,max)

# print(strListToInt(encode(50,"./test.txt")[0]))
# print(furthestVertice(0,strListToInt(encode(50,"./test.txt")[0])))

def closestVertice(vertice,adjacentList,visitedVertices):
    min=np.inf
    verticeMin=-1
    dist=djikstra(vertice,adjacentList)[0]
    for i in range(len(adjacentList)):
        if (i!=vertice) & (dist[i]<min) & (i not in visitedVertices):
            min=dist[i]
            verticeMin=i
    return (verticeMin,min)

# print(strListToInt(encode(50,"./test.txt")[0]))
# print(closestVertice(0,strListToInt(encode(50,"./test.txt")[0]),[1]))

def extractDuplicates(tab):
    firstSeen=[]
    dup=[]
    for i in range(len(tab)):
        if (tab[i] in firstSeen) & (tab[i] not in dup):
            dup+=[tab[i]]
        elif (tab[i] not in firstSeen):
            firstSeen+=[tab[i]]
        else:
            None
    return dup

# print(strListToInt(encode(50,"./test.txt")[0]))

def stackSortAscending(stack):
    # print(stack)
    newStack=[]
    length=len(stack)
    for i in range(length):
        # print(i)
        min=np.inf
        stackMin=-1
        for j in range(len(stack)):
            # print("len(stack)",len(stack))
            # print("j",j)
            if stack[j][2]<=min:
                min=stack[j][2]
                stackMin=j
        # print(newStack)
        # print(stack)
        # print(stackMin)
        newStack+=[stack[stackMin]]
        stack=removeFrom(stack,stack[stackMin],True)
    return newStack

# print(stackSortAscending([(0,1,30),(1,4,21),(2,4,13)]))

def stackMapSub(stack,e):
    # print(stack)
    for i in range(len(stack)):
        # print(stack[i][2], "-", e)
        stack[i][2]-=e
    return stack

def equalSet(set1,set2):
    if len(set1)!=len(set2):
        return False
    for i in range(len(set1)):
        if set1[i] in set2:
            set2=removeFrom(set2,set1[i],True)
    if (set2!=[]):
        return False
    return True

# print(equalSet([1,2,3,5],[3,1,2]))

def algo(adjacentList,coords):
    copyAdj=adjacentList
    adjacentList=strListToInt(adjacentList)
    # print(adjacentList)
    visitedVertices=[0]
    ongoingVertices=[]
    stack=[]
    avaliableRobots=[0]
    time=0
    memory_visited_vertices=[["R0"]]
    loopCount=0
    while ((((stack!=[]) | (avaliableRobots!=[])) | (time==0)) & (not equalSet(visitedVertices,[i for i in range(len(adjacentList))]))) :
        dup=extractDuplicates(avaliableRobots)
        print("dup",dup)
        sentClosest=[]
        for i in range(len(avaliableRobots)):
            if avaliableRobots[i] not in sentClosest :
                print("Closest")
                closest,dist = closestVertice(avaliableRobots[i],adjacentList,visitedVertices+ongoingVertices)
                if (closest==-1):
                    continue
                stack+=[[avaliableRobots[i],closest,dist]]
                ongoingVertices+=[closest]
                print("Cdist",closest,dist)
                sentClosest+=[avaliableRobots[i]]
            elif avaliableRobots[i] in dup:
                print("Furthest")
                furthest,dist = furthestVertice(avaliableRobots[i],adjacentList,visitedVertices+ongoingVertices)
                if (furthest==-1):
                    continue
                print("Fdist",furthest,dist)
                stack+=[[avaliableRobots[i],furthest,dist]]
                ongoingVertices+=[furthest]
        stack=stackSortAscending(stack)
        print("Sorted",stack)
        avaliableRobots=2*[stack[0][1]]
        print("Avaliable",avaliableRobots)
        time+=stack[0][2]
        visitedVertices+=[stack[0][1]]
        print("Visited",visitedVertices)
        ongoingVertices=removeFrom(ongoingVertices,stack[0][1],True)
        stack=stackMapSub(stack,stack[0][2])[1::]
        print('newStack',stack)
        memory_visited_vertices+=[intListToString(visitedVertices)]
        loopCount+=1
    # print(memory_visited_vertices)
    # viewer(copyAdj,coords,memory_visited_vertices)
    return time,loopCount

def travelling(verticeStart,verticeEnd,adjacentList,prev):
    travelling=[verticeEnd]
    lastVertice=verticeEnd
    while (lastVertice!=verticeStart):
        lastVertice=prev[lastVertice]
        travelling=[lastVertice]+travelling
    dist=[0]
    totalDist=0
    for i in range(len(travelling)-1):
        totalDist+=distance(travelling[i],travelling[i+1],adjacentList)
        dist+=[totalDist]
    return travelling,dist

print(travelling(3,4,strListToInt(encode(1050,"./test.txt")[0]),djikstra(3,strListToInt(encode(1050,"./test.txt")[0]))[1]))


def algoImproved(adjacentList,coords):
    copyAdj=adjacentList
    adjacentList=strListToInt(adjacentList)
    # print(adjacentList)
    visitedVertices=[0]
    ongoingVertices=[]
    stack=[]
    avaliableRobots=[0]
    time=0
    memory_visited_vertices=[["R0"]]
    loopCount=0
    while ((((stack!=[]) | (avaliableRobots!=[])) | (time==0)) & (not equalSet(visitedVertices,[i for i in range(len(adjacentList))]))) :
        dup=extractDuplicates(avaliableRobots)
        print("dup",dup)
        sentClosest=[]
        for i in range(len(avaliableRobots)):
            if avaliableRobots[i] not in sentClosest :
                print("Closest")
                closest,dist = closestVertice(avaliableRobots[i],adjacentList,visitedVertices+ongoingVertices)
                if (closest==-1):
                    continue
                stack+=[[avaliableRobots[i],closest,dist]]
                ongoingVertices+=[closest]
                print("Cdist",closest,dist)
                sentClosest+=[avaliableRobots[i]]
            elif avaliableRobots[i] in dup:
                print("Furthest")
                furthest,dist = furthestVertice(avaliableRobots[i],adjacentList,visitedVertices+ongoingVertices)
                if (furthest==-1):
                    continue
                print("Fdist",furthest,dist)
                travel,travDist=travelling(avaliableRobots[i],furthest,adjacentList,djikstra(avaliableRobots[i],adjacentList)[1])
                for j in range(len(travel)-1):
                    stack+=[[travel[j],travel[j+1],travDist[j+1]]]
                ongoingVertices+=[furthest]
        stack=stackSortAscending(stack)
        print("Sorted",stack)
        avaliableRobots=2*[stack[0][1]]
        print("Avaliable",avaliableRobots)
        time+=stack[0][2]
        if (stack[0][1] not in visitedVertices):
            visitedVertices+=[stack[0][1]]
        print("Visited",visitedVertices)
        ongoingVertices=removeFrom(ongoingVertices,stack[0][1],True)
        stack=stackMapSub(stack,stack[0][2])[1::]
        print('newStack',stack)
        memory_visited_vertices+=[intListToString(visitedVertices)]
        loopCount+=1
    print(memory_visited_vertices)
    viewer(copyAdj,coords,memory_visited_vertices)
    return time,loopCount

print(algoImproved(encode(50,"./bigtest.txt")[0],encode(50,"./bigtest.txt")[1]))
# viewer(encode(50,"./bigtest.txt")[0],encode(50,"./bigtest.txt")[1],[["R0"],["R0","R5"]])







