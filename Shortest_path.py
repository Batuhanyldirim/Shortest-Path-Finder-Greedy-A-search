"""
This code searchs the shortest path between malaga and valladolid in attached map. The solution found by Greedy Best First Search and A* search.
"""

#Greedy Best First Search

f = open("/content/Assignment 1 Spain map.txt", "r")

lines = f.readlines()

graph = {}
dist = {}

start = "Malaga"
stop = "Valladolid"

state = [[start],0] #keeps current state in code (node is equal with our nodes in this code)

paths = {start:state.copy()} #consist every reached last node of branch

roads = [] # possible roads that we can move in the next step

visited = [start] # keeps visited cities in order to avoid loops

for i in lines[5:83]:# creates graph in a dictionary from text file
  if i != "\n":
    words = i.split(" ")
    if words[0] not in graph:
      if words[2][-1] == "\n":
        graph[words[0]] = {words[1]:int(words[2][:-1])}
      else:
        graph[words[0]] = {words[1]:int(words[2])}
    else:
      if words[2][:-1] == "\n":
        graph[words[0]][words[1]]  = int(words[2][:-1])
      else:
        graph[words[0]][words[1]]  = int(words[2])


    if words[1] not in graph:
      if words[2][:-1] == "\n":
        graph[words[1]] = {words[0]:int(words[2][:-1])}
      else:
        graph[words[1]] = {words[0]:int(words[2])}

    else:
      if words[2][:-1] == "\n":
        graph[words[1]][words[0]]  = int(words[2][:-1])
      else:
        graph[words[1]][words[0]]  = int(words[2])

for i in lines[85:]: #Creates net distance to stop point dictionary
  if i !="\n":
    words = i.split(" ")
    if words[0] not in dist:
      dist[words[0]] = int(words[1])


def find_roads(city): #finds possible reacheble roads for the next step and ads it to path dictionary with their costs
  for i in graph[city]: # for every city we can reach from given "city"
    if i not in paths and i not in visited:
      #creating new end node of a trace in paths dictionary
      temp = (paths[city][0]).copy()
      val = paths[city][1]
      temp.append(i)
      val += graph[city][i]

      paths[i] = [temp.copy(),val]
      temp.pop()
      val -= graph[city][i]

      roads.append(i)# also adding this possible road to road list
  del paths[city] # deleting the path of the node we are in right now because we found a further way


def choose_road(roads):#chooses the next road to go with respect to closness to the final stop
  min = 9999999
  c = ""
  k=0
  for i in range(len(roads)):
    if roads[i] not in visited and dist[roads[i]] < min:
      c = roads[i]
      k=i
      min = dist[roads[i]]
  roads.pop(k)
  visited.append(c)
  return c


def GBFS(state):
  find_roads(state[0][-1]) #at first we find possible roads to go
  while roads: #this loop here to trace back until a valid node if we stuck in a dead end
    chosen = choose_road(roads) #chooses the road for next step
    #updating the state
    state[1] = paths[chosen][1] 
    state[0] = paths[chosen][0]
    if chosen == stop: # check if we are in desired place 
      return state
    else:
      solution = GBFS(state) #if not keep search
      return state
  return []



final = GBFS(state)
print(state)

val = 0
prev = start
for i in state[0][1:]:

  val += graph[prev][i]
  print(prev,"-->",i,graph[prev][i])
  prev = i
print(val)


#A* Search

f = open("/content/Assignment 1 Spain map.txt", "r")

lines = f.readlines()

graph = {}
dist = {}

start = "Malaga"
stop = "Valladolid"

state = [[start],0] #keeps current state in code (node is equal with our nodes in this code)

paths = {start:state.copy()} #consist every reached last node of branch

roads = [] # possible roads that we can move in the next step

visited = [start] # keeps visited cities in order to avoid loops

for i in lines[5:83]:# creates graph in a dictionary from text file
  if i != "\n":
    words = i.split(" ")
    if words[0] not in graph:
      if words[2][-1] == "\n":
        graph[words[0]] = {words[1]:int(words[2][:-1])}
      else:
        graph[words[0]] = {words[1]:int(words[2])}
    else:
      if words[2][:-1] == "\n":
        graph[words[0]][words[1]]  = int(words[2][:-1])
      else:
        graph[words[0]][words[1]]  = int(words[2])


    if words[1] not in graph:
      if words[2][:-1] == "\n":
        graph[words[1]] = {words[0]:int(words[2][:-1])}
      else:
        graph[words[1]] = {words[0]:int(words[2])}

    else:
      if words[2][:-1] == "\n":
        graph[words[1]][words[0]]  = int(words[2][:-1])
      else:
        graph[words[1]][words[0]]  = int(words[2])

for i in lines[85:]: #Creates net distance to stop point dictionary
  if i !="\n":
    words = i.split(" ")
    if words[0] not in dist:
      dist[words[0]] = int(words[1])


def find_roads(city): #finds possible reacheble roads for the next step and ads it to path dictionary with their costs
  for i in graph[city]: # for every city we can reach from given "city"
    if i not in paths and i not in visited:
      #creating new end node of a trace in paths dictionary
      temp = (paths[city][0]).copy()
      val = paths[city][1]
      temp.append(i)
      val += graph[city][i]

      paths[i] = [temp.copy(),val]
      temp.pop()
      val -= graph[city][i]

      roads.append(i)# also adding this possible road to road list
  del paths[city] # deleting the path of the node we are in right now because we found a further way


def choose_road(roads):#chooses the next road to go with respect to closness to the final stop
  min = 9999999
  c = ""
  k=0
  
  for i in range(len(roads)):
    if len(paths[roads[i]][0]) > 1:
      funcG = paths[roads[i]][1] - graph[paths[roads[i]][0][-2]][roads[i]]
    else:
      funcG = 0
    funcH = dist[roads[i]]
    funcf = funcG + funcH
    if roads[i] not in visited and funcf < min:
      min = funcf
      c = roads[i]
      k=i
  roads.pop(k)
  visited.append(c)
  return c


def ASearch(state):
  find_roads(state[0][-1]) #at first we find possible roads to go
  while roads: #this loop here to trace back until a valid node if we stuck in a dead end
    chosen = choose_road(roads) #chooses the road for next step
    #updating the state
    state[1] = paths[chosen][1] 
    state[0] = paths[chosen][0]
    if chosen == stop: # check if we are in desired place 
      return state
    else:
      solution = ASearch(state) #if not keep search
      return state
  return []



final = ASearch(state)
print(state)

val = 0
prev = start
for i in state[0][1:]:

  val += graph[prev][i]
  print(prev,"-->",i,graph[prev][i])
  prev = i
print(val)
