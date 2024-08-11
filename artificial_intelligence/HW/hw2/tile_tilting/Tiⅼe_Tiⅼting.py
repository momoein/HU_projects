from copy import deepcopy
import heapq

class State:
    def __init__(self, table, parent=None, g=0):
        self.table = table
        self.g = g+1
        self.parent = parent

class Tile_Tilting:
    def __init__(self, initial, goal, size):
        self.initial = initial
        self.goal = goal
        self.size = size
        self.movement = {
            "up" : self.up,
            "down" : self.down,
            "left" : self.left,
            "right" : self.right
        }
        self.place = self.varieble()
    
    def result(self, table):
        my_list = []
        a = list(self.movement.keys())
        for i in a:
            new_table = deepcopy(table)
            my_list.append(self.movement[i](new_table))
        return my_list
        
    def hu(self, table):
        max = 0
        h = 0
        a = list(self.place.keys())
        for i in range(self.size):
            for j in range(self.size):
                if table[i][j] in a:
                    a.remove(table[i][j])
                    h = self.find_hu_v(table, table[i][j], i, j)
                if max < h:
                    max = h
        return max

    def find_hu_v(self, table, x1, x, y):
        max = 0
        h = 0
        a = self.place[x1]
        for i in a:
            if x == i[0] and y == i[1]:
                h = 0
            elif x != i[0] and y != i[1]:
                h = 1
            else:
                h = 2
            if max < h:
                max = h
        return max
    
    def varieble(self):
        dic = {}
        for i in range(self.size):
            for j in range(self.size):
                if self.goal[i][j] is not None:
                    if self.goal[i][j] in list(dic.keys()):
                        dic[self.goal[i][j]].append([i, j])
                    else:
                        dic[self.goal[i][j]] = [[i, j]]
        return dic

    def goal_test(self, table):
        for i in range(self.size):
            for j in range(self.size):
                if table[i][j] != self.goal[i][j]:
                    return False
        return True

    def up(self, table):
        i = 1
        k = 1
        j = 0
        while j < self.size:
            if table[i-1][j] is None:
                table[i-1][j] = table[i][j]
                table[i][j] = None
            if i == self.size-1:
                if k+1 == self.size:
                    j += 1
                    i = 1
                    k = 1
                    continue
                k += 1
                i = 0
            i += 1
        return table
    
    def down(self, table):
        i = self.size-2
        k = i
        j = 0
        while j < self.size:
            if table[i+1][j] is None:
                table[i+1][j] = table[i][j]
                table[i][j] = None
            if i == 0:
                if k == 0:
                    j += 1
                    i = self.size-2
                    k = i
                    continue
                k -= 1
                i = self.size - 1
            i -= 1
        return table
    
    def left(self, table):
        i = 1
        k = 1
        j = 0
        while j < self.size:
            if table[j][i-1] is None:
                table[j][i-1] = table[j][i]
                table[j][i] = None
            if i == self.size-1:
                if k+1 == self.size:
                    j += 1
                    i = 1
                    k = 1
                    continue
                k += 1
                i = 0
            i += 1
        return table
                    
    def right(self, table):
        i = self.size-2
        k = i
        j = 0
        while j < self.size:
            if table[j][i+1] is None:
                table[j][i+1] = table[j][i]
                table[j][i] = None
            if i == 0:
                if k == 0:
                    j += 1
                    i = self.size-2
                    k = i
                    continue
                k -= 1
                i = self.size - 1
            i -= 1
        return table

class PriorityQueue:
    """ O(1) access to the lowest-priority item """
    def  __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0

    def update(self, item, priority):
        # If item already in priority queue with higher priority, update its priority and rebuild the heap.
        for index, (p, c, i) in enumerate(self.heap):
            if i == item:
                if p <= priority:
                    break
                del self.heap[index]
                self.heap.append((priority, c, item))
                heapq.heapify(self.heap)
                break
        else:
            self.push(item, priority)

def A_star(problem:Tile_Tilting):
    frontier = PriorityQueue()
    explored_set = set()
    frontier.push(State(problem.initial), problem.hu(problem.initial))
    explored_set.add(str(problem.initial))
    
    while not frontier.isEmpty():
        curr = frontier.pop()
        if problem.goal_test(curr.table):
            return curr
        
        explored_set.add(str(curr.table))
        c = problem.result(curr.table)
        for state in c:
            # print(len(c))
            h = problem.hu(state) + curr.g
            state = State(state, parent=curr, g=curr.g)
            if str(state.table) not in explored_set:
                explored_set.add(str(state.table))
                
                frontier.push(state, h)

initial = [[None, "r", None, None],
           ["r", "g", "y", "b"],
           [None, "b", None, None],
           [None, "y", "r", None]]

goal = [["y", "r", "b", "r"],
        [None, None, "y", "r"],
        [None, None, None, "g"],
        [None, None, None, "b"]]

t = Tile_Tilting(initial, goal, 4)
a = State(initial)
result = A_star(t)
print(result.table)
# while result.parent:
#     print(result.table)
#     print()
#     result = result.parent