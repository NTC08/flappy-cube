import pygame
import random
from sys import exit

v = -5
dead = 0
score = 0
start = 0

pygame.init()
screen = pygame.display.set_mode((400, 700))
pygame.display.set_caption("Flappy Cube")
Clock = pygame.time.Clock()
sky = pygame.image.load("flappy-bird/sky.png").convert_alpha()
bird = pygame.image.load("flappy-bird/bird_up.png").convert_alpha()
pipe_up = pygame.image.load("flappy-bird/pipe_up.png").convert_alpha()
pipe_down = pygame.image.load("flappy-bird/pipe_down.png").convert_alpha()
pygame.display.set_icon(bird)

#text
font = pygame.font.Font(None, 70)
font2 = pygame.font.Font(None, 30)
text = font.render("GAME OVER", False, "Red")
text_rec = text.get_rect(center = (200,300))
over_text = font2.render("press space to try again", False, "Red")
over_text_rec = text.get_rect(center = (250,350))
start_text = font2.render("press space to start", False, "Red")
start_text_rec = text.get_rect(center = (250,350))
flap_text = font.render("Flappy Bird", False, "Red")
flap_text_rec = text.get_rect(center = (210,300))

#bird
bird_rec = bird.get_rect(topleft = (100,350))
bird_frame = 2

#pipes
q = random.randint(200,600)
pipe_up_rec = pipe_up.get_rect(midtop = (400,q))
pipe_down_rec = pipe_down.get_rect(midbottom = (400,q - 170))

w = random.randint(200,600)
pipe_up_rec2 = pipe_up.get_rect(midtop = (700,w))
pipe_down_rec2 = pipe_down.get_rect(midbottom = (700,w - 170))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            
            if pygame.key.get_focused() and pygame.key.get_pressed()[pygame.K_SPACE]:
                if bird_rec.top > 0 and dead == 0:
                    v = -4
                elif dead == 1:
                    bird_rec.y = 350
                    dead = 0
                    v = -4
                    pipe_down_rec.x = 400
                    pipe_up_rec.x = 400
                    q = random.randint(200,600)
                    pipe_up_rec = pipe_up.get_rect(midtop = (400,q))
                    pipe_down_rec = pipe_down.get_rect(midbottom = (400,q - 170))
                    
                    w = random.randint(200,600)
                    pipe_up_rec2 = pipe_up.get_rect(midtop = (700,w))
                    pipe_down_rec2 = pipe_down.get_rect(midbottom = (700,w - 170))
                    score = 0
    
    if v <= 0:
        bird_frame = 1
    elif v >= 0:
        bird_frame = 2
        
    if start == 1:
        if bird_rec.colliderect(pipe_up_rec) or bird_rec.colliderect(pipe_down_rec) or bird_rec.colliderect(pipe_up_rec2) or bird_rec.colliderect(pipe_down_rec2):
            dead = 1
        if bird_rec.bottom > 700:
            dead = 1
        
        if dead == 1:
            bird_frame = 3
            
        if bird_frame == 1:
            bird = pygame.image.load('flappy-bird/bird_up.png').convert_alpha()
        elif bird_frame == 2:
            bird = pygame.image.load('flappy-bird/bird_down.png').convert_alpha()
        elif bird_frame == 3:
            bird = pygame.image.load('flappy-bird/bird_die.png').convert_alpha()
            
        if dead == 0:
            bird_rec.y += v
            v = v + 0.2
            pipe_up_rec.x -= 2
            pipe_down_rec.x -= 2
            pipe_up_rec2.x -= 2
            pipe_down_rec2.x -= 2
    
        if pipe_down_rec.x == bird_rec.x or pipe_down_rec2.x == bird_rec.x:
            score = score + 1
        if pipe_down_rec.x < -150:
            q = random.randint(200,600)
            pipe_up_rec = pipe_up.get_rect(midtop = (500,q))
            pipe_down_rec = pipe_down.get_rect(midbottom = (500,q - 200))
    
        if pipe_down_rec2.x < -150:
            w = random.randint(200,600)
            pipe_up_rec2 = pipe_up.get_rect(midtop = (500,w))
            pipe_down_rec2 = pipe_down.get_rect(midbottom = (500,w - 200))
    
    
        if dead == 0:
            screen.blit(sky,(0,0))
            screen.blit(bird,(bird_rec))
        
            screen.blit(pipe_up,(pipe_up_rec))
            screen.blit(pipe_down,(pipe_down_rec))
        
            screen.blit(pipe_up,(pipe_up_rec2))
            screen.blit(pipe_down,(pipe_down_rec2))
        
            score_text = font.render(str(score), False, "black")
            score_rec = score_text.get_rect(center = (200,63))
            screen.blit(score_text,(score_rec))
    
        elif dead == 1:
            screen.blit(text,(text_rec))
            screen.blit(over_text,(over_text_rec))
            screen.blit(bird,(bird_rec))
    else:
        screen.blit(sky,(0,0))
        screen.blit(start_text,(start_text_rec))
        screen.blit(flap_text,(flap_text_rec))
        if pygame.key.get_focused() and pygame.key.get_pressed()[pygame.K_SPACE]:
            start = 1
            
    
    pygame.display.update()
    Clock.tick(60)