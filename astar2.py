class Node():
    """Classe representando um nó da implementacao A*"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        #g: distancia do no ate o no inicial
        self.g = 0

        #h: distancia euclidiana do no ate o no final
        self.h = 0

        #f: na funcao astar = g + h
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    """Retorna uma lista de tuplas como o caminho"""

    # cria os nos: inicio e objetivo
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # inicializa as listas: fechada e aberta
    open_list = []
    closed_list = []

    # adicionando no inicial na lista aberta (em busca)
    open_list.append(start_node)

    # adiciona os nos a lista aberta ate encontrar o no objetivo
    while len(open_list) > 0:

        # obtem o no atual da lista aberta
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # retira o no da lista aberta e add na fechada
        open_list.pop(current_index)
        closed_list.append(current_node)

        # objetivo encontrado!
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # retorna o path revertido

        # gerando filhos..
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # obtem a posicao do no filho
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # verifica se esta dentro do maze
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # verifica se existe obstaculo
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # cria um novo no
            new_node = Node(current_node, node_position)

            
            children.append(new_node)

        # itera os filhos possiveis
        for child in children:

            # se o filho esta na lista fechada, ignorar
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # gerar os valores g, h e f (usando dist euclidiana)
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # filho ja esta na lista aberta: neste caso usar o caminho melhor
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # adiciona o filho na lista aberta
            open_list.append(child)


def main():
    
    #gerando o maze...
    
    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    #definir inicio e objetivo
    start = (0, 0)
    end = (7, 6)

    path = astar(maze, start, end)
    
    #printar as tuplas geradas na funcao astar
    print(path)


if __name__ == '__main__':
    main()
