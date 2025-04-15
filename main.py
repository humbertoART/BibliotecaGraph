from Models_Graphs import grafoMalla, grafoErdosRenyi, grafoGilbet, grafoGeograficoSimple, grafoBarabasiAlbert, grafoDorogovtsevMendes

def main():
    n1 = 50
    n2 = 200
    n3 = 500
    m = 12
    mErdos = 200
    mErdos2 = 500
    directed = False
    p = 0.5
    r1 = 0.4
    r2 = 0.15
    d = 1

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
    # gGilbertn2 = grafoGilbet(n2,p,directed)
    # gGilbertn3 = grafoGilbet(n3,p,directed)
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

    gBarabasin1 = grafoBarabasiAlbert(n1,d,directed)
    gBarabasin2 = grafoBarabasiAlbert(n2,d,directed)
    gBarabasin3 = grafoBarabasiAlbert(n3,d,directed)

    gBarabasin1.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Grafos/gBarabasin1.dot")

    gBarabasin2.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Grafos/gBarabasin2.dot")

    gBarabasin3.graphiViz("C:/Users/hrosa/OneDrive/Documentos/" \
    "CIC IPN/Primer Semestre/Analisis y Diseño de Algoritmos/" \
    "Proyecto_Biblioteca/BibliotecaGraph/Texto_Grafos/gBarabasin3.dot")        

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

if __name__ == "__main__":
    main()