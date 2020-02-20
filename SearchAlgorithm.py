#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 16:43:18 2020

@author: chetanrupakheti
"""

"""
Container of value and right and left children
"""
class Node:
    def __init__(self,x):
        self.val = x
        self.right = None
        self.left = None

"""
Given a root node, prints out the visited nodes
"""
class SearchAlgorithm:
    visitedDFS=[]  ### stores visited nodes for DFS 
    visitedBFS=[]  ### stores visited nodes for BFS
    q=[]    ### stores nodes in queue for BFS
        
    def dfs(self,n):
        self.visitedDFS.append(n.val)
        if n.left!=None: self.dfs(n.left)
        if n.right!=None: self.dfs(n.right)
        return

    def bfs(self,n):
        self.visitedBFS.append(n.val)
        if n.right!=None: self.q.append(n.right) 
        if n.left!=None: self.q.append(n.left)
        if len(self.q)>0:
            self.bfs(self.q.pop(0))
        else: return

if __name__=="__main__":
    n1 = Node(6) ### root
    n2 = Node(5)
    n3 = Node(4)
    n4 = Node(3)
    n5 = Node(2)
    n6 = Node(1)
    
    n1.left = n3
    n1.right = n2
    n3.left = n5
    n3.right = n4
    n5.left = n6

    algo = SearchAlgorithm()
    algo.dfs(n1)
    print "visitedDFS",algo.visitedDFS

    algo.bfs(n1)
    print "visitedBFS",algo.visitedBFS
    
    