class grafo:

    def __init__(self, num_vertices, direcionado):
        self.num_vertices = num_vertices
        self.direcionado = direcionado

        self.adjacencias = [[] for _ in range(num_vertices)]
        # self.adjacencias = [0] * num_vertices
        # for i in range(num_vertices):
        #     self.adjacencias[i] = []
    
    def aresta(self, u, v):
        if self.direcionado:
            for item in self.adjacencias[u]:
                if item[0] == v: return True
                return False
        else:
            flag_1 = flag_2 = False
            for item in self.adjacencias[u]:
                if item[0] == v: flag_1 = True
            for item in self.adjacencias[v]:
                if item[0] == u: flag_2 = True
            return flag_1 is True and flag_2 is True
    
    def peso(self, u, v):
        for item in self.adjacencias[u]:
            if item[0] == v: return item[1]
        return None
    
    def inserir_aresta(self, u, v, w):
        item = [v, w]
        self.adjacencias[u].append(item)
        if not self.direcionado:
            item = [u, w]
            self.adjacencias[v].append(item)

    def remover_aresta(self, u, v):
        for item in self.adjacencias[u]:
            if item[0] == v: item = None
        if not self.direcionado:
            for item in self.adjacencias[v]:
                if item[0] == u: item = None
    
    def encontrar_adjacencias(self, u):

        saida = []

        for item in self.adjacencias[u]:
            if item[0] is not None:
                saida.append(item[0])
        
        return saida

def cria_grafo(num_vertices, direcionado):

    global g
    g = grafo(num_vertices, direcionado)
    if direcionado:
        print(f'Grafo direcionado criado com {num_vertices} vertices.')
    else:
        print(f'Grafo nao direcionado criado com {num_vertices} vertices.')

def verificar_vertices(vertices):

    if grafo is None:
        print('Voce ainda nao criou um grafo.')
        return False
    
    for v in vertices:
        if v < 0:
            print(f'Vertice {v} nao eh valido(negativo).')
            return False
        elif v >= g.num_vertices:
            print(f'Vertice {v} nao eh valido (index maximo {g.num_vertices}).')
            return False
        
    return True

def verifica_vertice(u, v):
    if verificar_vertices([u, v]):
        if g.aresta(u, v):
            print(f'A aresta ({u}, {v}) existe e tem peso {g.peso(u, v)}.')
        else:
            print(f'A aresta ({u}, {v}) nao existe.')

def insere_aresta(u, v, w):

    if verificar_vertices([u, v]):
        if g.aresta(u, v):
            print(f'A aresta ({u}, {v}, {g.peso(u, v)}) existe e teve seu peso atualizado para {w}.')
        else:
            print(f'Aresta ({u}, {v}, {w}) criada.')
        g.inserir_aresta(u, v, w)

def remove_aresta(u, v):

    if verificar_vertices([u, v]):
        if g.aresta(u, v):
            print(f'Aresta ({u}, {v}) removida.')
        g.remover_aresta(u, v)

def imprimir_adjacentes(u):

    if verificar_vertices([u]):
        adjacencias = g.encontrar_adjacencias(u)

        if len(adjacencias) == 0:
            txt = ('Nenhum vertice')
        elif len(adjacencias) == 1:
            txt = f'Apenas {adjacencias[0]}'
        else:
            lista_str = [str(_) for _ in adjacencias]
            prim = lista_str[:-1]
            ult = lista_str[-1]
            txt = ', '.join(prim) + ' e ' + ult

def imprimir_matriz_adj():
    print("   |" + "|".join([f" {_:2d} " for _ in range(grafo.num_vertices)]))
    print("---+" + "|".join(["----"] * grafo.num_vertices))
    for u in range(grafo.num_vertices):
        print(f"{u:2d} ", end='')
        for v in range(grafo.num_vertices):
            if grafo.aresta(u, v):
                print(f"| {grafo.peso(u, v):2d} ", end='')
            else:
                print(f"|    ", end='')
        print()

def sair():
    print('Saindo...')
    exit()

def main():
    # g = grafo(3, False)
    # g.inserir_aresta(0, 1, 1)
    # g.inserir_aresta(1, 2, 2)
    # g.inserir_aresta(2, 0, 3)
    # print(g.encontrar_adjacencias(0))
    # print(g.encontrar_adjacencias(1))
    # print(g.encontrar_adjacencias(2))
    # print(g.peso(0, 1))
    # print(g.peso(1, 2))
    # print(g.peso(2, 0))

    while True:
        
        opc = int(input())

        match opc:
            case 1:
                print('Digite o numero de vertices desejados: ', end = '')
                num_vertices = int(input())
                print('Digite "s" para grafo direcionado ou "n" para grafo nao direcionado: ', end = '')
                direcionado = input()
                cria_grafo(num_vertices, direcionado)
            case 2:
                print('Digite a primeira aresta: ', end = '')
                u = int(input())
                print('Digite a segunda aresta: ', end = '')
                v = int(input())
                print('Digite o peso: ', end = '')
                w = int(input())
                insere_aresta(u, v, w)
            case 3:
                print('Digite ')            

if __name__ == '__main__':
    main()




            
