# Code adapted from https://github.com/rizanw/Romania-A-star-Algorithm
# 
# Author: Victor Sabino

import heapq

class priorityQueue:
    def __init__(self):
        self.cities = []

    def push(self, city, cost):
        heapq.heappush(self.cities, (cost, city))

    def pop(self):
        return heapq.heappop(self.cities)
    
    def border(self):
        return sorted(self.cities)

    def isEmpty(self):
        if (self.cities == []):
            return True
        else:
            return False

    def check(self):
        print(self.cities)

paris = []
parisConnect = []

def makearray(): #cria matrizes de distancia
    file1 = open("paris-direct.txt", 'r')
    for string in file1:
        row = string.split(',')
        for i in range(len(row)):
            row[i] = float(row[i])
        paris.append(row)        
    file2 = open("paris-connect.txt", 'r')
    for string in file2:
        row = string.split(',')
        for i in range(len(row)):
            row[i] = float(row[i])
        parisConnect.append(row)

def get_g(start, goal): # funcao para calcular g(n)
    s1 = start.split('E')
    s1 = int(s1[1]) - 1
    s2 = goal.split('E')
    s2 = int(s2[1]) - 1
    if s1 > s2:
        s1, s2 = s2, s1
    g = parisConnect[s1][s2] #
    return g

def get_h(start, goal): #funcao para calcular h(n)
    s1 = start.split('E')
    s1 = int(s1[1]) - 1
    s2 = goal.split('E')
    s2 = int(s2[1]) - 1
    if s1 > s2:
        s1, s2 = s2, s1
    h = paris[s1][s2]
    return h

def getAvailableCities(current,previousCity): #retorna todas as cidades conectadas a cidade atual
    s1 = current.split('E')
    s1 = int(s1[1]) - 1
    s2 = previousCity.split('E')
    s2 = int(s2[1]) - 1
    availableCities = []
    for i in range(len(parisConnect[s1])):
        if parisConnect[s1][i] != 0.0 and i > s1: #impede de voltar para a cidade de origem
            city = "E" + str(i + 1)
            availableCities.append(city)
        if parisConnect[i][s1] != 0.0 and i <= s1:
            city = "E" + str(i + 1)
            availableCities.append(city)
    return availableCities

def astar(start, end):
    path = {}
    distance = {}
    q = priorityQueue()
    q.push(start, 0)
    distance[start] = 0
    path[start] = None
    expandedList = []
    printoutput(start, end, path, distance, expandedList, q, 0)
    previousCity = start

    while (q.isEmpty() == False):
        current = q.pop()[1]
        expandedList.append(current)

        if (current == end):
            break

        availableCities = getAvailableCities(current, previousCity)

        for new in availableCities:
            g_cost = distance[current] + get_g(current,new)
            #print("from " + current + " to " + new + " => " + str(g_cost))
            if (new not in distance or g_cost < distance[new]):
                distance[new] = g_cost
                f_cost = g_cost + get_h(new,end)
                #print("from " + current + " to " + new + " => " + str(f_cost))
                q.push(new,f_cost)
                path[new] = current
        printoutput(start, end, path, distance, expandedList, q, 1)
    printoutput(start, end, path, distance, expandedList, q, 2)


def printoutput(start, end, path, distance, expandedlist, q, stage):
    finalpath = []
    i = end

    if stage == 0:
        print("\nBusca A* no mapa de Paris\n")
        print("\t Percurso: " + str(start) + " => " + str(end) + "\n")
        print("====================================\n")
    elif stage > 0:
        print("Fronteira de Busca \t\t: " + str(q.border()))
        print("Cidades Expandidas \t\t: " + str(expandedlist) + "  #" + str(len(expandedlist)) + "\n")
    if stage == 2:
        while (path.get(i) != None):
            finalpath.append(i)
            i = path[i]
        finalpath.append(start)
        finalpath.reverse()
        print("\n=======================================================\n")
        print("Menor caminho \t: " + str(finalpath))
        print("Numero de cidade visitas \t\t\t: " + str(len(finalpath)))
        print("Distancia total percorrida \t\t\t: " + str(distance[end]) + "Km")
        print("Tempo total da viagem \t\t\t: " + str((distance[end]/30)*60) + "min\n\n")




def main():
    makearray() # criar vetores de distancia (tabelas)
    start = "E2" # estacao inicial
    goal = "E14" # estacao destino
    astar(start, goal) 


if __name__ == "__main__":
    main()