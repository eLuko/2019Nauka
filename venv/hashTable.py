from collections import deque
book = dict()
book["ty"]=["alcja","łukasz"]
book["awokado"]=[1.67,9,887]


pom = book.get("awokado")
'''
graph={}
graph["ty"]=["Paulina","Dominika"]
graph["Paulina"] = ["Misiak","Pa"]
searchQueue = deque()
searchQueue +=graph["ty"]
print("------------------")
print(searchQueue)
while searchQueue:
    person = searchQueue.popleft()
    print(person)
'''


graphLoop={}
graphLoop["ty"]=["Paulina","Dominika"]
graphLoop["Paulina"] = ["A","B"]
loopQueue = deque()
loopQueue +=graphLoop["ty"]
print("------------------")
print(loopQueue)
#while loopQueue:
person = loopQueue.popleft()
print(person)
print(loopQueue)
loopQueue +=graphLoop["Paulina"]
print(loopQueue)