print("Hello")

# test
from bgraphv2.core import Graph

# g = Graph()
# for i in range(6):
#   g.addVertex(i)
# g.addEdge(0,1,5)
# g.addEdge(0,5,2)
# g.addEdge(1,2,4)
# g.addEdge(2,3,9)
# g.addEdge(3,4,7)
# g.addEdge(3,5,3)
# g.addEdge(4,0,1)
# g.addEdge(5,4,8)
# g.addEdge(5,2,1)
# for v in g:
#     for w in v.getConnections():
#         print("( %s , %s )" % (v.getId(), w.getId()))


#Build word graph
def buildGraph(wList):
    d = {}
    g = Graph()
    #phân hoạch các từ cùng độ dài chỉ khác nhau 1 ký tự
    for line in wList: #lấy từng từ trong từ điển
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    #thêm các đỉnh và các cạnh cho các từng trong cùng bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)
    return g


#main
wList = ["FOOD", "FOOT", "FOOL", "FORT",
        "GOOD",
        "PALE", "PALM", "POLE", "POLL", "POOL",
        "SAGE", "SALE", "SALT"]
g = buildGraph(wList)


for v in g:
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))

