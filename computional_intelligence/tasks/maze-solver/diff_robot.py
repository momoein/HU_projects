import pygame
import math

class Envir:
    def __init__(self, dimentions):
        # colors
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.red = (255, 0, 0)
        self.yel = (255, 255, 0)
        # map dims
        self.height = dimentions[0]
        self.width = dimentions[1]
        # window setting
        pygame.display.set_caption("Differential bot")
        self.map = pygame.display.set_mode((self.width, self.height))
        # text variables
        self.font = pygame.font.Font('freesansbold.ttf', 50)
        self.text = self.font.render('default', True, self.white, self.black)
        self.textRect = self.text.get_rect()
        self.textRect.center = (dimentions[1]-600, dimentions[0]-50)
        # trail
        self.trail_set = []

    def write_info(self, Vl, Vr, theta):
        txt = f"Vl = {Vl} Vr = {Vr} theta = {int(math.degrees(theta))}"
        self.text = self.font.render(txt, True, self.white, self.black)
        self.map.blit(self.text, self.textRect)

    def trail(self, pos):
        for i in range(0, len(self.trail_set)-1):
            pygame.draw.line(self.map, self.yel,
                             (self.trail_set[i][0], self.trail_set[i][1]),
                             (self.trail_set[i+1][0], self.trail_set[i+1][1]))
        if self.trail_set.__sizeof__() > 2000:
            self.trail_set.pop(0)
        self.trail_set.append(pos)

    def robot_frame(self, pos, rotation):
        n = 50
        centerx, centery = pos
        x_axis = (centerx + n*math.cos(-rotation), centery + n*math.sin(-rotation))
        y_axis = (centerx + n*math.cos(-rotation + math.pi/2), 
                  centery + n*math.sin(-rotation + math.pi/2))
        pygame.draw.line(self.map, self.red, (centerx, centery), x_axis, 3)
        pygame.draw.line(self.map, self.green, (centerx, centery), y_axis, 3)
        

class Robot:
    def __init__(self, startpos, robotImg, width):
        self.m2p = 3 # meters 2 pixels
        # robot dims
        self.w = width
        self.x = startpos[0]
        self.y = startpos[1]
        self.theta = 0
        self.vl = 0.01 * self.m2p # meters/s
        self.vr = 0.01 * self.m2p
        self.maxspeed = 0.02 * self.m2p
        self.minspeed = -0.02 * self.m2p
        # graphics 
        self.img = pygame.image.load(robotImg)
        self.rotated = self.img
        self.rect = self.rotated.get_rect(center=(self.x, self.y))

    def draw(self, map):
        map.blit(self.rotated, self.rect)

    def move(self, event=None):
        if event is not None:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP4:
                    self.vl += 0.00001 * self.m2p
                elif event.key == pygame.K_KP6:
                    self.vl -= 0.00001 * self.m2p
                # elif event.key == pygame.K_KP1:
                #     self.vr += 0.0001 * self.m2p
                # elif event.key == pygame.K_KP3:
                #     self.vr -= 0.0001 * self.m2p

        self.x += ((self.vl + self.vr)/2) * math.cos(self.theta) * dt
        self.y -= ((self.vl + self.vr)/2) * math.sin(self.theta) * dt
        self.theta += (self.vr - self.vl) / self.w * dt
        # reset theta
        if self.theta > 2*math.pi or self.theta < -2*math.pi:
            self.theta = 0
        # set max speed
        self.vr = min(self.vr, self.maxspeed)
        self.vl = min(self.vl, self.maxspeed)
        # set min speed
        self.vr = max(self.vr, self.minspeed)
        self.vl = max(self.vl, self.minspeed)

        self.rotated = pygame.transform.rotozoom(self.img,
                                                 math.degrees(self.theta), 1)
        self.rect = self.rotated.get_rect(center=(self.x, self.y))


# initialisation 
pygame.init()

# start position
start = (100, 100)

# dimentions
dims = (600, 1000)
running = True

# the envir
environment = Envir(dims)

# the robot
robot = Robot(start, 
              r"D:\work\university\Huni_projects\computional_intelligence\tasks\maze-solver\car64.png", 
              .2)

# dt 
dt = 0
lasttime = pygame.time.get_ticks()
# simulation loop
while running:
    # activate the quit buttom
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        robot.move(event)
    dt = (pygame.time.get_ticks() - lasttime)/1000
    pygame.display.update()
    environment.map.fill(environment.black)
    robot.move()
    environment.robot_frame((robot.x, robot.y), robot.theta)
    environment.write_info(int(robot.vl), int(robot.vr), robot.theta)
    robot.draw(environment.map)
    environment.trail((robot.x, robot.y))
