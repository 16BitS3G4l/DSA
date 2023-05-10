# Implementation of Vanilla Binary Search 
import math 

def solveHelper(listToSearch=[], elementToSearch=0):
    return solve(listToSearch, elementToSearch, 0, len(listToSearch)-1) 

def solve(listToSearch=[], elementToSearch=0, start=0, end=0):
    
    midway_point = math.floor((start+end)/2)

    if(listToSearch[midway_point] == elementToSearch):
        return midway_point 
    
    elif(end == start):
        return -1 
    
    elif listToSearch[midway_point] < elementToSearch:
        return solve(listToSearch, elementToSearch, midway_point+1, end)
    
    elif listToSearch[midway_point] > elementToSearch:
        return solve(listToSearch, elementToSearch, start, midway_point-1)
    

