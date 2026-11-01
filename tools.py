import pygame
import random
import math

player_group = pygame.sprite.Group()
block_group = pygame.sprite.Group()
ghost_group = pygame.sprite.Group()
attacker_group = pygame.sprite.Group()
enemy_projectile_group = pygame.sprite.Group()
hittable_group = pygame.sprite.Group()
player_weapon_group = pygame.sprite.Group()


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self, player_group)
        self.image = pygame.Surface((50,50))
        self.image.fill("lightblue")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.ghost = Ghost(x, y, 50, 50)
        self.attacking = False
        self.health = 10
        self.sword = self.Sword(self, 60)
        
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
                
                
    def check_take_damage(self):
        hits = pygame.sprite.spritecollide(self, enemy_projectile_group, dokill=True)
        for bullet in hits:
            self.health -= bullet.inflict_damage()
            if self.health <= 0:
                self.kill()
                self.sword.kill()

    def attack(self):
        self.attacking = True
        self.sword.swing()
    
    def update(self):
        self.check_take_damage()
        if not self.attacking:
            self.player_move()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.attacking:
            self.attack()
        


    class Sword(pygame.sprite.Sprite):
        def __init__(self, player, radius):
            pygame.sprite.Sprite.__init__(self)

            self.player = player
            self.radius = radius
            self.swinging = False
            self.theta = 0
            
            self.image = pygame.Surface((6,6))
            self.image.fill("white")
            self.rect = self.image.get_rect()
            self.rect.topleft = self.player.rect.center
            self.rect.y -= 50
            self.rect.x -= (radius - 3)

        def swing(self):
            if not self.swinging:
                self.swinging = True
                player_weapon_group.add(self)

        def update(self):
            if self.swinging:
                self.rect.centerx = int(self.player.rect.centerx - self.radius * math.cos(self.theta))
                self.rect.centery = int(self.player.rect.centery - self.radius * math.sin(self.theta))
                
                self.theta += math.radians(10)
                if self.theta >= math.radians(180):
                    self.theta = 0
                    self.swinging = False
                    self.player.attacking = False
                    self.kill()

                    
        def draw(self, screen):
            if self.swinging:
                screen.blit(self.image, (self.rect.x, self.rect.y))  

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
        self.image = pygame.Surface((300, 30))
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
        shoot_possible = random.randint(0,6)
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
        self.damage = 1
        
    def move_bullet(self):
        self.rect.x += self.speed *  self.direction[0]
        self.rect.y += self.speed * self.direction[1]
        if abs(self.rect.x - self.start[0]) > 1000:
            self.kill()
        elif abs(self.rect.y - self.start[1])> 1000:
            self.kill()
        
        if check_collision(self, block_group) >= 1:
            self.kill()
    
    def inflict_damage(self):
        return self.damage
    
    def update(self):
        self.move_bullet()



def check_collision(mover: pygame.sprite.Sprite, group: pygame.sprite.Group):
    collisions = pygame.sprite.spritecollide(mover, group, dokill=False)
    if collisions != None:
        return len(collisions)
    else: 
        return 0