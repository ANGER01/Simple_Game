import pygame

 

class Player:
    def __init__(self, x, y):
        self.body = pygame.Rect(x, y, 50 , 50)
        self.ghost = pygame.Rect(x, y, 50 , 50)
        
    def player_move(self, hittable_objects: list=None, speed=5):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.ghost.x -= speed
            ghost_collisions = self.check_collision(self.ghost, hittable_objects)
            if ghost_collisions == 0:     
                self.body.x -= speed
            else:
                self.ghost.x += speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.ghost.x += speed
            ghost_collisions = self.check_collision(self.ghost, hittable_objects)
            if ghost_collisions == 0:     
                self.body.x += speed
            else:
                self.ghost.x -= speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.ghost.y -= speed
            ghost_collisions = self.check_collision(self.ghost, hittable_objects)
            if ghost_collisions == 0:     
                self.body.y -= speed
            else:
                self.ghost.y += speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.ghost.y += speed
            ghost_collisions = self.check_collision(self.ghost, hittable_objects)
            if ghost_collisions == 0:     
                self.body.y += speed
            else:
                self.ghost.y -= speed
            
    def check_collision(self, mover: pygame.Rect, all_rects: list):
        if all_rects != None:
            collisions = mover.collidelistall(all_rects)
            return len(collisions)
        else: 
            return 0
    
    def draw(self, screen):
        pygame.draw.rect(screen, (255,255,255), self.body)
        
    def update():
        pass
        



class Attacker:
    def __init__(self, x, y):
        self.body = pygame.Rect(x, y)
        pass
    
    def draw(self, screen):
        pass
    
    def update(self):
        pass
    


class Bullet:
    def __init__(self, x, y, direction, speed=3):
        self.body = pygame.Rect(x, y, 5, 5)
        self.direction = direction
        self.speed = speed
        
    def draw(self, screen):
        pass
    
    def update(self):
        pass