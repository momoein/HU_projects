from sort import *
from data_structure import OpenHashTable



class Team:
    def __init__(self, name):
        self.name = name
        self.p = 0
        self.games_c = 0
        self.nw = 0 # number of win
        self.nl = 0 # number of loss
        self.ne = 0 # number of equally
        self.gd = 0
        self.g_zade = 0
        self.g_khorde = 0

    def update_details(self, zade, khorde):
        self.g_zade += zade
        self.g_khorde += khorde
        self.gd = self.g_zade - self.g_khorde
        # 
        if zade > khorde:
            self.nw += 1
        elif zade < khorde:
            self.nl += 1
        else:
            self.ne += 1
        #
        self.p = (self.nw * 3) + (self.ne * 1) + (self.nl * 0)
        self.games_c += 1

    def show(self):
        form = (
            self.name,
            f"{self.p}p,",
            f"{self.games_c}g",
            f"({self.nw}-{self.ne}-{self.nl}),",
            f"{self.gd}gd",
            f"({self.g_zade}-{self.g_khorde})"
        )
        # print(form)
        return form



class Tournament:
    def __init__(self, name, names_list, results):
        self.name = name
        self.teams = self.initial(names_list, results)


    def initial(self, names_list, results):
        teams = self.build_table(names_list)
        self.initial_result(results, teams)
        array = [teams[i] for i in teams]
        return array
    

    def build_table(self, array):
        table = OpenHashTable(len(array)) # my lovely hash table
        for team in array:
            table.update(team, Team(team))
        return table


    def initial_result(self, results, table):
        for i in results:
            self.add_result(i, table)


    def add_result(self, result, table):
        t1, t2 = self.detect_result(result)
        team1 = table[t1[0]]
        team2 = table[t2[0]]
        team1.update_details(t1[1], t1[2])
        team2.update_details(t2[1], t2[2])


    def detect_result(self, result):
        result = result.split('#')
        team1 = (
            result[0], # name 
            int(result[1].split("@")[0]), # zade
            int(result[1].split("@")[1]), # khorde
        )
        team2 = (
            result[2], # name
            int(result[1].split("@")[1]), # zade
            int(result[1].split("@")[0]), # khorde
        )
        return team1, team2

    
    def sort_teams(self):
        array = self.teams
        # sort by less game count
        array = radix_sort(array, key=lambda x: x.games_c)
        # sort by most goals scored
        array = list(reversed(radix_sort(array, key=lambda x: x.g_zade)))
        # sort by most win
        array = list(reversed(radix_sort(array, key=lambda x: x.nw)))
        # sort by most points
        array = list(reversed(radix_sort(array, key=lambda x: x.p)))
        self.teams = array

    def show(self):
        print(self.name)
        rank = 1
        for i in self.teams:
            print(f"{rank})", *i.show())
            rank += 1
