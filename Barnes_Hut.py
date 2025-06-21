from QuadTree import QuadTree, Rectangle, Point
from Models_Graphs import grafoMalla
from random import uniform
from math import *
import pygame

def fuerzaRepulsiva(k,x):
    return (k**2)/x

def fuerzaAtraccion(k,x):
    return (x**2)/k

def nomalizeDisp(disp):
    return sqrt(disp[0]**2 + disp[1]**2)
    
def cool(t):
    return max(t * 0.999,0.01)

def compute_repulsion_force(node_p, pos_p, q, k):
    fx, fy = 0, 0
    dx = pos_p[0] - q.mass_center_x
    dy = pos_p[1] - q.mass_center_y

    magnitude = sqrt(dx**2 + dy** 2)
    d = sqrt(q.boundary.w * q.boundary.h)
    
    if magnitude < 0.01:
        magnitude = 0.01

    if d/magnitude < 1 or not q.divided:
        fr = fuerzaRepulsiva(k, magnitude) * q.mass
        fx += (dx/magnitude) * fr
        fy += (dy/magnitude) * fr
    else:
        for s in [q.northwest, q.northeast, q.southwest, q.southeast]:
            if s and s.mass > 0:
                fxs, fys = compute_repulsion_force(node_p, pos_p, s, k)
                fx += fxs
                fy += fys
    return fx, fy

def Barnes_Hut(g, t=50, W=1500, L=1500):
    area = 300 * 300
    k = sqrt(area/len(g.V))
    pos_nodes = {n: (round(uniform(0,W)), round(uniform(0,L))) for n in g.V}

    pygame.init()
    screen = pygame.display.set_mode((1500,1500))
    iterations = 7000
    running = True

    for i in range(iterations):
        screen.fill((0,0,0))
        disp = {n: [0,0] for n in g.V}

        #QUADTREE
        boundary = Rectangle(W/2,L/2,W,L)
        q = QuadTree(boundary)
        for i in g.V:
            x, y = pos_nodes[i]
            q.insert(Point(x,y, i))

        for i in g.V:
            x, y = pos_nodes[i]
            # print(f'x:{x} and y:{y} of {i}')
            # fx, fy = compute_repulsion_force(i, (x, y), q, k)
            fx, fy = compute_repulsion_force(i, pos_nodes[i], q, k)
            disp[i][0] += fx
            disp[i][1] += fy

        for edge in g.E.values():
            u, v = edge.u, edge.v
            x1, y1 = pos_nodes[u]
            x2, y2 = pos_nodes[v]

            dx = x2 - x1
            dy = y2 - y1
            d = sqrt(dx**2+dy**2)

            if d < 0.01:
                d = 0.01

            B = [dx/d, dy/d]
            C = fuerzaAtraccion(k,d)

            BC = [B[0]*C, B[1]*C]

            disp[u][0] += BC[0]
            disp[u][1] += BC[1]

            disp[v][0] -= BC[0]
            disp[v][1] -= BC[1]             

        for u in g.V:
            # v.pos ← v.pos + (v.disp/|v.disp|) ∗ min(v.disp, t);
            dx, dy = disp[u]
            normalize = nomalizeDisp(disp[u]) or 0.01 #disp magnitude
                            
            new_x = pos_nodes[u][0] + (dx/normalize) * min(normalize,t)
            new_y = pos_nodes[u][1] + (dy/normalize) * min(normalize,t)

            new_x = min(W-10,max(10,new_x))
            new_y = min(L-10,max(10,new_y))

            pos_nodes[u] = (new_x, new_y)   

        t *= 0.95

        for v in g.V:
            x, y = pos_nodes[v]
            pygame.draw.circle(screen, (0,255,0),(int(x),int(y)),3)

        for edge in g.E.values():
            u, v = edge.u, edge.v
            x1, y1 = pos_nodes[u]
            x2, y2 = pos_nodes[v]
            pygame.draw.line(screen,(255,255,255),(int(x1),int(y1)),(int(x2),int(y2)),1)

        pygame.display.flip()
        pygame.time.delay(10)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False