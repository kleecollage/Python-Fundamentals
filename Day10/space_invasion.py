import io

from pygame import mixer
import math
import random
import pygame

# FONT TRANSFORM
def font_bytes(my_font):
    with open(my_font, "rb") as f:
        ttf_bytes = f.read()
    return io.BytesIO(ttf_bytes)

# INIT PYGAME
pygame.init()

# CREATE WINDOW
screen = pygame.display.set_mode((800, 600))
game_font = font_bytes("Game_Of_Squids.ttf")

# TITLE AND ICON
pygame.display.set_caption("Space Invasion")
icon = pygame.image.load("ufo_icon.png")
pygame.display.set_icon(icon)
background = pygame.image.load("universe_bg.jpg")

# MUSIC
mixer.music.load("game_music.mp3")
mixer.music.set_volume(0.3)
mixer.music.play(-1)

# MISSILE VARIABLES
missiles = []
img_missile = pygame.image.load("missile_2.png")
missile_x = 0
missile_y = 500
missile_y_change = 2
missile_visible = False

# PLAYER VARIABLES
img_player = pygame.image.load("spaceship.png")
player_x = 368
player_y = 500
player_x_change = 0

# ENEMY VARIABLES
img_enemy = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
enemy_number = 8
for enemy in range(enemy_number):
    img_enemy.append(pygame.image.load("ufo_1.png"))
    enemy_x.append(random.randint(0, 736))
    enemy_y.append(random.randint(50, 200))
    enemy_x_change.append(2)
    enemy_y_change.append(50)

# SCORE
score = 0

font = pygame.font.Font(game_font, 32)
score_x = 10
score_y = 10

# END GAME
final_font = pygame.font.Font(game_font, 40)
def final_text():
    my_final_font = final_font.render("GAME OVER", True, (0, 189, 35))
    screen.blit(my_final_font, (60, 200))

# SHOW SCORE
def show_score(x, y):
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (x, y))

# PLAYER FUNCTION
def player(x, y):
    screen.blit(img_player, (x, y))

# ENEMY FUNCTION
def enemy(x, y, ene):
    screen.blit(img_enemy[ene], (x, y))

# SHOOT MISSILE FUNCTION
def shoot_missile(x, y):
    global missile_visible
    missile_visible = True
    screen.blit(img_missile, (x + 16, y + 10))

# COLLISIONS FUNCTION
def is_collision(x_1, x_2, y_1, y_2):
    distance = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_1 - y_2, 2))
    if distance < 27:
        return True
    else:
        return False


# GAME LOOP
on_execution = True
while on_execution:
    # RGB
    # screen.fill((205, 144, 228))
    # BACKGROUND
    screen.blit(background, (0, 0))
    # EVENT ITERATION
    for event in pygame.event.get():
        # EVENT CLOSE
        if event.type == pygame.QUIT:
            on_execution = False
        # EVENT PRESS KEYS
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -2
            if event.key == pygame.K_RIGHT:
                player_x_change = 2
            if event.key == pygame.K_SPACE:
                missile_sound = mixer.Sound('shoot_2.mp3')
                missile_sound.set_volume(0.3)
                missile_sound.play()
                new_missile = {
                    "x": player_x,
                    "y": player_y,
                    "speed": -5
                }
                missiles.append(new_missile)
                if not missile_visible:
                    missile_x = player_x
                    shoot_missile(missile_x, missile_y)
        # EVENT KEYS RELEASE
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0
    # NEW PLAYER LOCATION
    player_x += player_x_change
    # KEEP PLAYER IN MARGINS
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736
    # NEW ENEMY LOCATION
    for e in range(enemy_number):
        # END GAME
        if enemy_y[e] > 500:
            for k in range(enemy_number):
                enemy_y[k] = 1000
            final_text()
            break

        enemy_x[e] += enemy_x_change[e]
        # KEEP ENEMIES IN MARGINS
        if enemy_x[e] <= 0:
            enemy_x_change[e] = 1
            enemy_y[e] += enemy_y_change[e]
        elif enemy_x[e] >= 736:
            enemy_x_change[e] = -1
            enemy_y[e] += enemy_y_change[e]
        # COLLISIONS
        for missil in missiles:
            collision = is_collision(enemy_x[e], missil["x"], enemy_y[e], missil["y"])
            if collision:
                collision_sound = mixer.Sound('collision_1.mp3')
                collision_sound.set_volume(0.8)
                collision_sound.play()
                missiles.remove(missil)
                # missile_y = 475
                # missile_visible = False
                score += 1
                enemy_x[e] = random.randint(0, 736)
                enemy_y[e] = random.randint(50, 200)
                break
        enemy(enemy_x[e], enemy_y[e], e)
    # MISSILE MOVEMENT
    for missil in missiles:
        missil["y"] += missil["speed"]
        screen.blit(img_missile, (missil["x"] + 16, missil["y"] + 10))
        if missil["y"] < 0:
            missiles.remove(missil)
    # if missile_y <= -64:
    #     missile_y = 500
    #     missile_visible = False
    # if missile_visible:
    #     shoot_missile(missile_x, missile_y)
    #     missile_y -= missile_y_change

    player(player_x, player_y)
    show_score(score_x, score_y)
    # UPDATE
    pygame.display.update()


