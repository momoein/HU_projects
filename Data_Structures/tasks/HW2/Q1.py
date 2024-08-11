class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.height = 0



def level_order(root):
        Q = []
        Q.append(root)
        while len(Q) > 0:
            temp = Q.pop(0)
            print(temp.data, end=", ")
            for i in range(len(temp.children)):
                 Q.append(temp.children[i])


def update_height(root):
    if root is None:
        return
     
    if len(root.children) < 1:
        return 0
    
    heights = []
    for i in range(len(root.children)):
        h = update_height(root.children[i])
        heights.append(h)
    
    # update root height
    root.height = max(heights) + 1

    return root.height



def cities_map(array):
    nc = len(array) + 1   # num of cities
    cities = [[] for i in range(nc+1)]

    abr = [i[1] for i in array] # All but the root
    root = None

    for item in array:
        i = item[0]
        j = item[1]
        
        cities[i].append(j)
        if i not in abr:
            root = i

    return root, cities



def build_tree(root_index, map):
    root = Node(root_index)
    root.children = map[root_index]
    
    for i in range(len(root.children)):
        root.children[i] = build_tree(root.children[i], map)
    
    return root



def cut_line_counter(root):
    cut_line_count = 0
    Q = []
    Q.append(root)

    while len(Q) > 0:
        temp = Q.pop(0) 

        for i in range(len(temp.children)):
            child = temp.children[i]
            Q.append(child)

            if child.height >= 1:
                cut_line_count += 1
    
    return cut_line_count



def result(n):
    return n * 2 + 2



a = [[1, 2], [1, 3], [3, 4], [3, 5]]

root, city = cities_map(a)

r = build_tree(root, city)
update_height(r)

res = result(cut_line_counter(r))
print(res)