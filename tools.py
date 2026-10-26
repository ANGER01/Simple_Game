import pygame

player_group = pygame.sprite.Group()
block_group = pygame.sprite.Group()
ghost_group = pygame.sprite.Group()

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self, player_group)
        self.image = pygame.Surface((50,50))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.ghost = Ghost(x, y, 50, 50)
        
        
    def player_move(self, speed=5):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.ghost.rect.x -= speed
            ghost_collisions = self.check_collision(self.ghost)
            if ghost_collisions == 0:     
                self.rect.x -= speed
            else:
                self.ghost.rect.x += speed

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.ghost.rect.x += speed
            ghost_collisions = self.check_collision(self.ghost)
            if ghost_collisions == 0:     
                self.rect.x += speed
            else:
                self.ghost.rect.x -= speed
                
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.ghost.rect.y -= speed
            ghost_collisions = self.check_collision(self.ghost)
            if ghost_collisions == 0:     
                self.rect.y -= speed
            else:
                self.ghost.rect.y += speed
                
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.ghost.rect.y += speed
            ghost_collisions = self.check_collision(self.ghost)
            if ghost_collisions == 0:     
                self.rect.y += speed
            else:
                self.ghost.rect.y -= speed
            
    def check_collision(self, mover: pygame.sprite.Sprite):
        collisions = pygame.sprite.spritecollide(mover, block_group, dokill=False)
        if collisions != None:
            return len(collisions)
        else: 
            return 0

        
class Ghost(pygame.sprite.Sprite):
    def __init__(self, x, y, width, heigth):
        pygame.sprite.Sprite.__init__(self, ghost_group)
        self.image = pygame.Surface((width,heigth))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        
class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self, block_group)
        self.image = pygame.Surface((25, 25))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        

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