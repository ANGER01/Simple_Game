import pygame

 

class Player:
    def __init__(self, x, y):
        self.body = pygame.Rect(x, y, 50 , 50)
        self.ghost = pygame.Rect(x, y, 50 , 50)
        
    def player_move(self, keys, hittable_objects: list, speed=5):
    
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
        collisions = mover.collidelistall(all_rects)
        
        return len(collisions)