import pygame
from random import uniform
from Models_Graphs import grafoMalla
from math import *

"""
IMPUT: GRAPH
"""
g = grafoMalla(12,2)
M = 100
c1,c2,c3 = 2,1,1

#1. Posiciones aleatorias de los vértices de G
pos_nodes = {n: (round(uniform(1,100)), round(uniform(1,100))) for n in g.V}
print(pos_nodes)

#2. Cálculo de las fuerzas de atracción en cada vértice

#Fuerza ejercida por spring: c1 * log(d/c2), donde c2 es constante
#Vértices conectados

for edge in g.E.values():
    i, j = edge.u, edge.v
    # print(f'i:{i} and j:{j}')
    x1, y1 = pos_nodes[i] #A
    x2, y2 = pos_nodes[j] #B

    dx = x2 - x1 #A
    dy = y2 - y1 #B

    #distance
    d = sqrt(pow((dx),2) + pow((dy),2))
    print(f'd:{d}')

    if d > 0:
        f_atraccion = c1 * log(d/c2)
    else:
        f_atraccion = 0
    
    #direccion 
    fax = f_atraccion * (dx/d)
    fay = f_atraccion * (dy/d)

    print(f'fuerza:{f_atraccion}')


#Fuerza ejercida por spring: c3/(sqrt(d)), donde c3 es constante
#Vértices no conectados
print('====================================')
for i in g.V:
    for j in g.V:
        if i != j and (i,j) not in g.E and (j,i) not in g.E:
            x1, y1 = pos_nodes[i]
            x2, y2 = pos_nodes[j]   

            dx = x2 - x1 
            dy = y2 - y1

            #distance
            d = sqrt(pow((dx),2) + pow((dy),2))

            if d > 0:
                f_repulsion = c3 / sqrt(d)
            else: 
                f_repulsion = 0

            frx = f_repulsion * (dx/d)
            fry = f_repulsion * (dy/d)

            print(f'fuerza:{f_repulsion}')





    

            