#!/usr/bin/python

"""

This problem was asked by Airbnb.

You are given a huge list of airline ticket prices between different cities around the world on a given day. These are all direct flights. Each element in the list has the format (source_city, destination, price).

Consider a user who is willing to take up to k connections from their origin city A to their destination B. Find the cheapest fare possible for this journey and print the itinerary for that journey.

For example, our traveler wants to go from JFK to LAX with up to 3 connections, and our input flights are as follows:

[
    ('JFK', 'ATL', 150),
    ('ATL', 'SFO', 400),
    ('ORD', 'LAX', 200),
    ('LAX', 'DFW', 80),
    ('JFK', 'HKG', 800),
    ('ATL', 'ORD', 90),
    ('JFK', 'LAX', 500),
]

Due to some improbably low flight prices, the cheapest itinerary would be JFK -> ATL -> ORD -> LAX, costing $440.

"""

# Dijkstra's Algorithm

from collections import defaultdict,deque

class Graph:
    def __init__(self, flights):
        self.flights=flights
        self.vertices=defaultdict(list)
        for (src,dst,fare) in flights:
            self.vertices[src]+=[(dst,fare)]

    # use BFS
    def cheapest_path_bfs(self,start,end,stops):
        min_cost,min_path=float('inf'),[]

        dq=deque([(start,0,[start])])
        while dq:
            (cur,cost_so_far,path)=dq.popleft()
            if len(path)<=stops:
                for next,cost in self.vertices[cur]:
                    new_cost=cost_so_far+cost
                    new_path=path+[next]
                    if next==end:
                        if new_cost<min_cost:
                            min_cost,min_path=new_cost,new_path
                            print("min_cost:",min_cost, "min_path:", min_path)
                    else:
                        dq.append((next,new_cost,new_path))

        print("Overall:  min_cost:",min_cost, "min_path:", min_path)
        return min_cost

    # use DFS
    def helper(self,start,end,stops,cost_so_far=0,path=[]):
        if stops<0:
            return 0,[]

        if start==end:
            print("path: ", path, "cost: ", cost_so_far)
            return cost_so_far,path

        min_cost,min_path=float('inf'),[]
        for next,cost in self.vertices[start]:
             new_cost,new_path=self.helper(next,end,stops-1,cost_so_far+cost,path+[next])
             if new_cost>0 and new_cost<min_cost:
                 min_cost,min_path=new_cost,new_path

        return min_cost,min_path

    def cheapest_path_dfs(self,start,end,stops):
        min_cost,min_path=self.helper(start,end,stops,0,[start])
        print("Overall:  min_cost:",min_cost, "min_path:", min_path)
        return min_cost if len(min_path)>1 else 0

flights=[
    ('JFK', 'ATL', 150),
    ('ATL', 'SFO', 400),
    ('ORD', 'LAX', 200),
    ('LAX', 'DFW', 80),
    ('JFK', 'HKG', 800),
    ('ATL', 'ORD', 90),
    ('JFK', 'LAX', 500),
]

g=Graph(flights)
assert g.cheapest_path_bfs('JFK','LAX',3)==440
assert g.cheapest_path_dfs('JFK','LAX',3)==440
