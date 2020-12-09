# astar-paris-subway-simplified
Adaptative Cognitive Agents' first assignment using A* algorithm

<h3>Paris Subway Simplified Problem

Use A* algorithm to solve the Paris Subway Simplified problem

**input**: User choose input from station 1 (E1) to station 14 (E14)
**output**: Border evolution with cost from root until goal, solution with final cost and elapsed time (min) considering train speed as 30 Km/h

![Subway Map](https://github.com/vhsabino/astar-paris-subway-simplified/blob/main/map/paris-subway-map-simplified.png)

<h3> Example: Algorithm output from E2 to E14 (portuguese text)
  
```
Busca A* no mapa de Paris

    Percurso: E2 => E14

====================================

Fronteira de Busca      : [(24.7, 'E10'), (25.1, 'E3'), (36.6, 'E9'), (39.8, 'E1')]
Cidades Expandidas      : ['E2']  #1

Fronteira de Busca      : [(25.1, 'E3'), (36.6, 'E9'), (39.8, 'E1')]
Cidades Expandidas      : ['E2', 'E10']  #2

Fronteira de Busca      : [(30.200000000000003, 'E4'), (32.3, 'E13'), (36.6, 'E9'), (39.8, 'E1')]
Cidades Expandidas      : ['E2', 'E10', 'E3']  #3

Fronteira de Busca      : [(32.3, 'E13'), (36.6, 'E9'), (39.8, 'E1'), (45.7, 'E5'), (57.7, 'E8')]
Cidades Expandidas      : ['E2', 'E10', 'E3', 'E4']  #4

Fronteira de Busca      : [(32.3, 'E14'), (36.6, 'E9'), (39.8, 'E1'), (45.7, 'E5'), (57.7, 'E8')]
Cidades Expandidas      : ['E2', 'E10', 'E3', 'E4', 'E13']  #5

Fronteira de Busca      : [(36.6, 'E9'), (39.8, 'E1'), (45.7, 'E5'), (57.7, 'E8')]
Cidades Expandidas      : ['E2', 'E10', 'E3', 'E4', 'E13', 'E14']  #6


=======================================================

Menor caminho   : ['E2', 'E3', 'E13', 'E14']
Numero de cidade visitas            : 4
Distancia total percorrida          : 32.3Km
Tempo total da viagem           : 64.6min

```
