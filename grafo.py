class elemento:
	
	def __init__(self, vertice, peso):
		self.vertice = vertice
		self.peso = peso
	
	def __lt__(self, outro):
		return self.peso < outro.peso
	
def min_heapify(vet, raiz, tam):
	
	menor = raiz
	
	esq = (2 * raiz) + 1
	while esq < tam and vet[esq] < vet[menor]:
		menor = esq
	
	dire = (2 * raiz) + 2
	while dire < tam and vet[dire] < vet[menor]:
		menor = dire
	
	if raiz != menor:
		vet[raiz], vet[menor] = vet[menor], vet[raiz]
		min_heapify(vet, menor, tam)
	
def montar_min_heap(vet, tam):
	
	ult = (tam // 2) - 1
	for i in range(ult, -1, -1):
		min_heapify(vet, i, tam)
# CLASSE ELEMENTO E FUNÇÕES DE HEAP MÍNIMA
# (ESTÃO AQUI PARA GERENCIAR A FILA DE PRIORIDADE DA FUNÇÃO DE DIJKSTRA)

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
                if item[0] == v: 
                    return True
            return False
        
        else:

            flag_1 = flag_2 = False

            for item in self.adjacencias[u]:
                if item[0] == v: 
                    flag_1 = True
            for item in self.adjacencias[v]:
                if item[0] == u: 
                    flag_2 = True

            return flag_1 is True and flag_2 is True
    
    def peso(self, u, v):

        for item in self.adjacencias[u]:
            if item[0] == v: 
                return item[1]
        return None
    
    def inserir_aresta(self, u, v, w):

        item = [v, w]
        self.adjacencias[u].append(item)

        if not self.direcionado:
            item = [u, w]
            self.adjacencias[v].append(item)

    def remover_aresta(self, u, v):
        
        i = j = 0

        for item in self.adjacencias[u]:
            if item[0] == v:
                self.adjacencias[u].pop(i)
            else:
                i += 1

        if not self.direcionado:
            for item in self.adjacencias[v]:
                if item[0] == u:
                    self.adjacencias[v].pop(j)
                else:
                    j += 1
    
    def encontrar_adjacencias(self, u):

        saida = []

        for item in self.adjacencias[u]:
            if item[0] is not None:
                saida.append(item[0])
        
        return saida
    
    def dfs(self, u):
        pass

    def bfs(self, u):
        pass

    def floyd_warshall(self, u):
        pass

    # ==========ALGORITMO DE DIJKSTRA========== 
    # (RETORNA A LISTA DE DISTANCIAS DE TODOS OS VERTICES EM RELAÇÃO AO
    # VERTICE PASSADO COMO PARÂMETRO)
    def dijkstra(self, u):

        agenda = []
        pai = [-1 for _ in range(self.num_vertices)]
        distancias = [1_000_000 for _ in range(self.num_vertices)]

        agenda.append(elemento(u, 0))
        distancias[u] = 0

        while agenda != []:

            elem = agenda.pop(0)
            vertice_da_vez, custo = elem.vertice, elem.peso
            todas_adjacencias = self.encontrar_adjacencias(vertice_da_vez)

            for v in todas_adjacencias:

                novo_peso = custo + self.peso(vertice_da_vez, v)

                if distancias[v] > novo_peso:
                    distancias[v] = novo_peso
                    pai[v] = vertice_da_vez
                    agenda.append(elemento(v, novo_peso))
                    montar_min_heap(agenda, len(agenda))

        return distancias


# FUNÇÕES DE INTERAÇÃO COM O USUÁRIO
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
        
        print(f"Vértices adjacentes a {u}: {txt}.")

# def imprimir_lista_adj():

#     for i in range(g.num_vertices):
#         print(f'Adjacencias do vertice {i + 1}: ', end = '')
#         for item in g.adjacencias[i]:
#             print(f'[({item[0]}, {g.peso(i, item[0])})]', end = '')
#         print()

def sair():
    print('Saindo...')
    exit()

def main():

    while True:

        print('===============GRAFO===============')
        print('Escolha uma das seguintes opcoes: ')
        print('1. Criar grafo.')
        print('2. Inserir n arestas.')
        print('3. Remover aresta.')
        print('4. Imprimir adjacencias de um vertice u.')
        print('5. Imprimir lista de adjacencias.')
        print('6. Sair.')
        
        print('Digite sua opcao: ', end = '')
        opc = int(input())

        match opc:
            case 1:
                print('Digite o numero de vertices desejados: ', end = '')
                num_vertices = int(input())
                print('Digite "s" para grafo direcionado ou "n" para grafo nao direcionado: ', end = '')
                direcionado = input()
                cria_grafo(num_vertices, direcionado)
            case 2:
                print('Digite a quantidade de arestas que voce quer adicionar: ', end = '')
                num = int(input())
                for _ in range(num):   
                    print('Digite o primeiro vertice: ', end = '')
                    u = int(input())
                    print('Digite o segundo vertice: ', end = '')
                    v = int(input())
                    print('Digite o peso: ', end = '')
                    w = int(input())
                    insere_aresta(u, v, w)
            case 3:
                print('Digite o primeiro vertice: ', end = '')
                u = int(input())
                print('Digite o segundo vertice: ', end = '')
                v = int(input())
                remove_aresta(u, v)
            case 4:
                print('Digite o vertice: ', end = '')
                u = int(input())
                imprimir_adjacentes(u)
            # case 5:
            #     imprimir_lista_adj()
            case 6:
                sair()            

if __name__ == '__main__':
    main()