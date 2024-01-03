import pygame
from fuzzy_expert.variable import FuzzyVariable
from p import Graphic, Robot , Ultrasonic
from fuzzy_expert.rule import FuzzyRule

## implementing fuzzy logic##
variables = {
    "s1": FuzzyVariable(
        universe_range=(46, 120),
        terms={
            "Far": [(range(120,100), 0.9), (range(100,80), 0.7), (range(80,60), 0.5), (range(60,40), 1)],
            "Close": [(range(60,40), 1), (range(80,60), 0.8), (range(100,80), 0.5), (range(100,200), 0.2)],
        },
    ),
    "s2": FuzzyVariable(
       universe_range=(46, 120),
        terms={
            "Far": [(range(120,100), 0.9), (range(100,80), 0.7), (range(80,60), 0.5), (range(60,40), 1)],
            "Close": [(range(60,40), 1), (range(80,60), 0.8), (range(100,80), 0.5), (range(100,200), 0.2)],
        },
    ),
    #
    "s3": FuzzyVariable(
        universe_range=(46, 120),
        terms={
            "Far": [(range(120,100), 0.9), (range(100,80), 0.7), (range(80,60), 0.5), (range(60,40), 1)],
            "Close": [(range(60,40), 1), (range(80,60), 0.8), (range(100,80), 0.5), (range(100,200), 0.2)],
        },
    ),
    #
    "s4": FuzzyVariable(
        universe_range=(46, 120),
        terms={
            "Far": [(range(120,100), 0.9), (range(100,80), 0.7), (range(80,60), 0.5), (range(60,40), 1)],
            "Close": [(range(60,40), 1), (range(80,60), 0.8), (range(100,80), 0.5), (range(100,200), 0.2)],
        },
    ),
    "s5": FuzzyVariable(
        universe_range=(46, 120),
        terms={
            "Far": [(range(120,100), 0.9), (range(100,80), 0.7), (range(80,60), 0.5), (range(60,40), 1)],
            "Close": [(range(60,40), 1), (range(80,60), 0.8), (range(100,80), 0.5), (range(100,200), 0.2)],
        },
    ),
    "decision": FuzzyVariable(
        universe_range=(0, 10),
        terms={
            "Left": [(5, 0), (6, 0.3), (7, 0.7), (8, 1)],
            "Right": [(2, 1), (3, 0.7), (4, 0.3), (5, 0)],
            "Stop": [(3, 0.1), (4, 0.3), (5, 0.6), (8, 0)],
        },
    ),
}

rules = [
    FuzzyRule(
        premise=[
            ("s1", "Far"),
            ("AND", "s2", "Far"),
            ("AND", "s3", "Far"),
            ("AND", "s4", "Far"),
            ("AND", "s5", "Far"),
        ],
        consequence=[("decision", "Forward")],
    ),
    FuzzyRule(
    premise=[
        ("s1", "Close"),
        ("AND", "s2", "Close"),
        ("AND", "s3", "Close"),
        ("AND", "s4", "Close"),
        ("AND", "s5", "Close"),
    ],
    consequence=[("decision", "Stop")],
),
    
]





    
    
## end// implementing fuzzy logic##





Map = (600 , 1200)

gtx = Graphic(Map , "sosk.png" , "maze2.png")

start = (100 , 100)

robot = Robot(start , 0.01 * 3779.52)

sensor_range = 120

ultra = Ultrasonic(sensor_range , gtx.map)  

dt = 0
last_time = pygame.time.get_ticks()

runnin = True


while runnin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnin = False
            
            
    dt = (pygame.time.get_ticks()-last_time)/1000
    last_time = pygame.time.get_ticks()
    
    gtx.map.blit(gtx.map_img , (0,0))
    robot.kinameter(dt)
    
    gtx.drwa_robot(robot.x , robot.y , robot.heading)
    
    point_cloud = ultra.seenc_obs(robot.x , robot.y , robot.heading)
    robot.avoid_distance(point_cloud , dt)
    gtx.draw_sensor_data(point_cloud)
    
    pygame.display.update()