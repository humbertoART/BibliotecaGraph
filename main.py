from Models_Graphs import grafoMalla, grafoErdosRenyi, grafoGilbet, grafoGeograficoSimple, grafoBarabasiAlbert, grafoDorogovtsevMendes
import sys
sys.setrecursionlimit(30000)

def main():
    #PROYECTO 1: CREACIÓN DE MODELOS
    #==================================
    n1 = 50
    n2 = 200
    n3 = 500
    m = 12
    mErdos = 200
    mErdos2 = 500
    directed = False
    p = 0.5
    p2 = 0.05
    p3 = 0.01
    r1 = 0.4
    r2 = 0.15
    d1 = 2
    d2 = 3

    # gMallan1 = grafoMalla(m,n1,directed)
    # gMallan2 = grafoMalla(m,n2,directed)
    # gMallan3 = grafoMalla(m,n3,directed)
    # gMallan1.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    # "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    # "Proyecto_Biblioteca/BibliotecaGraph/Texto_Grafos/gMallan1.dot")

    # gMallan2.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    # "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    # "Proyecto_Biblioteca/BibliotecaGraph/Texto_Grafos/gMallan2.dot")

    # gMallan3.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    # "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    # "Proyecto_Biblioteca/BibliotecaGraph/Texto_Grafos/gMallan3.dot")

    # gErdosn1 = grafoErdosRenyi(n1,mErdos,directed)
    # gErdosn2 = grafoErdosRenyi(n2,mErdos,directed)
    # gErdosn3 = grafoErdosRenyi(n3,mErdos2,directed)
    # gErdosn1.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    # "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    # "Proyecto_Biblioteca/BibliotecaGraph/Texto_Grafos/gErdosn1.dot")

    # gErdosn2.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    # "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    # "Proyecto_Biblioteca/BibliotecaGraph/Texto_Grafos/gErdosn2.dot")

    # gErdosn3.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    # "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    # "Proyecto_Biblioteca/BibliotecaGraph/Texto_Grafos/gErdosn3.dot")        

    # gGilbertn1 = grafoGilbet(n1,p,directed)
    # gGilbertn2 = grafoGilbet(n2,p2,directed)
    # gGilbertn3 = grafoGilbet(n3,p3,directed)
    # gGilbertn1.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    # "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    # "Proyecto_Biblioteca/BibliotecaGraph/Texto_Grafos/gGilbertn1.dot")

    # gGilbertn2.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    # "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    # "Proyecto_Biblioteca/BibliotecaGraph/Texto_Grafos/gGilbertn2.dot")

    # gGilbertn3.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    # "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    # "Proyecto_Biblioteca/BibliotecaGraph/Texto_Grafos/gGilbertn3.dot")              

    # gSimplen1 = grafoGeograficoSimple(n1,r1,directed)
    # gSimplen2 = grafoGeograficoSimple(n2,r2,directed)
    # gSimplen3 = grafoGeograficoSimple(n3,r2,directed)
    # gSimplen1.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    # "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    # "Proyecto_Biblioteca/BibliotecaGraph/Texto_Grafos/gSimplen1.dot")

    # gSimplen2.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    # "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    # "Proyecto_Biblioteca/BibliotecaGraph/Texto_Grafos/gSimplen2.dot")

    # gSimplen3.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    # "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    # "Proyecto_Biblioteca/BibliotecaGraph/Texto_Grafos/gSimplen3.dot")            

    # gBarabasin1 = grafoBarabasiAlbert(n1,d1,directed)
    # gBarabasin2 = grafoBarabasiAlbert(n2,d1,directed)
    # gBarabasin3 = grafoBarabasiAlbert(n3,d2,directed)
    # gBarabasin1.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    # "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    # "Proyecto_Biblioteca/BibliotecaGraph/Texto_Grafos/gBarabasin1.dot")

    # gBarabasin2.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    # "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    # "Proyecto_Biblioteca/BibliotecaGraph/Texto_Grafos/gBarabasin2.dot")

    # gBarabasin3.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    # "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    # "Proyecto_Biblioteca/BibliotecaGraph/Texto_Grafos/gBarabasin3.dot")        

    # gDorogovtsevn1 = grafoDorogovtsevMendes(n1,directed)
    # gDorogovtsevn2 = grafoDorogovtsevMendes(n2,directed)
    # gDorogovtsevn3 = grafoDorogovtsevMendes(n3,directed)
    # gDorogovtsevn1.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    # "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    # "Proyecto_Biblioteca/BibliotecaGraph/Texto_Grafos/gDorogovtsenn1.dot") 

    # gDorogovtsevn2.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    # "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    # "Proyecto_Biblioteca/BibliotecaGraph/Texto_Grafos/gDorogovtsenn2.dot")     

    # gDorogovtsevn3.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    # "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    # "Proyecto_Biblioteca/BibliotecaGraph/Texto_Grafos/gDorogovtsenn3.dot")   


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
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Proyecto2/gDorogovtsenn21.dot")     

    gDorogovtsevn23.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Proyecto2/gDorogovtsenn21.dot") 

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

if __name__ == "__main__":
    main()