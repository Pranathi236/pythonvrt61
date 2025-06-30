
'''Scenario 1:Vignan Campus Map
context: Each bullding in a college campus is a node, and walkable paths are edges,.
Represent the campus map using an adjacency list, 
Check If there's a path from the library to the Auditorium using BFS.List all buildings that are directly connected to the Admin Block.
Use DFS to visit all reachable buildings from the Main Gate. 
Find if there are any disconnected buildings (buildings not connected to campus).'''
campus={
    "Main Gate":["Admin Block"],
    "Admin Block":["Main Gate","Library","Canteen","Engineering Block"],
    "Library":["Admin Block","Auditorium"],
    "Canteen":["Admin Block","Hostel"],
    "Auditorium":["Library"],
    "Engineering Block":["Admin Block","Science Block"],
    "Science Block":["Engineering Block"],
    "Hostel":["Canteen"]
}
def bfs(start,target):
    visited=set()
    queue=[start]
    while queue:
        b=queue.pop()
        if b == target:
            return True
        if b not in visited:
            visited.add(b)
            queue+=[n for n in campus[b] if n not in visited]
    return False
def dfs(start,visited=None):
    if visited is None:
        visited=set()
    if start in visited:
        return
    print(start,end=' ')
    visited.add(start)
    for neighbour in campus[start]:
        dfs(neighbour,visited)
def disconnected():
    visited=set()
    dfs(next(iter(campus)),visited)
    return set(campus.keys())- visited
#1.Adjacency List
print("1. Campus Map : ")
for b,n in campus.items():
    print(f"{b} -> {', '.join(n)}")
print("\n2. Path from library to auditorium exists : ")
print("Yes" if bfs ("Library","Auditorium") else "No")
print("\n3. Direct connections from admin block : ")
print(campus["Admin Block"])
print("\n4. DFS from Main Gate:")
dfs("Main Gate")
print()
print("\n5.Disconnected Buildings : ")
d=disconnected()
print(d if d else "None, campus is fully connected.")