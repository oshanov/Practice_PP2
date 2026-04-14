import pygame
import datetime


class MickeyClock:
    def __init__(self, screen):
        self.screen = screen
        self.bg = pygame.image.load(r"C:\\git_practice\\Practice9\\MickeyClock\\images\\clock_face.png").convert_alpha()
        self.bg = pygame.transform.scale(self.bg, (800, 800))

        self.hand_m = pygame.image.load(r"C:\\git_practice\\Practice9\\MickeyClock\\images\\hand_minutes.png").convert_alpha()
        self.hand_s = pygame.image.load(r"C:\\git_practice\\Practice9\\MickeyClock\\images\\hand_seconds.png").convert_alpha()

        self.hand_m = pygame.transform.scale(self.hand_m, (800, 800)) 
        self.hand_s = pygame.transform.scale(self.hand_s, (800, 800))

        self.angle_m = 0
        self.angle_s = 0

    def updatetime(self):
        now = datetime.datetime.now()
        self.angle_m = -now.minute*6 + 60
        self.angle_s = -now.second*6 

    def drawscreen(self):
        self.screen.blit(self.bg, (0,0))

        rot_m = pygame.transform.rotate(self.hand_m, self.angle_m)
        rect_m = rot_m.get_rect(center=(400, 400))
        self.screen.blit(rot_m, rect_m)

        rot_s = pygame.transform.rotate(self.hand_s, self.angle_s)
        rect_s = rot_s.get_rect(center=(400, 400))
        self.screen.blit(rot_s, rect_s)






# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_ESCAPE:
#                 running = False

    
    
    

#     screen.blit(bg, (0, 0))

    
#     rot_m = pygame.transform.rotate(hand_m, angle_m)
#     rect_m = rot_m.get_rect(center=(400, 400))
#     screen.blit(rot_m, rect_m)

#     rot_s = pygame.transform.rotate(hand_s, angle_s)
#     rect_s = rot_s.get_rect(center=(400, 400))
#     screen.blit(rot_s, rect_s)

#     pygame.display.flip()
#     clock.tick(60)

# pygame.quit()