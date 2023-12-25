import pygame
from movment import Graphic, Robot , Ultrasonic

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