import pygame
import random

player_group = pygame.sprite.Group()
block_group = pygame.sprite.Group()
ghost_group = pygame.sprite.Group()
attacker_group = pygame.sprite.Group()
enemy_projectile_group = pygame.sprite.Group()



class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self, player_group)
        self.image = pygame.Surface((50,50))
        self.image.fill("lightblue")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.ghost = Ghost(x, y, 50, 50)
        
        
    def player_move(self, speed=5):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.ghost.rect.x -= speed
            ghost_collisions = check_collision(self.ghost, block_group)
            if ghost_collisions == 0:     
                self.rect.x -= speed
            else:
                self.ghost.rect.x += speed

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.ghost.rect.x += speed
            ghost_collisions = check_collision(self.ghost, block_group)
            if ghost_collisions == 0:     
                self.rect.x += speed
            else:
                self.ghost.rect.x -= speed
                
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.ghost.rect.y -= speed
            ghost_collisions = check_collision(self.ghost, block_group)
            if ghost_collisions == 0:     
                self.rect.y -= speed
            else:
                self.ghost.rect.y += speed
                
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.ghost.rect.y += speed
            ghost_collisions = check_collision(self.ghost, block_group)
            if ghost_collisions == 0:     
                self.rect.y += speed
            else:
                self.ghost.rect.y -= speed
    def update(self):
        self.player_move()

        
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
        self.image.fill("gray")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        

class Attacker(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self, attacker_group)
        self.image = pygame.Surface((25,25))
        self.image.fill("crimson")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.direction = 1
        self.start_x = x


    def move_attacker(self):
        self.rect.x += 2 * self.direction
        if self.rect.x >= 600:
            self.direction = -1
        elif self.rect.x <= 200:
            self.direction = 1

    
    def attack(self):
        shoot_possible = random.randint(0,30)
        speed = random.randint(1,4)
        if shoot_possible == 5:
            Bullet(self.rect.x, self.rect.y, (0,1), speed)
 
        
    
    def update(self):
        self.attack()
        enemy_projectile_group.update()


    


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, speed=3):
        pygame.sprite.Sprite.__init__(self, enemy_projectile_group)
        self.image = pygame.Surface((5,10))
        self.image.fill("red")
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.direction = direction
        self.speed = speed
        self.start = (x,y)
        
    def move_bullet(self):
        self.rect.x += self.speed *  self.direction[0]
        self.rect.y += self.speed * self.direction[1]
        if abs(self.rect.x - self.start[0]) > 1000:
            self.kill()
        elif abs(self.rect.y - self.start[1])> 1000:
            self.kill()
        
        if check_collision(self, player_group) >= 1:
            self.kill()

    def update(self):
        self.move_bullet()



def check_collision(mover: pygame.sprite.Sprite, group: pygame.sprite.Group):
    collisions = pygame.sprite.spritecollide(mover, group, dokill=False)
    if collisions != None:
        return len(collisions)
    else: 
        return 0