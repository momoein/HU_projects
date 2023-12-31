from HW3 import Tournament


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

tournament_names2 = "Some strange tournamen"
team_count2 = 5
teams_list2 = ["Team A", "Team B", "Team C", "Team D", "Team E"]
games_count2 = 5
natige2 = [
    "Team A#1@1#Team B",
    "Team A#2@2#Team C",
    "Team A#0@0#Team D",
    "Team E#2@1#Team C",
    "Team E#1@2#Team D",
]



teams_list = list(reversed(teams_list))
tour = Tournament(tournament_names, teams_list, natige)
tour.sort_teams()
tour.show()

teams_list2 = list(reversed(teams_list2))
tour2 = Tournament(tournament_names2, teams_list2, natige2)
tour2.sort_teams()
tour2.show()




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
