import time
import pygame, sys, random
pygame.mixer.pre_init(44100, -16, 2,512)
pygame.init()
screen_width,screen_height = 780,500


pygame.display.set_caption('The Smal BOB')
screen = pygame.display.set_mode((screen_width,screen_height))
box = pygame.Rect(20,10000,22,40)
enemy_x = random.randrange(screen_width)
enemy_y = random.randrange(screen_height)
text = pygame.font.SysFont('Comic Sans MS',30).render('click space to play',False,(0,0,0))
clock = pygame.time.Clock()
menu = True
by_dawid = pygame.font.SysFont('Comic Sans MS', 20).render('game by dizel g', False, (0, 0, 0))
the_smal_bob = pygame.font.SysFont('Comic Sans MS', 50).render('The Small BOB', False, (0, 0, 0))
coin_image = pygame.image.load('coin.png')
gras_image = pygame.image.load('player0.png')
gras_image.set_colorkey((255,255,255))
pygame.display.set_icon(gras_image)


but_image = pygame.image.load('but.png')
but_image = pygame.transform.scale(but_image,(70,50))
but_image.get_rect()
upgrade_image = pygame.image.load('upgrade.png')
upgrade_image.set_colorkey((255,255,255))
upgrade_image = pygame.transform.scale(upgrade_image,(80,60))
background_image = pygame.image.load('background.png')
background_image = pygame.transform.scale(background_image,(screen_width,screen_height))
but_image.set_colorkey((255,255,255))
coin_image.set_colorkey((255,255,255))
score_plus = 1
coin_plus = 1
upgrade = False
die_sound = pygame.mixer.Sound('die.wav')
levelup_sound = pygame.mixer.Sound('levelup.wav')
coin_sound = pygame.mixer.Sound('coin.wav')
music = pygame.mixer.music.load('music.wav')
music = pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)
def game ():
    score_plus = 1
    score = 0
    punkty = 0
    cost = 2
    lvl = 1
    enemy_x = random.randrange(screen_width)
    enemy_y = -60
    coin_x = random.randrange(screen_width)
    coin_y = -60
    game_run = True
    player_speed = 4
    while game_run:

        gras_image = pygame.image.load('player0.png')
        gras_image.set_colorkey((255,255,255))
        gras_image = pygame.transform.scale(gras_image, (50, 50))
        punkty_text = pygame.font.SysFont('Comic Sans MS', 30).render(f'coins: {punkty}', False, (0, 0, 0))
        lvl_text = pygame.font.SysFont('Comic Sans MS', 25).render(f'lvl: {lvl}', False, (0, 0, 0))
        score_text = pygame.font.SysFont('Comic Sans MS', 30).render(f'score: {score}', False, (0, 0, 0))
        coin = pygame.Rect(coin_x - 30, coin_y - 30, 70, 50)
        enemy = pygame.Rect(enemy_x - 30, enemy_y - 30, 70, 50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(666)
        if player_speed > 6:
            player_speed = 6
        if cost <= punkty:
            upgrade = True
        if cost > punkty:
            upgrade = False
        if enemy_y >= screen_height:
            score += score_plus
            enemy_y = -60
            enemy_x = random.randrange(screen_width)
        if coin_y >= screen_height:
            coin_y = -60
            coin_x = random.randrange(screen_width)
        if box.y >= screen_height:
            box.y -= 51
        if box.x >= screen_width-24:
            box.x -= player_speed
        if box.x <= 0:
            box.x += player_speed
        enemy_y += 6
        coin_y += 5

        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_d]:

            box.x += player_speed
        if key_input[pygame.K_a]:

            box.x -= player_speed

        if box.colliderect(enemy):
            die_sound.set_volume(0.3)
            die_sound.play()
            game_run = False
            enemy_x = random.randrange(screen_width)
            enemy_y = 0
        if box.colliderect(coin):
            coin_sound.set_volume(0.2)
            coin_sound.play()
            punkty += coin_plus
            coin_x = random.randrange(screen_width)
            coin_y = -60


        # drawing

        screen.fill((100, 100, 255))
        #back ground
        screen.blit(background_image,(0,0))
        screen.blit(punkty_text,(0,0))
        screen.blit(score_text,(0,25))
        rect = pygame.draw.rect
        screen.blit(lvl_text,(0,100))
        screen.blit(coin_image,(coin))
        screen.blit(but_image,(enemy))
        screen.blit(gras_image, (box.x-13, box.y-3))
        screen.blit(upgrade_image,(0,50))
        if upgrade == True:
            upgrade_avaliable = pygame.font.SysFont('Comic Sans MS', 38).render(f'PRESS SPACE TO UPGRADE', False, (0, 0, 0))
            screen.blit(upgrade_avaliable,(170,0))
            pygame.display.flip()
            if pygame.key.get_pressed() [pygame.K_SPACE]:
                upgrade_avaliable = False
                levelup_sound.set_volume(0.5)
                levelup_sound.play()
                player_speed +=1
                punkty -= cost
                cost += 2
                lvl +=1
                score_plus += 1
        pygame.display.update()
        clock.tick(160)
#menu
while menu:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:

            box.x = 3
            box.y = 554
            game()
    screen.fill((0, 162, 235))
    screen.blit(the_smal_bob,(230,50))
    gras_image = pygame.transform.scale(gras_image,(100,100))
    screen.blit(gras_image,(350,150))
    screen.blit(by_dawid,(0,screen_height-30))
    pygame.display.update()
    clock.tick(120)

