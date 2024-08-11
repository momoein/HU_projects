# import setup
def add_nth_parent_dir_to_syspath(n=0, display=False):
    import os
    import sys
    def nth_parent_dir(n):
        """default n=0 means current directory"""
        path = os.path.dirname(os.path.realpath(__file__))
        for _ in range(n):
            path = os.path.dirname(path)
        return path
    
    dir = nth_parent_dir(n)
    print(dir) if display else None
        
    if dir not in sys.path:
        sys.path.append(dir)

add_nth_parent_dir_to_syspath(n=1)


import numpy as np
import random
from copy import deepcopy

from tools.problem import Problem
from tools.search import aStar_search



class RubikCube(Problem):
    def __init__(self, initial) -> None:
        self.initial = initial
        self.sides = dict(
            # face to face
            white=dict(up="red", down="orange", left="green", right="blue"), 
            yellow=dict(up="red", down="orange", left="blue", right="green"), 
            # face to face
            blue=dict(up="yellow", down="white", left="red", right="orange"), 
            green=dict(up="yellow", down="white", left="orange", right="red"),
            # face to face
            red=dict(up="yellow", down="white", left="green", right="blue"),  
            orange=dict(up="yellow", down="white", left="blue", right="green")
        )

    @staticmethod
    def make_rubik():
        names = ['white', 'yellow', 'red', 'blue', 'green', 'orange']
        rubik = {}
        for name in names:
            arr = [f"{name[0].upper()}-{i}" for i in range(1, 3**2 + 1)]
            rubik[name] = np.array(arr, dtype=str).reshape(3, 3)
        return rubik
    
    def goal_test(self, state: dict) -> bool:
        for side in state:
            center_color = side[0].upper()
            side_items = state[side].reshape(
                state[side].shape[0] * state[side].shape[1]
            )
            if any(map(lambda x : x[0] != center_color, side_items)):
                return False
        return True

    def actions(self, state: dict) -> list[tuple]:
        colors = list(state.keys())
        rotations = ["L", "R"]
        acts = []
        for color in colors:
            for rotate in rotations:
                acts.append((color, rotate))
        return acts
        

    def result(self, state, action) -> dict:
        new_state = deepcopy(state)
        self.rubik_rotate(new_state, *action)
        return new_state

    def heuristic(self, state) -> int:
        """num of incomplete surface """
        num_wrongs = 0
        for side in state:
            center_color = side[0].upper()
            side_items = state[side].reshape(
                state[side].shape[0] * state[side].shape[1]
            )
            num_wrongs += any(map(lambda x : x[0] != center_color, side_items))
        return num_wrongs
        
    def h(self, node) -> int:
        return self.heuristic(node.state)
    
    def reverse_arr(self, arr):
        n = len(arr)
        copy = arr.copy()
        for i in range(n//2):
            copy[i], copy[n-i-1] = copy[n-i-1], copy[i]
        return copy
    
    def twod_array_rotate(self, array, rotate="L"):
        """rotate : 'L' or 'R' 
        array : np.array with shape (x, x)
        """
        shape = array.shape
        if len(shape) != 2 or shape[0] != shape[1]:
            raise f"array.sahpe : {array}, All axes must be the same"
        if rotate not in ["L", "R"]:
            raise "rotate must be 'L' or 'R' "
        
        surface = array
        surcopy = surface.copy()
        n = array.shape[0]
        for i in range(n):
            if rotate == "R":
                # Right rotate
                surface[i] = self.reverse_arr(surcopy[:, i])
            elif rotate == "L":
                # Left rotate
                surface[: , i] = self.reverse_arr(surcopy[i])

        return surface
    
    def advers_side(self, color, side):
        target_color = self.sides[color][side]
        for key, val in self.sides[target_color].items():
            if val == color:
                return key

    def get_side_row(self, array, side):
        arr = array.copy()
        if side == "up":
            return arr[0, :]
        if side == "down":
            return arr[2, :]
        if side == "left":
            return arr[:, 0]
        if side == "right":
            return arr[:, 2]

    def set_side_row(self, _2d_array, array, side: str):
        if side == "up":
            _2d_array[0, :] = array
        if side == "down":
            _2d_array[2, :] = array
        if side == "left":
            _2d_array[:, 0] = array
        if side == "right":
            _2d_array[:, 2] = array

    def rubik_rotate(self, rubik, color: str, rotate: str):
        """choose between 
        colors: 'white', 'yellow', 'red', 'blue', 'green', 'orange'
        rotate: 'L' or 'R' 
        """
        rubik[color] = self.twod_array_rotate(rubik[color], rotate)
        
        up = self.get_side_row(rubik[self.sides[color]["up"]], side=self.advers_side(color=color, side="up"))
        down = self.get_side_row(rubik[self.sides[color]["down"]], side=self.advers_side(color=color, side="down"))
        left = self.get_side_row(rubik[self.sides[color]["left"]], side=self.advers_side(color=color, side="left"))
        right = self.get_side_row(rubik[self.sides[color]["right"]], side=self.advers_side(color=color, side="right"))

        if rotate == "L":
            self.set_side_row(rubik[self.sides[color]["up"]], array=left, 
                              side=self.advers_side(color=color, side="up"))
            self.set_side_row(rubik[self.sides[color]["right"]], array=up, 
                              side=self.advers_side(color=color, side="right"))
            self.set_side_row(rubik[self.sides[color]["down"]], array=right, 
                              side=self.advers_side(color=color, side="down"))
            self.set_side_row(rubik[self.sides[color]["left"]], array=down, 
                              side=self.advers_side(color=color, side="left"))
            
        elif rotate == "R":
            self.set_side_row(rubik[self.sides[color]["up"]], array=right, 
                              side=self.advers_side(color=color, side="up"))
            self.set_side_row(rubik[self.sides[color]["right"]], array=down, 
                              side=self.advers_side(color=color, side="right"))
            self.set_side_row(rubik[self.sides[color]["down"]], array=left, 
                              side=self.advers_side(color=color, side="down"))
            self.set_side_row(rubik[self.sides[color]["left"]], array=up, 
                              side=self.advers_side(color=color, side="left"))

    
    def shuffle_actions(self, n=10):
        colors = ['white', 'yellow', 'red', 'blue', 'green', 'orange']
        rotations = ["L", "R"]
        shuffled_movements = []
        for _ in range(n):
            color = random.choice(colors)
            rotate = random.choice(rotations)
            shuffled_movements.append((color, rotate))
        return shuffled_movements
    
    def shuffle_rubik(self, state, n=5):
        for action in self.shuffle_actions(n):
            self.rubik_rotate(state, *action)

    def display(self, rubik):
        for key, val in rubik.items():
            print(key)
            print(val)




## initial the problem
problem = RubikCube(initial=RubikCube.make_rubik())
random_actions = problem.shuffle_rubik(problem.initial, 4)


## A* search
res = aStar_search(problem, wight=1, display=False)
path = res.path()

print("path length:", len(path))
for i, node in enumerate(path):
    print(f"\nstep {i}")
    print("action:", node.action)
    problem.display(node.state)