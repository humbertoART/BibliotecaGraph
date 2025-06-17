import pygame
from random import uniform
from Models_Graphs import grafoMalla
from math import *

"""
IMPUT: GRAPH
"""
def Spring(g):
    # g = grafoMalla(2,100)
    M = 800
    c1,c2,c3,c4 = 2,1,1,0.1
    constant = 150

    #PYGAME 
    pygame.init()
    screen = pygame.display.set_mode((1500,1500))
    # clock = pygame.time.Clock()
    running = True

    #1. Posiciones aleatorias de los vértices de G
    pos_nodes = {n: (round(uniform(700,720+constant)), round(uniform(820,820-constant))) for n in g.V}


    for k in range(M):
        screen.fill((0,0,0))

        forces = {n: [0.0,0.0] for n in g.V}
        
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
            # d = sqrt(pow((dx),2) + pow((dy),2))
            d = sqrt(dx**2+dy**2)
            # print(f'd:{d}')

            if d > 0:
                f_atraccion = c1 * log(d/c2)
                #direccion 
                fax = f_atraccion * (dx/d)
                fay = f_atraccion * (dy/d)
                forces[i][0] += fax
                forces[i][1] += fay
                forces[j][0] -= fax
                forces[j][1] -= fay            
            else:
                f_atraccion = 0


        #Fuerza ejercida por spring: c3/(sqrt(d)), donde c3 es constante
        #Vértices no conectados
        for i in g.V:
            for j in g.V:
                if i != j and (i,j) not in g.E and (j,i) not in g.E:
                    x1, y1 = pos_nodes[i]
                    x2, y2 = pos_nodes[j]   

                    dx = x2 - x1 
                    dy = y2 - y1

                    #distance
                    # d = sqrt(pow((dx),2) + pow((dy),2))
                    d = sqrt(dx**2+dy**2)

                    if d > 0:
                        f_repulsion = c3 / sqrt(max(d,0.5))
                        frx = f_repulsion * (dx/d)
                        fry = f_repulsion * (dy/d)
                        forces[i][0] -= frx
                        forces[i][1] -= fry
                        forces[j][0] += frx
                        forces[j][1] += fry                    
                    else: 
                        f_repulsion = 0

        #4. Mover el vértice c4 * (fuerza en el vértice)
        for i in g.V:
            x, y = pos_nodes[i]
            # print(f'x:{x} and y:{y}')
            fx, fy = forces[i]
            # print(f'fx:{fx} and fy:{fy}')
            new_x = x + (c4 * fx)
            new_y = y + (c4 * fy)  

            # pos_nodes[i] = max(50,min(new_x,2100)), max(50,min(new_y,2100))
            pos_nodes[i] = new_x, new_y

            
        #5. Dibujar un círculo relleno para cada vértice.
        for i in g.V:
            x, y = pos_nodes[i]
            pygame.draw.circle(screen,(0,255,0),(int(x),int(y)),3)   


        #6. Dibujar una línea recta para cada arista.
        for edge in g.E.values():
            i, j = edge.u, edge.v
        
            x1, y1 = pos_nodes[i]
            x2, y2 = pos_nodes[j]
            pygame.draw.line(screen,(255,255,255),(int(x1),int(y1)),(int(x2),int(y2)),1)        

        pygame.display.flip()
        # pygame.time.delay(1)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

