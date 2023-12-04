import pygame
import math
import numpy as np



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
        print(obs_points)
        print(obs_distances)


        if closest_obs is not None and closest_obs[1] < self.min_obs_dist and self.count_down > 0:
            self.count_down -= dt
            self.move_left()
        else:
            self.count_down = 2
            self.move_forward()

        # Check if the robot has completed the desired rotation
        if self.count_down <= 0:
            self.count_down = 0  # Reset the countdown
            self.vr = 0  # Stop the right wheel
            self.vl = 0  # Stop the left wheel
                        
    def move_forward(self):
        self.vr = self.maxspeed
        self.vl = self.maxspeed

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
        sensors = {
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
                        sensors["s1"] = point[1]
                    elif i == 1:
                        sensors["s2"] = point[1]
                    elif i == 2:
                        sensors["s3"] = point[1]
                    elif i == 3:
                        sensors["s4"] = point[1]
                    elif i == 4:
                        sensors["s5"] = point[1]

        return sensors
        

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

            
         
    
         