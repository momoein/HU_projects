import pygame
import math
import numpy as np
from fuzzy_expert.variable import FuzzyVariable
from fuzzy_expert.rule import FuzzyRule
from fuzzy_expert.inference import DecompositionalInference



def distance(point1, point2):
    point1 = np.array(point1)
    point2 = np.array(point2)
    return np.linalg.norm(point1-point2)



class Graphic :
    def __init__(self , dimentions , sosk_image_path ,map_img_path  ) -> None:
        pygame.init()
        
        self.black = (0,0,0)
        self.white = (255,255,255)
        self.green = (0,255,0)
        self.blue = (0,0,255)
        
        self.red = (255 , 0 , 0)
        self.yel = (255 , 255 , 0)
        
        self.sosk = pygame.image.load(sosk_image_path)
        self.map_img = pygame.image.load(map_img_path)
        
        self.height , self.width = dimentions
        
        self.map = pygame.display.set_mode((self.width , self.height))
        self.map.blit(self.map_img , (0,0))
        
        
    def drwa_robot(self,x,y,heading):
        rotate = pygame.transform.rotozoom(self.sosk , math.degrees(heading) ,1)
        rect = rotate.get_rect(center=(x,y))
        self.map.blit(rotate , rect)
        
    
    def draw_sensor_data(self, point_cloud):
        point_cloud, _ = point_cloud
        for point in point_cloud:
            if len(point) > 0:
                pygame.draw.circle(self.map , self.red , point , 3 ,0)
            


### changes
class Robot:
    def __init__(self , startpos , width) -> None:
        self.mp2 = 3779.52
        self.w = width
        self.x = startpos[0]
        self.y = startpos[1]
        
        self.heading = 0
        
        self.vl = 0.01*self.mp2
        self.vr = 0.01*self.mp2
        
        self.maxspeed = 0.02*self.mp2
        self.minspeed = 0.01*self.mp2
        
        self.min_obs_dist = 50
        self.count_down = 2
        
        
    def avoid_distance(self, point_cloud, dt):
        
        threshold_left = 0.6
        threshold_right = 0.6
        threshold_stop = 0.6


        closest_obs = None
        dist = np.inf
        points, _ = point_cloud

        if len(points) > 1:
            for point in points:
                if len(point) > 0:
                    if dist > distance([self.x, self.y], point):
                        dist = distance([self.x, self.y], point)
                        closest_obs = (point, dist)

        # get obs point and distance from each sensor
        obs_points = self.sensor_detect(point_cloud)
        obs_distances = obs_points.copy()

        for point in obs_distances:
            if obs_distances[point] is not None:
                obs_distances[point] = distance([self.x, self.y], obs_distances[point])


        if closest_obs is not None and closest_obs[1] < self.min_obs_dist and self.count_down > 0:
                obs_points = self.sensor_detect(point_cloud)
                obs_distances = obs_points.copy()
                

                for sensor in obs_distances:
                    if obs_distances[sensor] is not None:
                       obs_distances[sensor] = distance([self.x, self.y], obs_distances[sensor])
                    print(obs_distances[sensor])

                variables = {
                    "s1": FuzzyVariable(
                    universe_range=(46, 200),
                    terms={
                        "Close": [(175, 0), (180, 0.2), (185, 0.7), (190, 1)],
                        "Far": [(155, 1), (160, 0.8), (165, 0.5), (170, 0.2), (175, 0)],
                    },
                ),
                    "s2": FuzzyVariable(
                    universe_range=(46, 200),
                    terms={
                        "Close": [(175, 0), (180, 0.2), (185, 0.7), (190, 1)],
                        "Far": [(155, 1), (160, 0.8), (165, 0.5), (170, 0.2), (175, 0)],
                    },
                ),
                    "s3": FuzzyVariable(
                    universe_range=(46, 200),
                    terms={
                        "Close": [(175, 0), (180, 0.2), (185, 0.7), (190, 1)],
                        "Far": [(155, 1), (160, 0.8), (165, 0.5), (170, 0.2), (175, 0)],
                    },
                ),
                    "s4": FuzzyVariable(
                    universe_range=(46, 200),
                    terms={
                        "Close": [(175, 0), (180, 0.2), (185, 0.7), (190, 1)],
                        "Far": [(155, 1), (160, 0.8), (165, 0.5), (170, 0.2), (175, 0)],
                    },
                ),
                    "s5": FuzzyVariable(
                    universe_range=(46, 200),
                    terms={
                        "Close": [(175, 0), (180, 0.2), (185, 0.7), (190, 1)],
                        "Far": [(155, 1), (160, 0.8), (165, 0.5), (170, 0.2), (175, 0)],
                    },
                ),
                
                    "decision": FuzzyVariable(
                    universe_range=(0, 10),
                    terms={
                        "Left": [(5, 0), (6, 0.3), (7, 0.7), (8, 1)],
                        "Right": [(2, 1), (3, 0.7), (4, 0.3), (5, 0)],
                        "Stop": [(3, 0.1), (4, 0.3), (5, 0.6), (8, 0)],
                        "Forward": [(0, 0), (1, 0.3), (2, 0.7), (3, 1)],
                }
                ),
            }
                rules = [
                    FuzzyRule(
                    cf = 0.9,
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
                    ("s1" , 'Close'),
                    ("AND", "s2", "Close"),
                    ("AND", "s3", "Close"),
                    ("AND", "s4", "Close"),
                    ("AND", "s5", "Close"),
                ],
                consequence=[("decision", "Stop")],
                ),
    
                ]
                
                model = DecompositionalInference(
                    and_operator="min",
                    or_operator="max",
                    implication_operator="Rc",
                    composition_operator="max-min",
                    production_link="max",
                    defuzzification_operator="cog",
                )
               

            # Move fuzzy inference logic inside this block
                decision_output = model(variables=variables, rules=rules)
                decision_labels = decision_output[0]
                print(decision_output)

                threshold_left = 0.6
                threshold_right = 0.6
                threshold_stop = 0.6

                if decision_labels['Left'] > threshold_left:
                    self.move_left()
                    print('go left')
                elif decision_labels['Right'] > threshold_right:
                    self.move_right()
                    print('go rigt')
                elif decision_labels['Stop'] > threshold_stop:
                    self.move_stop()
                else:
                    self.move_forward()
                    print('go forward')
        
                        
    def move_forward(self):
        self.vr = self.maxspeed
        self.vl = self.maxspeed
       
        
    def move_stop(self):
        if self.count_down <= 0:
            self.count_down = 0  # Reset the countdown
            self.vr = 0  # Stop the right wheel
            self.vl = 0  # Stop the left wheel

    # left rotation
    def move_left(self):
        self.vr = self.minspeed/2
        self.vl = - self.minspeed/2
    # right rotation
    def move_right(self):
        self.vr = - self.minspeed/2
        self.vl = self.minspeed/2

    def sensor_detect(self, point_cloud):
        start_angle = self.heading - math.radians(90)  
        finish_angle = self.heading + math.radians(136)
        linspace = np.linspace(start_angle, finish_angle, 5, False)

        _, points= point_cloud
        self.sensors = {
            "s1" : None, # -90 degree toward heading
            "s2" : None, # -45 degree toward heading
            "s3" : None, #  0 degree toward heading
            "s4" : None, #  45 degree toward heading
            "s5" : None, #  90 degree toward heading
        }
        # point[0] = radian , point[1] = [x, y]
        for point in points:
            for i in range(len(linspace)):
                if linspace[i] == point[0]:
                    if i == 0:
                        self.sensors["s1"] = point[1]
                    elif i == 1:
                        self.sensors["s2"] = point[1]
                    elif i == 2:
                        self.sensors["s3"] = point[1]
                    elif i == 3:
                        self.sensors["s4"] = point[1]
                    elif i == 4:
                        self.sensors["s5"] = point[1]
        return self.sensors
        

    def kinameter(self , dt):
        self.x += ((self.vl + self.vr)/2) * math.cos(self.heading) * dt
        self.y -= ((self.vl + self.vr)/2) * math.sin(self.heading) * dt
        self.heading += (self.vr - self.vl) / self.w * dt
        
        if self.heading > 2*math.pi or self.heading < -2*math.pi:
            self.heading = 0
            
        self.vr = max(min(self.maxspeed , self.vr) , self.minspeed )
        self.vl = max(min(self.maxspeed , self.vl) , self.minspeed )



class Ultrasonic:
    def __init__(self, sensor_range, map):
        self.sensor_range = sensor_range
        self.map_width, self.map_height = pygame.display.get_surface().get_size()
        self.map = map


    def seenc_obs(self, x, y, heading):
        x1, y1 = x, y
        start_angle = heading - math.radians(90)  
        finish_angle = heading + math.radians(136)
        linspace = np.linspace(start_angle, finish_angle, 5, False)
        obs = []
        obs_with_radian = []
        
        for index in range(len(linspace)):
            x2 = x1 + self.sensor_range * math.cos(linspace[index])
            y2 = y1 - self.sensor_range * math.sin(linspace[index])
            for i in range(1, 100):
                u = i / 100
                x = int(x2 * u + x1 * (1 - u))
                y = int(y2 * u + y1 * (1 - u))
                if 0 < x < self.map_width and 0 < y < self.map_height:
                    color = self.map.get_at((x, y))
                    self.map.set_at((x, y), (0, 208, 255))
                    if (color[0], color[1], color[2]) == (0, 0, 0):
                        obs.append([x, y])
                        obs_with_radian.append([linspace[index], [x, y]])
                        break
                    
        
        return (obs, obs_with_radian)


## implementing fuzzy logic##






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