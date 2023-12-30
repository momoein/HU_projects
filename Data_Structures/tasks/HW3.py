
class Team:
    def __init__(self, name):
        self.name = name
        self.p = 0
        self.games_c = 0
        self.nwle = [0, 0, 0] # number of (win, loss, equally)
        self.gd = 0
        self.g_zade = 0
        self.g_khorde = 0

    def update_details(self, zade, khorde):
        self.g_zade += zade
        self.g_khorde += khorde
        self.gd = self.g_zade - self.g_khorde
        # 
        if zade > khorde:
            self.nwle[0] += 1
        elif zade < khorde:
            self.nwle[2] += 1
        else:
            self.nwle[1] += 1
        #
        self.p = (self.nwle[0] * 3) + (self.nwle[1] * 1) + (self.nwle[2] * 0)
        self.games_c += 1

    def show(self):
        print(
            self.name,
            f"{self.p}p,",
            f"{self.games_c}g",
            f"({self.nwle[0]}-{self.nwle[1]}-{self.nwle[2]}),",
            f"{self.gd}gd",
            f"({self.g_zade}-{self.g_khorde})"
        )

    # def __repr__(self):
    #     return repr((self.name, self.p, self.games_c, self.nwle, self.gd, self.g_zade, self.g_khorde))



def detect_result(result):
    result = result.split('#')
    team1 = {
        "name" : result[0],
        "zade" : int(result[1].split("@")[0]),
        "khorde" : int(result[1].split("@")[1]),
    }
    team2 = {
        "name" : result[2],
        "zade" : int(result[1].split("@")[1]),
        "khorde" : int(result[1].split("@")[0]),
    }
    return team1, team2



def build_table(list):
    table = {}
    for team in teams_list:
        table.update({team : Team(team)})
    return table



def add_result(result, table):
    t1, t2 = detect_result(result)
    team1 = table[t1["name"]]
    team2 = table[t2["name"]]
    team1.update_details(t1["zade"], t1["khorde"])
    team2.update_details(t2["zade"], t2["khorde"])
    


def initial_result(results, table):
    for i in results:
        add_result(i, table)





## __main__

tournament_count = 2
tournament_names = "World Cup 1998 - Group A"
team_count = 4
teams_list = ["Brazil", "Norway", "Morocco", "Scotland"]
games_count = 6
natige = [
    "Brazil#2@1#Scotland",
    "Norway#2@2#Morocco",
    "Scotland#1@1#Norway",
    "Brazil#3@0#Morocco",
    "Morocco#3@0#Scotland",
    "Brazil#1@2#Norway",
]

"""out:
    World Cup 1998 - Group A
    1) Brazil 6p, 3g (2-0-1), 3gd (6-3)
    2) Norway 5p, 3g (1-2-0), 1gd (5-4)
    3) Morocco 4p, 3g (1-1-1), 0gd (5-5)
    4) Scotland 1p, 3g (0-1-2), -4gd (2-6)
    Some strange tournament
    1) Team D 4p, 2g (1-1-0), 1gd (2-1)
    2) Team E 3p, 2g (1-0-1), 0gd (3-3)
    3) Team A 3p, 3g (0-3-0), 0gd (3-3)
    4) Team B 1p, 1g (0-1-0), 0gd (1-1)
    5) Team C 1p, 2g (0-1-1), -1gd (3-4)
"""

"""input:
    2
    World Cup 1998 - Group A
    4
    Brazil
    Norway
    Morocco
    Scotland
    6
    Brazil#2@1#Scotland
    Norway#2@2#Morocco
    Scotland#1@1#Norway
    Brazil#3@0#Morocco
    Morocco#3@0#Scotland
    Brazil#1@2#Norway

    Some strange tournamen
    5
    Team A
    Team B
    Team C
    Team D
    Team E
    5
    Team A#1@1#Team B
    Team A#2@2#Team C
    Team A#0@0#Team D
    Team E#2@1#Team C
    Team E#1@2#Team D
"""



teams = build_table(teams_list)
initial_result(natige, teams)


for i in teams:
    teams[i].show()


def radix_sort(array, digits):
    d = digits
    for i in range(1, d+1):
        array = count_sort_by_digit(array, 9, i)
    return array

def count_sort_by_digit(array, max, digit, key=None):
    key = key if key is not None else lambda x: x
    a, m = array, max
    c = [0 for i in range(m+1)] 
    b = [0 for i in range(len(array) + 1)]
    
    for i in range(len(a)):
        c[which_digit(key(a[i]), digit)] += 1
    
    for i in range(1, len(c)):
        c[i] += c[i-1]
    
    for i in range(len(a)-1, -1, -1):
        b[c[which_digit(key(a[i]), digit)]] = a[i]
        c[which_digit(key(a[i]), digit)] -= 1

    return b[1:]

def which_digit(integer, digit):
    base =  10 ** (digit)
    integer %= base
    base /= 10
    return int(integer // base)



test = [teams[i] for i in teams]
print(test)




test_p = count_sort_by_digit(test, max=9, digit=1, key=lambda x: x.p)
test_win = count_sort_by_digit(test, max=9, digit=1, key=lambda x: x.nwle[0])
print(test_p)
key = lambda x: x.p
test_p.reverse()
for i in test_p:
    print(key(i))

print(test_win)
key = lambda x: x.nwle[0]
test_win.reverse()
for i in test_win:
    print(key(i))