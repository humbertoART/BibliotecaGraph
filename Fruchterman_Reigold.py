from math import *
from random import uniform
import pygame
from Models_Graphs import grafoMalla

def fuerzaRepulsiva(k,x):
    fr = (k**2)/x
    return fr

def fuerzaAtraccion(k,x):
    fa = (x**2)/k
    return fa

def nomalizeDisp(disp):
    normal = sqrt((disp[0]**2) + (disp[1]**2))
    return normal

def cool(t,W,L):
        # permite que un nodo pueda moverse decenas de píxeles al inicio
     return t * 0.99


def FruchtermanReigold(g,W=1500,L=1500, t=0.95):
    area = W * L
    iterations = 1000
    pos_nodes = {n: (round(uniform(50,W-50)), round(uniform(50,L-50))) for n in g.V}
    k = (sqrt(area/len(g.V)))
    # k = 70
    pygame.init()
    screen = pygame.display.set_mode((W,L))
    running = True

    for i in range(iterations):
        screen.fill((0,0,0))
        disp = {n: [0,0] for n in g.V}
        
        for u in g.V:
            for v in g.V:
                if u != v:
                    x1, y1 = pos_nodes[u]
                    x2, y2 = pos_nodes[v]
                    #calculo de delta por componentes
                    dx = x2 - x1
                    dy = y2 - y1
                    d = sqrt(dx**2+dy**2)

                    if d == 0:
                        d = 0.01

                    B = [dx/d, dy/d]
                    C = fuerzaRepulsiva(k,d)

                    BC = [B[0]*C, B[1]*C]

                    disp[u][0] -= BC[0]
                    disp[u][1] -= BC[1] 

        for edge in g.E.values():
            u, v = edge.u, edge.v
            x1, y1 = pos_nodes[u]
            x2, y2 = pos_nodes[v]

            dx = x2 - x1
            dy = y2 - y1
            d = sqrt(dx**2+dy**2)

            if d == 0:
                d = 0.01

            B = [dx/d, dy/d]
            C = fuerzaAtraccion(k,d)

            BC = [B[0]*C, B[1]*C]

            disp[u][0] -= BC[0]
            disp[u][1] -= BC[1]

            disp[v][0] += BC[0]
            disp[v][1] += BC[1]

        for u in g.V:
            # v.pos ← v.pos + (v.disp/|v.disp|) ∗ min(v.disp, t);
            x, y = pos_nodes[u]
            dx, dy = disp[u]
            normalize = nomalizeDisp(disp[u]) or 0.01 #disp magnitude

            if normalize > 0:                 
                dx = dx / normalize * min(normalize,t)
                dy = dy / normalize * min(normalize,t)

                new_x = min(W, max(50,x+dx))
                new_y = min(L,max(50,y+dy))

                pos_nodes[u] = (new_x, new_y) 

        t = cool(t,W,L)

        for v in g.V:
            x, y = pos_nodes[v]
            pygame.draw.circle(screen, (0,255,0),(int(x),int(y)),3)

        for edge in g.E.values():
            u, v = edge.u, edge.v
            x1, y1 = pos_nodes[u]
            x2, y2 = pos_nodes[v]
            pygame.draw.line(screen,(255,255,255),(int(x1),int(y1)),(int(x2),int(y2)),1)

        pygame.display.flip()
        pygame.time.delay(20)
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


g = grafoMalla(8,7)
FruchtermanReigold(g)