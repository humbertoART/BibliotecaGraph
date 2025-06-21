from Models_Graphs import grafoMalla, grafoErdosRenyi, grafoGilbet, grafoGeograficoSimple, grafoBarabasiAlbert, grafoDorogovtsevMendes
from Spring import Spring
from Fruchterman_Reigold import FruchtermanReigold
from Barnes_Hut import Barnes_Hut

import sys
sys.setrecursionlimit(30000)

def main():
    #PROYECTO 1: CREACIÓN DE MODELOS
    #==================================
    n1 = 50
    n2 = 200
    n3 = 500
    m = 12
    mErdos = 12
    mErdos2 = 35
    directed = False
    p = 0.5
    p2 = 0.05
    p3 = 0.01
    r1 = 0.4
    r2 = 0.15
    d1 = 2
    d2 = 3

    gMallan1 = grafoMalla(m,n1,directed)
    gMallan2 = grafoMalla(m,n2,directed)
    gMallan3 = grafoMalla(m,n3,directed)
    gMallan1.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Grafos/gMallan1.dot")

    gMallan2.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Grafos/gMallan2.dot")

    gMallan3.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Grafos/gMallan3.dot")

    gErdosn1 = grafoErdosRenyi(n1,mErdos,directed)
    gErdosn2 = grafoErdosRenyi(n2,mErdos,directed)
    gErdosn3 = grafoErdosRenyi(n3,mErdos2,directed)
    gErdosn1.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Grafos/gErdosn1.dot")

    gErdosn2.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Grafos/gErdosn2.dot")

    gErdosn3.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Grafos/gErdosn3.dot")        

    gGilbertn1 = grafoGilbet(n1,p,directed)
    gGilbertn2 = grafoGilbet(n2,p2,directed)
    gGilbertn3 = grafoGilbet(n3,p3,directed)
    gGilbertn1.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Grafos/gGilbertn1.dot")

    gGilbertn2.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Grafos/gGilbertn2.dot")

    gGilbertn3.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Grafos/gGilbertn3.dot")              

    gSimplen1 = grafoGeograficoSimple(n1,r1,directed)
    gSimplen2 = grafoGeograficoSimple(n2,r2,directed)
    gSimplen3 = grafoGeograficoSimple(n3,r2,directed)
    gSimplen1.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Grafos/gSimplen1.dot")

    gSimplen2.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Grafos/gSimplen2.dot")

    gSimplen3.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Grafos/gSimplen3.dot")            

    gBarabasin1 = grafoBarabasiAlbert(n1,d1,directed)
    gBarabasin2 = grafoBarabasiAlbert(n2,d1,directed)
    gBarabasin3 = grafoBarabasiAlbert(n3,d2,directed)
    gBarabasin1.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Grafos/gBarabasin1.dot")

    gBarabasin2.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Grafos/gBarabasin2.dot")

    gBarabasin3.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Grafos/gBarabasin3.dot")        

    gDorogovtsevn1 = grafoDorogovtsevMendes(n1,directed)
    gDorogovtsevn2 = grafoDorogovtsevMendes(n2,directed)
    gDorogovtsevn3 = grafoDorogovtsevMendes(n3,directed)
    gDorogovtsevn1.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Grafos/gDorogovtsenn1.dot") 

    gDorogovtsevn2.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Grafos/gDorogovtsenn2.dot")     

    gDorogovtsevn3.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Grafos/gDorogovtsenn3.dot")   


    #PROYECTO 2: BFS Y DFS(RECURSIVO E ITERATIVO)
    #==================================  
    n21 = 30
    n22 = 100
    n23 = 500

    #Modelo: Malla

    gMallan21 = grafoMalla(m,n21,directed)
    gMallan22 = grafoMalla(m,n22,directed)
    gMallan23 = grafoMalla(m,n23,directed)
    gMallan21.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Proyecto2/gMallan21.dot")

    gMallan22.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Proyecto2/gMallan22.dot")

    gMallan23.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Proyecto2/gMallan23.dot")

    bfs_Malla21 = gMallan21.BFS(25)
    bfs_Malla22 = gMallan22.BFS(56)
    bfs_Malla23 = gMallan23.BFS(123) 

    bfs_Malla21.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gMallan21BFS.dot")

    bfs_Malla22.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gMallan22BFS.dot")

    bfs_Malla23.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gMallan23BFS.dot") 

    dfs_iterative_Malla21 = gMallan21.DFS_I(45)
    dfs_iterative_Malla22 = gMallan22.DFS_I(85)
    dfs_iterative_Malla23 = gMallan23.DFS_I(345)

    dfs_iterative_Malla21.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gMallan21DFSI.dot")

    dfs_iterative_Malla22.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gMallan22DFSI.dot")

    dfs_iterative_Malla23.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gMallan23DFSI.dot") 

    dfs_recursive_Malla21 = gMallan21.DFS_R(95)
    dfs_recursive_Malla22 = gMallan22.DFS_R(125)
    dfs_recursive_Malla23 = gMallan23.DFS_R(800)

    dfs_recursive_Malla21.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gMallan21DFSR.dot")

    dfs_recursive_Malla22.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gMallan22DFSR.dot")

    dfs_recursive_Malla23.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gMallan23DFSR.dot")        

    #Modelo: Erdos Renyi   

    gErdosn21 = grafoErdosRenyi(n21,mErdos,directed)
    gErdosn22 = grafoErdosRenyi(n22,mErdos,directed)
    gErdosn23 = grafoErdosRenyi(n23,mErdos2,directed)
    gErdosn21.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Proyecto2/gErdosn21.dot")

    gErdosn22.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Proyecto2/gErdosn22.dot")

    gErdosn23.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Proyecto2/gErdosn23.dot")  

    bfs_Erdos21 = gErdosn21.BFS(1)
    bfs_Erdos22 = gErdosn22.BFS(67)
    bfs_Erdos23 = gErdosn23.BFS(444)

    bfs_Erdos21.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gErdos21BFS.dot")

    bfs_Erdos22.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gErdos22BFS.dot")

    bfs_Erdos23.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gErdos23BFS.dot")

    dfs_iterative_Erdos21 = gErdosn21.DFS_I(12)
    dfs_iterative_Erdos22 = gErdosn22.DFS_I(34)
    dfs_iterative_Erdos23 = gErdosn23.DFS_I(120)

    dfs_iterative_Erdos21.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gErdos21DFSI.dot") 

    dfs_iterative_Erdos22.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gErdos22DFSI.dot")

    dfs_iterative_Erdos23.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gErdos23DFSI.dot")

    dfs_recursive_Erdos21 = gErdosn21.DFS_R(22)
    dfs_recursive_Erdos22 = gErdosn22.DFS_R(55)
    dfs_recursive_Erdos23 = gErdosn23.DFS_R(245)

    dfs_recursive_Erdos21.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gErdos21DFSR.dot") 

    dfs_recursive_Erdos22.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gErdos22DFSR.dot")

    dfs_recursive_Erdos23.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gErdos23DFSR.dot")

    #Modelo: Gilbert   

    gGilbertn21 = grafoGilbet(n21,p,directed)
    gGilbertn22 = grafoGilbet(n22,p2,directed)
    gGilbertn23 = grafoGilbet(n23,p3,directed)
    gGilbertn21.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Proyecto2/gGilbertn21.dot")

    gGilbertn22.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Proyecto2/gGilbertn22.dot")

    gGilbertn23.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Proyecto2/gGilbertn23.dot")   

    bfs_Gilbert21 = gGilbertn21.BFS(0)
    bfs_Gilbert22 = gGilbertn22.BFS(69)
    bfs_Gilbert23 = gGilbertn23.BFS(333)

    bfs_Gilbert21.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gGilbert21BFS.dot")

    bfs_Gilbert22.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gGilbert22BFS.dot")

    bfs_Gilbert23.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gGilbert23BFS.dot")

    dfs_iterative_Gilbert21 = gGilbertn21.DFS_I(5)
    dfs_iterative_Gilbert22 = gGilbertn22.DFS_I(22)
    dfs_iterative_Gilbert23 = gGilbertn23.DFS_I(455)

    dfs_iterative_Gilbert21.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gGilbert21DFSI.dot")

    dfs_iterative_Gilbert22.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gGilbert22DFSI.dot")

    dfs_iterative_Gilbert23.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gGilbert23DFSI.dot")

    dfs_recursive_Gilbert21 = gGilbertn21.DFS_R(5)
    dfs_recursive_Gilbert22 = gGilbertn22.DFS_R(88)
    dfs_recursive_Gilbert23 = gGilbertn23.DFS_R(0)

    dfs_recursive_Gilbert21.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gGilbert21DFSR.dot") 

    dfs_recursive_Gilbert22.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gGilbert22DFSR.dot")   

    dfs_recursive_Gilbert23.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gGilbert23DFSR.dot")     

    #Modelo: Geografico Simple           

    gSimplen21 = grafoGeograficoSimple(n21,r1,directed)
    gSimplen22 = grafoGeograficoSimple(n22,r2,directed)
    gSimplen23 = grafoGeograficoSimple(n23,r2,directed)
    gSimplen21.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Proyecto2/gSimplen21.dot")

    gSimplen22.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Proyecto2/gSimplen22.dot")

    gSimplen23.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Proyecto2/gSimplen23.dot")  

    bfs_Simple21 = gSimplen21.BFS(15)
    bfs_Simple22 = gSimplen22.BFS(26)
    bfs_Simple23 = gSimplen23.BFS(77)

    bfs_Simple21.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gSimple21BFS.dot")

    bfs_Simple22.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gSimple22BFS.dot")

    bfs_Simple23.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gSimple23BFS.dot")

    dfs_iterative_Simple21 = gSimplen21.DFS_I(14)
    dfs_iterative_Simple22 = gSimplen22.DFS_I(88)
    dfs_iterative_Simple23 = gSimplen23.DFS_I(111)

    dfs_iterative_Simple21.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gSimple21DFSI.dot")

    dfs_iterative_Simple22.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gSimple22DFSI.dot")

    dfs_iterative_Simple23.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gSimple23DFSI.dot")

    dfs_recursive_Simple21 = gSimplen21.DFS_R(0)
    dfs_recursive_Simple22 = gSimplen22.DFS_R(6)
    dfs_recursive_Simple23 = gSimplen23.DFS_R(12)

    dfs_recursive_Simple21.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gSimple21DFSR.dot")

    dfs_recursive_Simple22.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gSimple22DFSR.dot")

    dfs_recursive_Simple23.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gSimple23DFSR.dot")

    #Modelo Barabasi Albert
              
    gBarabasin21 = grafoBarabasiAlbert(n21,d1,directed)
    gBarabasin22 = grafoBarabasiAlbert(n22,d1,directed)
    gBarabasin23 = grafoBarabasiAlbert(n23,d2,directed)
    gBarabasin21.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Proyecto2/gBarabasin21.dot")

    gBarabasin22.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Proyecto2/gBarabasin22.dot")

    gBarabasin23.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Proyecto2/gBarabasin23.dot") 

    bfs_Barabasi21 = gBarabasin21.BFS(2)
    bfs_Barabasi22 = gBarabasin22.BFS(11)
    bfs_Barabasi23 = gBarabasin23.BFS(444)

    bfs_Barabasi21.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gBarabasi21BFS.dot")

    bfs_Barabasi22.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gBarabasi22BFS.dot")

    bfs_Barabasi23.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gBarabasi23BFS.dot")

    dfs_iterative_Barabasi21 = gBarabasin21.DFS_I(3)
    dfs_iterative_Barabasi22 = gBarabasin22.DFS_I(22)
    dfs_iterative_Barabasi23 = gBarabasin23.DFS_I(333)

    dfs_iterative_Barabasi21.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gBarabasi21DFSI.dot")

    dfs_iterative_Barabasi22.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gBarabasi22DFSI.dot")

    dfs_iterative_Barabasi23.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gBarabasi23DFSI.dot")

    dfs_recursive_Barabasi21 = gBarabasin21.DFS_R(4)
    dfs_recursive_Barabasi22 = gBarabasin22.DFS_R(71)
    dfs_recursive_Barabasi23 = gBarabasin23.DFS_R(321)

    dfs_recursive_Barabasi21.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gBarabasi21DFSR.dot")

    dfs_recursive_Barabasi22.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gBarabasi22DFSR.dot")

    dfs_recursive_Barabasi23.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gBarabasi23DFSR.dot")

    #Modelo Dorogovtsev       

    gDorogovtsevn21 = grafoDorogovtsevMendes(n21,directed)
    gDorogovtsevn22 = grafoDorogovtsevMendes(n22,directed)
    gDorogovtsevn23 = grafoDorogovtsevMendes(n23,directed)
    gDorogovtsevn21.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Proyecto2/gDorogovtsenn21.dot") 

    gDorogovtsevn22.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Proyecto2/gDorogovtsenn22.dot")     

    gDorogovtsevn23.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Proyecto2/gDorogovtsenn23.dot") 

    bfs_Dorogovtsev21 = gDorogovtsevn21.BFS(0)
    bfs_Dorogovtsev22 = gDorogovtsevn22.BFS(0)
    bfs_Dorogovtsev23 = gDorogovtsevn23.BFS(0)

    bfs_Dorogovtsev21.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gDorogovtsev21BFS.dot")

    bfs_Dorogovtsev22.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gDorogovtsev22BFS.dot")

    bfs_Dorogovtsev23.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gDorogovtsev23BFS.dot")

    dfs_iterative_Dorogovtsev21 = gDorogovtsevn21.DFS_I(0)
    dfs_iterative_Dorogovtsev22 = gDorogovtsevn22.DFS_I(0)
    dfs_iterative_Dorogovtsev23 = gDorogovtsevn23.DFS_I(0)

    dfs_iterative_Dorogovtsev21.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gDorogovtsev21DFSI.dot")

    dfs_iterative_Dorogovtsev22.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gDorogovtsev22DFSI.dot")

    dfs_iterative_Dorogovtsev23.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gDorogovtsev23DFSI.dot")

    dfs_recursive_Dorogovtsev21 = gDorogovtsevn21.DFS_R(0)
    dfs_recursive_Dorogovtsev22 = gDorogovtsevn22.DFS_R(0)
    dfs_recursive_Dorogovtsev23 = gDorogovtsevn23.DFS_R(0)

    dfs_recursive_Dorogovtsev21.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gDorogovtsev21DFSR.dot")

    dfs_recursive_Dorogovtsev22.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gDorogovtsev22DFSR.dot")

    dfs_recursive_Dorogovtsev23.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_DFS_BFS/gDorogovtsev23DFSR.dot")

    #####################################################################
    ####################################################################

    #Proyecto 3: Dijkstra
    n31 = 30
    n32 = 500

    #MODELO MALLA

    gMallan31 = grafoMalla(m,n31,directed)
    gMallan32 = grafoMalla(m,n32,directed)

    gMallan31.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Proyecto3/gMallan31.dot")

    gMallan32.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Proyecto3/gMallan32.dot")

    dijMalla31, distMalla31 = gMallan31.Dijkstra(3)
    dijMalla32, distMalla32 = gMallan32.Dijkstra(3)

    dijMalla31.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Dijkstra/DijMalla31.dot", distance=distMalla31)

    dijMalla32.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Dijkstra/DijMalla32.dot", distance=distMalla32)

    #MODELO ERDOS RENYI

    gErdosn31 = grafoErdosRenyi(n31,mErdos,directed)
    gErdosn32 = grafoErdosRenyi(n32,mErdos2,directed)

    gErdosn31.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Proyecto3/gErdosn31.dot")
    
    gErdosn32.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Proyecto3/gErdosn32.dot")

    dijErdosn31, distErdos31 = gErdosn31.Dijkstra(6)
    dijErdosn32, distErdos32 = gErdosn32.Dijkstra(6)

    dijErdosn31.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Dijkstra/DijErdos31.dot", distance=distErdos31)

    dijErdosn32.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Dijkstra/DijErdos32.dot", distance=distErdos32)

    #MODELO GILBERT
    gGilbertn31 = grafoGilbet(n31,p,directed)
    gGilbertn32 = grafoGilbet(n32,p3,directed)

    gGilbertn31.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Proyecto3/gGilbertn31.dot")

    gGilbertn32.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Proyecto3/gGilbertn32.dot")

    dijGilbertn31, distGilbert31 = gGilbertn31.Dijkstra(4)
    dijGilbertn32, distGilbert32 = gGilbertn32.Dijkstra(4)

    dijGilbertn31.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Dijkstra/DijGilbert31.dot", distance=distGilbert31)

    dijGilbertn32.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Dijkstra/DijGilbert32.dot", distance=distGilbert32)

    #MODELO GEOGRAFICO SIMPLE
    gSimplen31 = grafoGeograficoSimple(n31,r1,directed)
    gSimplen32 = grafoGeograficoSimple(n32,r2,directed)

    gSimplen31.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Proyecto3/gSimplen31.dot")

    gSimplen32.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Proyecto3/gSimplen32.dot")

    dijSimplen31, distSimple31 = gSimplen31.Dijkstra(7)
    dijSimplen32, distSimple32 = gSimplen32.Dijkstra(7)

    dijSimplen31.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Dijkstra/DijSimple31.dot", distance=distSimple31)

    dijSimplen32.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Dijkstra/DijSimple32.dot", distance=distSimple32)

    #MODELO BARABASI ALBERT
    gBarabasin31 = grafoBarabasiAlbert(n31,d1,directed)
    gBarabasin32 = grafoBarabasiAlbert(n32,d2,directed)

    gBarabasin31.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Proyecto3/gBarabasin31.dot")

    gBarabasin32.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Proyecto3/gBarabasin32.dot")

    dijBarabasin31, distBarabasi31 = gBarabasin31.Dijkstra(9)
    dijBarabasin32, distBarabasi32 = gBarabasin32.Dijkstra(9)

    dijBarabasin31.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Dijkstra/DijBarabasi31.dot", distance=distBarabasi31)

    dijBarabasin32.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Dijkstra/DijBarabasi32.dot", distance=distBarabasi32)

    #MODELO DOROGOVTSEV
    gDorogovtsevn31 = grafoDorogovtsevMendes(n31,directed)
    gDorogovtsevn32 = grafoDorogovtsevMendes(n32,directed)

    gDorogovtsevn31.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Proyecto3/gDorogovtsev31.dot")

    gDorogovtsevn32.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Proyecto3/gDorogovtsev32.dot")

    dijDorogovtsev31, distDorogovtsev31 = gDorogovtsevn31.Dijkstra(0)
    dijDorogovtsev32, distDorogovtsev32 = gDorogovtsevn32.Dijkstra(2)

    dijDorogovtsev31.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Dijkstra/DijDorogovtsev31.dot", distance=distDorogovtsev31)

    dijDorogovtsev32.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Dijkstra/DijDorogovtsev32.dot", distance=distDorogovtsev32)

    #####################################################################
    ####################################################################

    #Proyecto 4: Kruskal Directo e Inverso y Prim

    n41 = 30
    nMall42 = 200
    nGilbert42 = 200
    nSimple42 = 200
    n42 = 500
    m40 = 2

    mErdos41 = 50
    mErdos42 = 550

    #Modelo Malla 

    gMallan41 = grafoMalla(m40,n41,directed)
    gMallan42 = grafoMalla(m40,nMall42,directed)

    gMallan41.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Proyecto4/gMallan41.dot")

    gMallan42.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Proyecto4/gMallan42.dot") 

    print(f'Modelo Malla: {n41} nodos')
    KDMalla41 = gMallan41.KruskalD()
    KIMalla41 = gMallan41.KruskalI()
    PrimMalla41 = gMallan41.Prim() 

    print(f'Modelo Malla: {nMall42} nodos')

    KDMalla42 = gMallan42.KruskalD()
    KIMalla42 = gMallan42.KruskalI()
    PrimMalla42 = gMallan42.Prim()   

    KDMalla41.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Kruskal_Prim/gKDMalla41.dot") 

    KIMalla41.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Kruskal_Prim/gKIMalla41.dot") 

    PrimMalla41.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Kruskal_Prim/gPrimMalla41.dot")  

    KDMalla42.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Kruskal_Prim/gKDMalla42.dot") 

    KIMalla42.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Kruskal_Prim/gKIMalla42.dot") 

    PrimMalla42.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Kruskal_Prim/gPrimMalla42.dot")   

    #MODELO ERDOS RENYI

    gErdosn41 = grafoErdosRenyi(n41,mErdos41,directed)
    gErdosn42 = grafoErdosRenyi(n42,mErdos42,directed)    

    gErdosn41.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Proyecto4/gErdosn41.dot")

    gErdosn42.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Proyecto4/gErdosn42.dot")    

    print(f'Modelo Erdos Renyi: {n41} nodos')
    KDErdos41 = gErdosn41.KruskalD()
    KIErdos41 = gErdosn41.KruskalI()
    PrimErdos41 = gErdosn41.Prim() 

    print(f'Modelo Erdos Renyi: {n42} nodos')
    KDErdos42 = gErdosn42.KruskalD()
    KIErdos42 = gErdosn42.KruskalI()
    PrimErdos42 = gErdosn42.Prim()

    KDErdos41.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Kruskal_Prim/gKDErdos41.dot") 

    KIErdos41.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Kruskal_Prim/gKIErdos41.dot") 

    PrimErdos41.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Kruskal_Prim/gPrimErdos41.dot")  

    KDErdos42.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Kruskal_Prim/gKDErdos42.dot") 

    KIErdos42.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Kruskal_Prim/gKIErdos42.dot") 

    PrimErdos42.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Kruskal_Prim/gPrimErdos42.dot") 

    #MODELO GILBERT  

    gGilbertn41 = grafoGilbet(n41,p,directed)
    gGilbertn42 = grafoGilbet(nGilbert42,p3,directed)     

    gGilbertn41.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Proyecto4/gGilbertn41.dot")

    gGilbertn42.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Proyecto4/gGilbertn42.dot")
    
    print(f'Modelo Gilbert: {n41} nodos')
    KDGilbert41 = gGilbertn41.KruskalD()
    KIGilbert41 = gGilbertn41.KruskalI()
    PrimGilbert41 = gGilbertn41.Prim() 

    print(f'Modelo Gilbert: {nGilbert42} nodos')
    KDGilbert42 = gGilbertn42.KruskalD()
    KIGilbert42 = gGilbertn42.KruskalI()
    PrimGilbert42 = gGilbertn42.Prim()    

    KDGilbert41.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Kruskal_Prim/gKDGilbert41.dot") 

    KIGilbert41.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Kruskal_Prim/gKIGilbert41.dot") 

    PrimGilbert41.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Kruskal_Prim/gPrimGilbert41.dot")  

    KDGilbert42.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Kruskal_Prim/gKDGilbert42.dot") 

    KIGilbert42.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Kruskal_Prim/gKIGilbert42.dot") 

    PrimGilbert42.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Kruskal_Prim/gPrimGilbert42.dot")  

    #MODELO GEOGRAFICO SIMPLE

    gSimplen41 = grafoGeograficoSimple(n41,r1,directed)
    gSimplen42 = grafoGeograficoSimple(nSimple42,r2,directed)  
    
    gSimplen41.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Proyecto4/gSimplen41.dot")

    gSimplen42.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Proyecto4/gSimplen42.dot") 

    print(f'Modelo Geografico Simple: {n41} nodos')
    KDSimple41 = gSimplen41.KruskalD()
    KISimple41 = gSimplen41.KruskalI()
    PrimSimple41 = gSimplen41.Prim() 

    print(f'Modelo Geografico Simple: {nSimple42} nodos')
    KDSimple42 = gSimplen42.KruskalD()
    KISimple42 = gSimplen42.KruskalI()
    PrimSimple42 = gSimplen42.Prim() 

    KDSimple41.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Kruskal_Prim/gKDSimple41.dot") 

    KISimple41.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Kruskal_Prim/gKISimple41.dot") 

    PrimSimple41.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Kruskal_Prim/gPrimSimple41.dot")  

    KDSimple42.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Kruskal_Prim/gKDSimple42.dot") 

    KISimple42.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Kruskal_Prim/gKISimple42.dot") 

    PrimSimple42.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Kruskal_Prim/gPrimSimple42.dot")  

    #MODELO BARABASI ALBERT

    gBarabasin41 = grafoBarabasiAlbert(n41,d1,directed)
    gBarabasin42 = grafoBarabasiAlbert(n42,d2,directed)     

    gBarabasin41.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Proyecto4/gBarabasin41.dot")

    gBarabasin42.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Proyecto4/gBarabasin42.dot") 

    print(f'Modelo Barabasi Albert: {n41} nodos')
    KDBarabasi41 = gBarabasin41.KruskalD()
    KIBarabasi41 = gBarabasin41.KruskalI()
    PrimBarabasi41 = gBarabasin41.Prim() 

    print(f'Modelo Barabasi Albert: {n42} nodos')
    KDBarabasi42 = gBarabasin42.KruskalD()
    KIBarabasi42 = gBarabasin42.KruskalI()
    PrimBarabasi42 = gBarabasin42.Prim()       

    KDBarabasi41.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Kruskal_Prim/gKDBarabasi41.dot") 

    KIBarabasi41.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Kruskal_Prim/gKIBarabasi41.dot") 

    PrimBarabasi41.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Kruskal_Prim/gPrimBarabasi41.dot")  

    KDBarabasi42.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Kruskal_Prim/gKDBarabasi42.dot") 

    KIBarabasi42.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Kruskal_Prim/gKIBarabasi42.dot") 

    PrimBarabasi42.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Kruskal_Prim/gPrimBarabasi42.dot") 

    #MODELO DOROGOVTSEV

    gDorogovtsevn41 = grafoDorogovtsevMendes(n41,directed)
    gDorogovtsevn42 = grafoDorogovtsevMendes(n42,directed) 

    gDorogovtsevn41.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Proyecto4/gDorogovtsevn41.dot")

    gDorogovtsevn42.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Proyecto4/gDorogovtsevn42.dot")   

    print(f'Modelo Dorogovtsev: {n41} nodos')
    KDDorogovtsev41 = gDorogovtsevn41.KruskalD()
    KIDorogovtsev41 = gDorogovtsevn41.KruskalI()
    PrimDorogovtsev41 = gDorogovtsevn41.Prim() 

    print(f'Modelo Dorogovtsev: {n42} nodos')
    KDDorogovtsev42 = gDorogovtsevn42.KruskalD()
    KIDorogovtsev42 = gDorogovtsevn42.KruskalI()
    PrimDorogovtsev42 = gDorogovtsevn42.Prim()    

    KDDorogovtsev41.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Kruskal_Prim/gKDDorogovtsev41.dot") 

    KIDorogovtsev41.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Kruskal_Prim/gKIDorogovtsev41.dot") 

    PrimDorogovtsev41.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Kruskal_Prim/gPrimDorogovtsev41.dot")  

    KDDorogovtsev42.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Kruskal_Prim/gKDDorogovtsev42.dot") 

    KIDorogovtsev42.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Kruskal_Prim/gKIDorogovtsev42.dot") 

    PrimDorogovtsev42.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Kruskal_Prim/gPrimDorogovtsev42.dot")                             

    ########################################################################
    #PROYECTO 5

    #Modelo Malla
    gMallan30 = grafoMalla(3,30)
    gMallan100 = grafoMalla(2,100)
    gMallan500 = grafoMalla(2,500)
    Spring(gMallan30)
    Spring(gMallan100)
    Spring(gMallan500)

    #Modelo Erdos Renyi
    gErdosn100 = grafoErdosRenyi(100,289)
    gErdosn500 = grafoErdosRenyi(500,2500)
    Spring(gErdosn100)
    Spring(gErdosn500)

    #Modelo Gilbert
    gGilbertn100 = grafoGilbet(100,0.5)
    gGilbertn500 = grafoGilbet(500,0.02)
    Spring(gGilbertn100)
    Spring(gGilbertn500)

    #Modelo Geográfico Simple
    gSimplen100 = grafoGeograficoSimple(100,0.25,directed)
    gSimplen500 = grafoGeograficoSimple(500,0.1,directed)
    Spring(gSimplen100)
    Spring(gSimplen500)

    #Modelo Barabasi Albert
    gBarabasin100 = grafoBarabasiAlbert(100,10,directed)
    gBarabasin500 = grafoBarabasiAlbert(500,15,directed)
    Spring(gBarabasin100)
    Spring(gBarabasin500)

    #Modelo Dorogovtsev Mendes
    gDorogovtsevn100 = grafoDorogovtsevMendes(100,directed)
    gDorogovtsevn500 = grafoDorogovtsevMendes(500,directed) 
    Spring(gDorogovtsevn100)
    Spring(gDorogovtsevn500)

    ########################################################################
    #PROYECTO 6

    #Modelo Malla
    gMallan9= grafoMalla(9,9,directed) 
    gMallan100 = grafoMalla(2,100)
    gMallan500 = grafoMalla(2,500)
    FruchtermanReigold(gMallan9)
    FruchtermanReigold(gMallan100)
    FruchtermanReigold(gMallan500)

    #Modelo Erdos Renyi
    gErdosn100 = grafoErdosRenyi(100,289)
    gErdosn500 = grafoErdosRenyi(500,2500)
    FruchtermanReigold(gErdosn100)
    FruchtermanReigold(gErdosn500)

    #Modelo Gilbert
    gGilbertn100 = grafoGilbet(100,0.5)
    gGilbertn500 = grafoGilbet(500,0.02)
    FruchtermanReigold(gGilbertn100)
    FruchtermanReigold(gGilbertn500)

    #Modelo Geográfico Simple
    gSimplen100 = grafoGeograficoSimple(100,0.25,directed)
    gSimplen500 = grafoGeograficoSimple(500,0.1,directed)
    FruchtermanReigold(gSimplen100)
    FruchtermanReigold(gSimplen500)

    #Modelo Barabasi Albert
    gBarabasin100 = grafoBarabasiAlbert(100,10,directed)
    gBarabasin500 = grafoBarabasiAlbert(500,15,directed)
    FruchtermanReigold(gBarabasin100)
    FruchtermanReigold(gBarabasin500)

    #Modelo Dorogovtsev Mendes
    gDorogovtsevn100 = grafoDorogovtsevMendes(100,directed)
    gDorogovtsevn500 = grafoDorogovtsevMendes(500,directed) 
    FruchtermanReigold(gDorogovtsevn100)
    FruchtermanReigold(gDorogovtsevn500)

    #######################################################################
    # PROYECTO 7

    # Modelo Malla
    gMallan9= grafoMalla(9,9,directed) 
    gMallan100 = grafoMalla(3,100)
    gMallan500 = grafoMalla(2,500)
    Barnes_Hut(gMallan9)
    Barnes_Hut(gMallan100)
    Barnes_Hut(gMallan500)

    #Modelo Erdos Renyi
    gErdosn100 = grafoErdosRenyi(100,450)
    gErdosn500 = grafoErdosRenyi(500,2500)
    Barnes_Hut(gErdosn100)
    Barnes_Hut(gErdosn500)

    #Modelo Gilbert
    gGilbertn100 = grafoGilbet(100,0.5)
    gGilbertn500 = grafoGilbet(500,0.02)
    Barnes_Hut(gGilbertn100)
    Barnes_Hut(gGilbertn500)

    #Modelo Geográfico Simple
    gSimplen100 = grafoGeograficoSimple(100,0.25,directed)
    gSimplen500 = grafoGeograficoSimple(500,0.1,directed)
    Barnes_Hut(gSimplen100)
    Barnes_Hut(gSimplen500)

    #Modelo Barabasi Albert
    gBarabasin100 = grafoBarabasiAlbert(100,20,directed)
    gBarabasin500 = grafoBarabasiAlbert(500,15,directed)
    Barnes_Hut(gBarabasin100)
    Barnes_Hut(gBarabasin500)

    #Modelo Dorogovtsev Mendes
    gDorogovtsevn100 = grafoDorogovtsevMendes(100,directed)
    gDorogovtsevn500 = grafoDorogovtsevMendes(500,directed) 
    Barnes_Hut(gDorogovtsevn100)
    Barnes_Hut(gDorogovtsevn500)

if __name__ == "__main__":
    main()