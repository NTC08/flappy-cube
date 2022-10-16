import pygame
import random
from sys import exit

v = -5
dead = 0
score = 0
start = 0
run = 1
between = 200

f = open("flappy-bird/score.data", "a")
f = open("flappy-bird/score.data", "r")
try:
    high_score = int(f.read())
    f.close()
except:
    f = open("flappy-bird/score.data", "w")
    f.write("0")
    high_score = int(f.read())
    
pygame.init()
screen = pygame.display.set_mode((400, 700))
pygame.display.set_caption("Flappy Cube")
Clock = pygame.time.Clock()
sky = pygame.image.load("flappy-bird/sky.png").convert_alpha()
bird = pygame.image.load("flappy-bird/bird_up.png").convert_alpha()
pipe_up = pygame.image.load("flappy-bird/pipe_up.png").convert_alpha()
pipe_down = pygame.image.load("flappy-bird/pipe_down.png").convert_alpha()
pause_ = pygame.image.load("flappy-bird/pause.png").convert_alpha()
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
h = font2.render("high score = " + str(high_score), False, "Black")
h_rec = h.get_rect(center = (200,90))

#score

#bird
bird_rec = bird.get_rect(topleft = (100,350))
bird_frame = 2

#pipes
q = random.randint(250,600)
pipe_up_rec = pipe_up.get_rect(midtop = (400,q))
pipe_down_rec = pipe_down.get_rect(midbottom = (400,q - between))

w = random.randint(250,600)
pipe_up_rec2 = pipe_up.get_rect(midtop = (700,w))
pipe_down_rec2 = pipe_down.get_rect(midbottom = (700,w - between))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            f = open("flappy-bird/score.data", "r")
            if int(f.read()) < high_score:
                f = open("flappy-bird/score.data", "w")
                f.write(str(high_score))
                f.close()
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            
            if pygame.key.get_focused() and pygame.key.get_pressed()[pygame.K_SPACE]:
                if bird_rec.top > 0 and dead == 0 and run == 1:
                    v = -4
                
                elif dead == 1 and run == 1:
                    bird_rec.y = 350
                    dead = 0
                    v = -4
                    pipe_down_rec.x = 400
                    pipe_up_rec.x = 400
                    q = random.randint(200,600)
                    pipe_up_rec = pipe_up.get_rect(midtop = (400,q))
                    pipe_down_rec = pipe_down.get_rect(midbottom = (400,q - between))
                    
                    w = random.randint(200,600)
                    pipe_up_rec2 = pipe_up.get_rect(midtop = (700,w))
                    pipe_down_rec2 = pipe_down.get_rect(midbottom = (700,w - between))
                    score = 0
            if pygame.key.get_focused() and pygame.key.get_pressed()[pygame.K_ESCAPE]:
                if run == 1:
                    run = 0
                elif run == 0:
                    run = 1
    
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
            
        if dead == 0 and run == 1:
            bird_rec.y += v
            v = v + 0.2
            pipe_up_rec.x -= 2
            pipe_down_rec.x -= 2
            pipe_up_rec2.x -= 2
            pipe_down_rec2.x -= 2
    
        if pipe_down_rec.x == bird_rec.x or pipe_down_rec2.x == bird_rec.x and run == 1:
            score = score + 1
            if score > int(high_score):
                high_score = score
                h = font2.render("high score = " + str(high_score), False, "Black")
                h_rec = h.get_rect(center = (200,90))
                
                f = open("flappy-bird/score.data", "r")
                if int(f.read()) < high_score:
                    f = open("flappy-bird/score.data", "w")
                    f.write(str(high_score))
                    f.close()
                

        if pipe_down_rec.x < -150:
            q = random.randint(220,600)
            pipe_up_rec = pipe_up.get_rect(midtop = (500,q))
            pipe_down_rec = pipe_down.get_rect(midbottom = (500,q - between))
    
        if pipe_down_rec2.x < -150:
            w = random.randint(220,600)
            pipe_up_rec2 = pipe_up.get_rect(midtop = (500,w))
            pipe_down_rec2 = pipe_down.get_rect(midbottom = (500,w - between))
    
    
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
            screen.blit(font2.render("press Esc pause", False, "Black"),(0,0))
            
            screen.blit(h,(h_rec))
    
        elif dead == 1:
            screen.blit(sky,(0,0))
            screen.blit(bird,(bird_rec))
            screen.blit(pipe_up,(pipe_up_rec))
            screen.blit(pipe_down,(pipe_down_rec))
            screen.blit(pipe_up,(pipe_up_rec2))
            screen.blit(pipe_down,(pipe_down_rec2))
            screen.blit(text,(text_rec))
            screen.blit(over_text,(over_text_rec))
            score_text = font.render(str(score), False, "black")
            screen.blit(font2.render("press Esc pause", False, "Black"),(0,0))
            score_rec = score_text.get_rect(center = (200,63))
            screen.blit(score_text,(score_rec))
            
            screen.blit(h,(h_rec))
    else:
        screen.blit(sky,(0,0))
        screen.blit(flap_text,(flap_text_rec))
        screen.blit(start_text,(start_text_rec))
        score_text = font.render(str(score), False, "black")
        score_rec = score_text.get_rect(center = (200,63))
        screen.blit(score_text,(score_rec))
        screen.blit(font2.render("made by Nathan", False, "black"),(120,350))
        screen.blit(font2.render("press Esc pause", False, "Black"),(0,0))
        if pygame.key.get_focused() and pygame.key.get_pressed()[pygame.K_SPACE]:
            start = 1
        
        screen.blit(h,(h_rec))
    
    if run == 0:
                screen.blit(pause_,(0,0))
                screen.blit(font.render("PAUSED", False, "white"),(100,100))
                screen.blit(font2.render("Press Esc to unpause", False, "white"),(100,150))
                      
    pygame.display.update()
    Clock.tick(60)