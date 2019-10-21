from collections import deque
def isLama(person):
    if person == "Lama":
        return True
    else:
        return False

graph = {}
graph["ty"] = ["Magda","Dominika","Paulina"]
graph["Dominika"] = ["Lama","Kurak"]
graph["Kurak"] = []
graph["Lama"] = []
graph["Paulina"] = []
graph["Magda"] = []

searched = []
search_query = deque()
search_query += graph["ty"]
while search_query:
    person = search_query.popleft()
    if not person in searched:
        print(person)
        if isLama(person):
            print(person)
            print(graph[person])
        else:
            search_query += graph[person]
            searched.append(person)
            #print(search_query)


print(searched)
print(graph["ty"])