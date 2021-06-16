import random

import pygame

pygame.init()
size = screen_width, screen_height = 1366, 768
win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, pygame.RESIZABLE)

pygame.display.set_caption("GAME")
fps = 8
velocity = 20

# background sprites
bg = pygame.image.load("backgrounds/bg.png")
bg_clouds = [pygame.image.load("backgrounds/1.png"), pygame.image.load("backgrounds/2.png")]
bullet = pygame.transform.scale(pygame.image.load("objects/bullet.png"), (50, 50))

enemy_no = 0

# character size
height = 100
width = 100
shot_x = 0
shot_y = 0
bush_x = 0

# initial Character position
char_x = 150
char_y = 500
enemy_x = screen_width / 2
enemy_y = 530

# character animation sprites
# male
anim_idle_m = [pygame.transform.scale(pygame.image.load("characters/male/I1.png"), (width, height)),
               pygame.transform.scale(pygame.image.load("characters/male/I2.png"), (width, height)),
               pygame.transform.scale(pygame.image.load("characters/male/I3.png"), (width, height)),
               pygame.transform.scale(pygame.image.load("characters/male/I4.png"), (width, height)),
               pygame.transform.scale(pygame.image.load("characters/male/I5.png"), (width, height)),
               pygame.transform.scale(pygame.image.load("characters/male/I6.png"), (width, height)),
               pygame.transform.scale(pygame.image.load("characters/male/I7.png"), (width, height)),
               pygame.transform.scale(pygame.image.load("characters/male/I8.png"), (width, height)),
               ]
anim_walk_m = [pygame.transform.scale(pygame.image.load("characters/male/W1.png"), (width, height)),
               pygame.transform.scale(pygame.image.load("characters/male/W2.png"), (width, height)),
               pygame.transform.scale(pygame.image.load("characters/male/W3.png"), (width, height)),
               pygame.transform.scale(pygame.image.load("characters/male/W4.png"), (width, height)),
               pygame.transform.scale(pygame.image.load("characters/male/W5.png"), (width, height)),
               pygame.transform.scale(pygame.image.load("characters/male/W6.png"), (width, height)),
               pygame.transform.scale(pygame.image.load("characters/male/W7.png"), (width, height)),
               pygame.transform.scale(pygame.image.load("characters/male/W8.png"), (width, height)),
               ]
anim_dead_m = [pygame.transform.scale(pygame.image.load("characters/male/D1.png"), (width, height)),
               pygame.transform.scale(pygame.image.load("characters/male/D2.png"), (width, height)),
               pygame.transform.scale(pygame.image.load("characters/male/D3.png"), (width, height)),
               pygame.transform.scale(pygame.image.load("characters/male/D4.png"), (width, height)),
               pygame.transform.scale(pygame.image.load("characters/male/D5.png"), (width, height)),
               pygame.transform.scale(pygame.image.load("characters/male/D6.png"), (width, height)),
               pygame.transform.scale(pygame.image.load("characters/male/D7.png"), (width, height)),
               pygame.transform.scale(pygame.image.load("characters/male/D8.png"), (width, height)),
               ]
anim_attack_m = [pygame.transform.scale(pygame.image.load("characters/male/A1.png"), (width, height)),
                 pygame.transform.scale(pygame.image.load("characters/male/A2.png"), (width, height)),
                 pygame.transform.scale(pygame.image.load("characters/male/A3.png"), (width, height)),
                 pygame.transform.scale(pygame.image.load("characters/male/A4.png"), (width, height)),
                 pygame.transform.scale(pygame.image.load("characters/male/A5.png"), (width, height)),
                 pygame.transform.scale(pygame.image.load("characters/male/A6.png"), (width, height)),
                 pygame.transform.scale(pygame.image.load("characters/male/A7.png"), (width, height)),
                 pygame.transform.scale(pygame.image.load("characters/male/A8.png"), (width, height)),
                 ]
# female
anim_idle_f = [pygame.transform.scale(pygame.image.load("characters/female/I1.png"), (width, height)),
               pygame.transform.scale(pygame.image.load("characters/female/I2.png"), (width, height)),
               pygame.transform.scale(pygame.image.load("characters/female/I3.png"), (width, height)),
               pygame.transform.scale(pygame.image.load("characters/female/I4.png"), (width, height)),
               pygame.transform.scale(pygame.image.load("characters/female/I5.png"), (width, height)),
               pygame.transform.scale(pygame.image.load("characters/female/I6.png"), (width, height)),
               pygame.transform.scale(pygame.image.load("characters/female/I7.png"), (width, height)),
               pygame.transform.scale(pygame.image.load("characters/female/I8.png"), (width, height)),
               ]
anim_walk_f = [pygame.transform.scale(pygame.image.load("characters/female/W1.png"), (width, height)),
               pygame.transform.scale(pygame.image.load("characters/female/W2.png"), (width, height)),
               pygame.transform.scale(pygame.image.load("characters/female/W3.png"), (width, height)),
               pygame.transform.scale(pygame.image.load("characters/female/W4.png"), (width, height)),
               pygame.transform.scale(pygame.image.load("characters/female/W5.png"), (width, height)),
               pygame.transform.scale(pygame.image.load("characters/female/W6.png"), (width, height)),
               pygame.transform.scale(pygame.image.load("characters/female/W7.png"), (width, height)),
               pygame.transform.scale(pygame.image.load("characters/female/W8.png"), (width, height)),
               ]
anim_dead_f = [pygame.transform.scale(pygame.image.load("characters/female/D1.png"), (width, height)),
               pygame.transform.scale(pygame.image.load("characters/female/D2.png"), (width, height)),
               pygame.transform.scale(pygame.image.load("characters/female/D3.png"), (width, height)),
               pygame.transform.scale(pygame.image.load("characters/female/D4.png"), (width, height)),
               pygame.transform.scale(pygame.image.load("characters/female/D5.png"), (width, height)),
               pygame.transform.scale(pygame.image.load("characters/female/D6.png"), (width, height)),
               pygame.transform.scale(pygame.image.load("characters/female/D7.png"), (width, height)),
               pygame.transform.scale(pygame.image.load("characters/female/D8.png"), (width, height)),
               ]
anim_attack_f = [pygame.transform.scale(pygame.image.load("characters/female/A1.png"), (width, height)),
                 pygame.transform.scale(pygame.image.load("characters/female/A2.png"), (width, height)),
                 pygame.transform.scale(pygame.image.load("characters/female/A3.png"), (width, height)),
                 pygame.transform.scale(pygame.image.load("characters/female/A4.png"), (width, height)),
                 pygame.transform.scale(pygame.image.load("characters/female/A5.png"), (width, height)),
                 pygame.transform.scale(pygame.image.load("characters/female/A6.png"), (width, height)),
                 pygame.transform.scale(pygame.image.load("characters/female/A7.png"), (width, height)),
                 pygame.transform.scale(pygame.image.load("characters/female/A8.png"), (width, height)),
                 ]
# temp
anim_walk = anim_walk_m
anim_idle = anim_idle_m
anim_dead = anim_dead_m
anim_attack = anim_attack_m

# enemy
enemy = [[pygame.image.load("characters/enemy/1/idle/frame-1.png"),
          pygame.image.load("characters/enemy/1/Idle/frame-2.png"),
          pygame.image.load("characters/enemy/1/Idle/frame-1.png"),
          pygame.image.load("characters/enemy/1/Idle/frame-2.png"),
          pygame.image.load("characters/enemy/1/Idle/frame-1.png"),
          pygame.image.load("characters/enemy/1/Idle/frame-2.png"),
          pygame.image.load("characters/enemy/1/Idle/frame-1.png"),
          pygame.image.load("characters/enemy/1/Idle/frame-2.png")],
         [pygame.image.load("characters/enemy/2/Idle/frame-1.png"),
          pygame.image.load("characters/enemy/2/Idle/frame-2.png"),
          pygame.image.load("characters/enemy/2/Idle/frame-1.png"),
          pygame.image.load("characters/enemy/2/Idle/frame-2.png"),
          pygame.image.load("characters/enemy/2/Idle/frame-1.png"),
          pygame.image.load("characters/enemy/2/Idle/frame-2.png"),
          pygame.image.load("characters/enemy/2/Idle/frame-1.png"),
          pygame.image.load("characters/enemy/2/Idle/frame-2.png")]]

# bushes/extras
bush = [pygame.image.load("objects/non_collidable/1.png"),
        pygame.image.load("objects/non_collidable/2.png"),
        pygame.image.load("objects/non_collidable/3.png"),
        pygame.image.load("objects/non_collidable/4.png"),
        pygame.image.load("objects/non_collidable/5.png"),
        pygame.image.load("objects/non_collidable/6.png"),
        pygame.image.load("objects/non_collidable/7.png"),
        pygame.image.load("objects/non_collidable/8.png"),
        pygame.image.load("objects/non_collidable/9.png"),
        pygame.image.load("objects/non_collidable/10.png"),
        pygame.image.load("objects/non_collidable/11.png"),
        ]

# boolean Variables Runtimes
isRunning = True
isJump = False
walk_left = False
walk_right = False
isAttacking = False
isEnemyAlive = True

# extras
jumpCount = 10
attackCount = 5
screen = 0
char_no = 0
walkCount = 0
clock = pygame.time.Clock()
cloud_transform_x = 2 * screen_width
bullet_x = height

score = 0
font = pygame.font.Font('freesansbold.ttf', 32)


def flip_screen():
    global screen
    global win
    if screen == 0:
        win = pygame.display.set_mode(size)
        screen = 1
    else:
        win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, pygame.RESIZABLE)
        screen = 0
    pygame.display.init()


def switchPlayer():
    global char_no, anim_attack, anim_dead, anim_idle, anim_walk
    if char_no == 0:
        anim_idle = anim_idle_m
        anim_dead = anim_dead_m
        anim_walk = anim_walk_m
        anim_attack = anim_attack_m
        char_no = 1
    elif char_no == 1:
        anim_idle = anim_idle_f
        anim_dead = anim_dead_f
        anim_walk = anim_walk_f
        anim_attack = anim_attack_f
        char_no = 0


# rendering Loop
def addEnemy():
    global enemy_x
    win.blit(enemy[enemy_no][walkCount // (fps // 8)], (enemy_x, enemy_y))
    enemy_x -= velocity


def set_window_rendering():
    global clock, walkCount, win, cloud_transform_x, attackCount, bullet_x, isAttacking
    global shot_x, shot_y, isEnemyAlive, enemy_x, enemy_no, score

    cloud_transform_x -= velocity / 2
    if cloud_transform_x <= -screen_width:
        cloud_transform_x = screen_width

    # animate BG
    win.blit(pygame.transform.scale(bg, (screen_width, screen_height)), (0, 0))
    win.blit(bg_clouds[0], (cloud_transform_x - screen_width, 0))
    win.blit(bg_clouds[1], (2 * cloud_transform_x, 0))

    score_text = font.render('Score : ' + str(score), True, (255, 255, 255))
    win.blit(score_text, (screen_width / 2, 40))

    if walkCount >= fps:
        walkCount = 0

    addEnemy()

    if (shot_x in range(int(enemy_x) - 10, int(enemy_x) + 11) and shot_y in range(enemy_y - 10,
                                                                                  enemy_y + 11)) or enemy_x < -screen_width:

        score += 100
        print(score)
        enemy_no = random.randrange(0, 2)
        enemy_x = screen_width

    if enemy_x in range(char_x - 10, char_x + 11):
        print("you lose")

    if isAttacking:
        if attackCount == 0:
            attackCount = 5
            isAttacking = False
        attackCount -= 1
        bullet_x += 3 * velocity
        shot_x = char_x + bullet_x - 50
        win.blit(bullet, (shot_x, shot_y, width, height))
        win.blit(anim_attack[walkCount // (fps // 8)], (char_x, char_y, width, height))
        walkCount += 1
    else:
        shot_x = -1000
        if walk_right:
            win.blit(anim_walk[walkCount // (fps // 8)], (char_x, char_y, width, height))
            walkCount += 1
        elif walk_left:
            win.blit(pygame.transform.flip(anim_walk[walkCount // (fps // 8)], True, False),
                     (char_x, char_y, width, height))
            walkCount += 1
        else:
            win.blit(anim_idle[walkCount // (fps // 8)], (char_x, char_y, width, height))
            walkCount += 1

    pygame.display.update()


# mainLoop
while isRunning:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        flip_screen()
    if keys[pygame.K_TAB]:
        switchPlayer()

    if keys[pygame.K_LEFT] and char_x > velocity:
        char_x -= 2 * velocity
        walk_left = True
        walk_right = False
    elif keys[pygame.K_RIGHT] and char_x < 1366 - width - velocity:
        char_x += 2 * velocity
        walk_left = False
        walk_right = True
    else:
        walk_left = False
        walk_right = False

    if keys[pygame.K_SPACE] and attackCount <= 5:
        bullet_x = width
        isAttacking = True
        shot_y = char_y + 30

    if not isJump:
        if keys[pygame.K_UP]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            char_y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    set_window_rendering()

# quiting the game
pygame.quit()
