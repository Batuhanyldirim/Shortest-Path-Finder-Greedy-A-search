# Shortest-Path-Finder-Greedy-A-search

### Explanation of the problem

In this assignment we are trying to find the shortest path between Malaga and Valladolid in Spain. We have the information of which citiesarerelatedtowhich other cities and what is the real cost of this given road, also we know the direct distance between every city and desired destination (Valladolid) in a list. As a result we get list of cities like {C1, C2, C3, ... , Cn}. An example soliton is {Malaga, Sevilla, Merida, Caceres, Salamanca, Zamora, Valladolid}. Given case means shortest path between Malaga and Valladolid is solution.


### Equation of f(n) for Gready Best-first Search

In Gready Best-first Search we are choosing the next step in which has the closest net distance to desired destination which means most desirable next move. So our f(n) is calculated as following equation.

If we have the following possible destinations in our next moves {C1,, C2, C3, ... , Cn} we know the net distance between those cities and desired city, so we are looking for Cxwhich gives smallest net distance to given city.We can calculate net distance by heuristic function h(Cx)


![image](https://user-images.githubusercontent.com/41572446/121976803-da7e0080-cd84-11eb-8850-66d4425e4037.png)



We used this function because we are making a greedy searchand this does not guaranties the optimum result. Because we are choosing our next step with only consideration of net distance from the next city and desired city, but real distance may differ in this situation.


### Equation of f(n) for A* Search

In A* search we are choosing the next step in consideration with the real distance we traveled and next city has the minimum heuristic function to the desired city. That means we are checking the distance we already traveled to decide next move and if there is a better option. The f(n) is calculated in two steps for A* search.The first step calculates the h(n) and second step calculates g(n) so our final f(n) = h(n) + g(n)

First step is the same as Greedy Best-first Search so it is the following equation if we have {C1,, C2, C3, ... , Cn} as possible destinations in our next moves and have heuristic function H(Cx) which gives net distance from given city to desired city.

![image](https://user-images.githubusercontent.com/41572446/121976853-ef5a9400-cd84-11eb-9fd4-21411940531b.png)

The second step is the calculation of the road we have took so far. If we have already come along with the path {C1,, C2, C3, ... , Cn} and C2-1gives the real distance between C1to C2then we can calculate g(n) as follows;

![image](https://user-images.githubusercontent.com/41572446/121976870-fe414680-cd84-11eb-8fa3-20d94ee5fb74.png)

As a conclusion we are looking for min(h(n)+g(n)) to decide our next move.We are using this equationbecause we want to minimize our traveled distance, so we are considering the distance we already traveled to not get mocked by net distance instead of real distance.


### Algorithm Differences

We have already discussed differences between algorithms in f(n) equations part but there are similarities and differences in two algorithms. Both algorithms have possible next move options in given states and both algorithms decide one city among possible options to travel as next move. So,algorithms memorize all available next moves in a given state of search tree. The difference starts in f(n) function which decides which city will we move in the next stepand both algorithms choses the smallest n for f(n). In GBFS algorithm we only consider the heuristic function of the next available cities and this may giveus not optimal results because the real distance between two cities are equal or greater than the net distance we obtained from heuristic function. Besides that A* search also calculates the distance already traveled to eliminates the effect of real-net distance difference and gives optimal results with f(n) function which decides better cities to travel.


