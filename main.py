import re
import time
import math
import numpy as np


class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right      
        
def Insert(T,newItem):
    if T == None:
        T =  BST(newItem)
    elif T.item[0] > newItem[0]:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T

def Delete(T,del_item):
    if T is not None:
        if del_item < T.item:
            T.left = Delete(T.left,del_item)
        elif del_item > T.item:
            T.right = Delete(T.right,del_item)
        else:  # del_item == T.item
            if T.left is None and T.right is None: # T is a leaf, just remove it
                T = None
            elif T.left is None: # T has one child, replace it by existing child
                T = T.right
            elif T.right is None:
                T = T.left    
            else: # T has two chldren. Replace T by its successor, delete successor
                m = Smallest(T.right)
                T.item = m.item
                T.right = Delete(T.right,m.item)
    return T
         
def InOrder(T):
    # Prints items in BST in ascending order
    if T is not None:
        InOrder(T.left)
        print(T.item,end = ' ')
        InOrder(T.right)
  
def InOrderD(T,space):
    # Prints items and structure of BST
    if T is not None:
        InOrderD(T.right,space+'   ')
        print(space,T.item)
        InOrderD(T.left,space+'   ')
  
def SmallestL(T):
    # Returns smallest item in BST. Returns None if T is None
    if T is None:
        return None
    while T.left is not None:
        T = T.left
    return T   
 
def Smallest(T):
    # Returns smallest item in BST. Error if T is None
    if T.left is None:
        return T
    else:
        return Smallest(T.left)

def Largest(T):
    if T.right is None:
        return T
    else:
        return Largest(T.right)   

def Find(T,k):
    # Returns the address of k in BST, or None if k is not in the tree
    if T is None or T.item[0] == k:
        return T.item[1]
    if T.item[0]<k:
        return Find(T.right,k)
    return Find(T.left,k)
    
def FindAndPrint(T,k):
    f = Find(T,k)
    if f is not None:
        print(f.item,'found')
    else:
        print(k,'not found')

def getNum(T):
    if T is None:
        return 0
    return 1 + getNum(T.left) + getNum(T.right)


def Height(T):
    if T is None :
        return 0
    else :
        lheight = Height(T.left)
        rheight = Height(T.right)

        if (lheight>rheight):
            return lheight +1
        else :
            return rheight +1

class HashTableC(object):
    # Builds a hash table of size 'size'
    # Item is a list of (initially empty) lists
    # Constructor
    def __init__(self,size):  
        self.item = []
        self.length = 0 
        for i in range(size):
            self.item.append([])

       
def InsertC(H,k):
    # Inserts k in appropriate bucket (list) 
    # Does nothing if k is already in the table
    b = h(k[0],len(H.item))
    H.item[b].append([k[0], np.array(k[1:]).astype(np.float)])
    H.length += 1
    return H
   
def FindC(H,k):
    # Returns bucket (b) and index (i) 
    # If k is not in table, i == -1
    b = h(k,len(H.item))
    for i in range(len(H.item[b])):
        if H.item[b][i][0] == k:
            return H.item[b][i][1]
    return -1
 
def h(s,n):
    r = 0
    for c in s:
        r = (r*n + ord(c))% n
    return r

def EmptyLists(H):
    count = 0
    for i in H.item:
        if i == []:
            count += 1
    percentage = count / len(H.item) * 100 
    return percentage            


def Binary():
    T = None
    print('Building binary search tree')
    print(' ')
    start = time.time() 
    with open('glove.6B.50d.txt', encoding='utf-8') as file_to_read:
        for i in file_to_read:
            s1 = i.split()
            T = Insert(T, [s1[0], np.array(s1[1:]).astype(float)])
    print('Binary Search Tree stats:')
    print('Number of nodes: ', getNum(T))
    print('Height: ', Height(T))
    print(' ')
    print('Running time for binary search tree construction: ', (time.time() - start))
    print(' ')
    print('Reading word file to determine similarities')
    print(' ')
    start = time.time() 
    with open('wordlist.txt', encoding='utf-8') as file_to_read_second:
        print('Word Similarities found:')
        for j in file_to_read_second:
            s2 = j.split()
            e0 = Find(T, s2[0])
            e1 = Find(T, s2[1])
            print('Similarity', s2[0:], ' = ', round(np.sum(e0 * e1) / (math.sqrt(np.sum(e0 * e0)) * math.sqrt(np.sum(e1 * e1))), 4))
    print(' ')
    print('Running time for binary search tree query processing: ',(time.time() - start))

def Hash():
    H = HashTableC(1000)
    print('Building hash table with chaining')
    print(' ')
    print('Hash table stats:')
    print('Initial table size: ', len(H.item))
    start = int(time.time())
    with open('glove.6B.50d.txt', encoding = 'utf-8') as file_to_read:
        for i in file_to_read:
            s1 = i.split()
            H = InsertC(H, s1)
    end = int(time.time())
    print('Final table size: ', len(H.item))
    print('Load factor: ', H.length / float(len(H.item)))    
    print('Percentage of empty lists: ', EmptyLists(H))
    print(' ')
    print('Running time for Hash Table construction: ', (end - start))
    print(' ')
    print('Reading word file to determine similarities')
    print(' ')
    start = int(time.time())
    with open('wordlist.txt', encoding = 'utf-8') as file_to_read_second:
        print('Word Similarities found:')
        for j in file_to_read_second:
            s2 = j.split()
            e0 = FindC(H, s2[0])
            e1 = FindC(H, s2[1])
            print('Similarity ', s2[0:], ' = ', round(np.sum(e0 * e1) / (math.sqrt(np.sum(e0 * e0)) * math.sqrt(np.sum(e1 * e1))), 4))
    end = int(time.time())
    print(' ')
    print('Running time for hash table query processing: ', (end - start))

      
print('Choose table implementation')
print('Type 1 for binary search tree or 2 for hash table with chaining ')
choice = int(input('Choice: '))
print(' ')
if choice == 1:
    Binary()
if choice == 2:
    Hash()



    

