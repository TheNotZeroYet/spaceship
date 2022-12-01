import pygame as pg
import sys
from random import randint, choice

from spaceship import Spaceship
from screen import Screen
from meteor import Meteor
from bonusMeteor import BonusMeteor
from rocket import Rocket
from enemy import Enemy
from button import Button

pg.init()

screen = pg.display.set_mode((Screen.WIDTH, Screen.HEIGHT))


# FUNCTION
def create_meteor():
    global meteor_i
    global random_meteor
    meteor_i += 1
    if meteor_i == random_meteor and screen_obj.is_game:
        meteor_i = 0
        random_meteor = randint(50, 120)
        meteor_obj_list.append(choice([Meteor(meteor_img_list), BonusMeteor(bonus_img_list)]))


# SPAWN ENEMY
def create_enemy():
    global enemy_i
    global random_enemy
    enemy_i += 1
    if enemy_i == random_enemy:
        enemy_i = 0
        enemy_spawn_music.play()
        random_enemy = randint(360, 540)
        enemy_obj_list.append(Enemy(enemy_img))


def push_rocket(event):
    if event.type == pg.KEYDOWN and screen_obj.is_game:
        if event.key == pg.K_SPACE:
            for space_ship_obj in space_ship_obj_list:
                shot_spaceship_sound.play()
                rocket_obj_list.append(Rocket(rocket_img, rocket_enemy_img, "up", space_ship_obj.x, space_ship_obj.y))


def enemy_push_rocket():
    global rocket_enemy_random
    global rocket_enemy_i
    rocket_enemy_i += 1
    if rocket_enemy_i == rocket_enemy_random:
        rocket_enemy_i = 1
        rocket_enemy_random = 120
        for enemy_obj in enemy_obj_list:
            # TODO: Звук выстрела врага
            rocket_enemy_list.append(Rocket(rocket_img, rocket_enemy_img, "down", enemy_obj.x, enemy_obj.y))


def spawn_count_meteor(count):
    for _ in range(count):
        meteor_obj_list.append(Meteor(meteor_img_list))


def move_spaceship():
    if screen_obj.is_game:
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            for space_ship_obj in space_ship_obj_list:
                space_ship_obj.move_left()
        if keys[pg.K_d]:
            for space_ship_obj in space_ship_obj_list:
                space_ship_obj.move_right()


def collision_red():
    # COLLISION RED
    for m in meteor_obj_list:
        for space_ship_obj in space_ship_obj_list:
            if space_ship_obj.collision(m) and m.is_bonus:
                if m in meteor_obj_list and m.bonus == "red":
                    meteor_obj_list.remove(m)
                    spawn_count_meteor(randint(15, 35))


def collision_green():
    # COLLISION GREEN
    for m in meteor_obj_list:
        for space_ship_obj in space_ship_obj_list:
            if space_ship_obj.collision(m) and m.is_bonus:
                if m in meteor_obj_list and m.bonus == "green" and space_ship_obj.life > 0:
                    meteor_obj_list.remove(m)
                    space_ship_obj.life_edit(-1)
                if m in meteor_obj_list and m.bonus == "green":
                    meteor_obj_list.remove(m)


def collision_purple():
    # COLLISION PURPLE
    for m in meteor_obj_list:
        for space_ship_obj in space_ship_obj_list:
            if space_ship_obj.collision(m) and m.is_bonus:
                if m in meteor_obj_list and m.bonus == "purple":
                    rand_bonus = choice(["pos", "neg", "pos", "neg"])
                    meteor_obj_list.remove(m)
                    if rand_bonus == "pos":
                        space_ship_obj_list.append(
                            Spaceship(space_ship_img_list, spaceship_x + choice([n * 30 for n in range(-20, 20)])))
                    else:
                        enemy_obj_list.append(Enemy(enemy_img))


def collision_rocket_meteor():
    for r in rocket_obj_list:
        for m in meteor_obj_list:
            if r.collision(m):
                if m in meteor_obj_list:
                    destroy_meteor_sound.play()
                    meteor_obj_list.remove(m)
                if r in rocket_obj_list:
                    rocket_obj_list.remove(r)


def collision_spaceship_meteor():
    for m in meteor_obj_list:
        for space_ship_obj in space_ship_obj_list:
            if space_ship_obj.collision(m) and not m.is_bonus:
                if m in meteor_obj_list:
                    meteor_obj_list.remove(m)
                    if space_ship_obj.life == 2:
                        space_ship_obj_list.remove(space_ship_obj)
                        spaceship_damage_sound3.play()
                    else:
                        if space_ship_obj.life == 1:
                            space_ship_obj.life_edit(1)
                            spaceship_damage_sound1.play()
                        else:
                            spaceship_damage_sound2.play()
                            space_ship_obj.life_edit(1)


def collision_enemy_rocket_spaceship():
    for rocket_obj in rocket_enemy_list:
        for space_ship_obj in space_ship_obj_list:
            if space_ship_obj.collision(rocket_obj):
                rocket_enemy_list.remove(rocket_obj)
                if space_ship_obj.life == 2:
                    spaceship_damage_sound3.play()
                    space_ship_obj_list.remove(space_ship_obj)
                else:
                    if space_ship_obj.life == 1:
                        space_ship_obj.life_edit(1)
                        spaceship_damage_sound1.play()
                    else:
                        spaceship_damage_sound2.play()
                        space_ship_obj.life_edit(1)


def collision_spaceship_rocket_enemy():
    for enemy_obj in enemy_obj_list:
        for rocket_obj in rocket_obj_list:
            if enemy_obj.collision_spaceship_rocket(rocket_obj):
                enemy_obj_list.remove(enemy_obj)
                rocket_obj_list.remove(rocket_obj)


def rocket_update():
    for r in rocket_obj_list:
        if r.is_active:
            r.update(screen)
        else:
            rocket_obj_list.remove(r)


def meteor_update():
    for m in meteor_obj_list:
        if m.is_active:
            m.update(screen)


def spaceship_update():
    for space_ship_obj in space_ship_obj_list:
        space_ship_obj.update(screen)


def enemy_update():
    for space_ship_obj in space_ship_obj_list:
        for enemy_obj in enemy_obj_list:
            enemy_obj.update(screen, space_ship_obj.x)


def screen_update():
    screen_obj.update(screen)


def enemy_rocket_update():
    for enemy_rocket_obj in rocket_enemy_list:
        enemy_rocket_obj.update(screen)


def objects_update():
    screen_update()
    enemy_rocket_update()
    meteor_update()
    rocket_update()
    enemy_update()
    spaceship_update()


def objects_collision():
    collision_red()
    collision_green()
    collision_purple()
    collision_rocket_meteor()
    collision_spaceship_meteor()
    collision_spaceship_rocket_enemy()
    collision_enemy_rocket_spaceship()


def click_play(event):
    if event.type == pg.MOUSEBUTTONDOWN and button_obj.x <= pg.mouse.get_pos()[0] <= button_obj.x + Button.WIDTH \
            and button_obj.y <= pg.mouse.get_pos()[1] <= button_obj.y + Button.HEIGHT:
        screen_obj.set_game(True)


def check_game():
    if len(space_ship_obj_list) == 0:
        screen_obj.set_game(False)
        screen_obj.set_img(fail_img)


# IMAGE
space_ship_img_list = [pg.image.load(f"sprites/spaceship{i}.png") for i in range(1, 4)]
back_img = pg.image.load("sprites/back.jpg")
meteor_img_list = [pg.image.load(f"sprites/meteor{i}.png") for i in range(1, 4)]
bonus_img_list = [pg.image.load(f"sprites/bonus{i}.png") for i in range(1, 4)]
rocket_img = pg.image.load("sprites/rocket.png")
rocket_enemy_img = pg.image.load("sprites/rocket_enemy.png")
enemy_img = pg.image.load("sprites/enemy.png")
fail_img = pg.image.load("sprites/fail_cat.png")
button_img = pg.image.load("sprites/play_btn.png")

# AUDIO
shot_spaceship_sound = pg.mixer.Sound("audio/sounds/shot_spaceship.mp3")
destroy_meteor_sound = pg.mixer.Sound("audio/sounds/destroy_meteor.mp3")
enemy_spawn_music = pg.mixer.Sound("audio/music/enemy_spawn.wav")
spaceship_damage_sound3 = pg.mixer.Sound("audio/sounds/spaceship_damage3.wav")
spaceship_damage_sound2 = pg.mixer.Sound("audio/sounds/spaceship_damage2.wav")
spaceship_damage_sound1 = pg.mixer.Sound("audio/sounds/spaceship_damage1.wav")
back_music = pg.mixer.Sound("audio/music/back_music.wav")

# CREATE OBJECTS AND VARIABLES
screen_obj = Screen(back_img)
button_obj = Button(600, 300, button_img)
random_meteor = randint(20, 60)
meteor_i = 0
meteor_obj_list = []

rocket_obj_list = []

spaceship_x = (Screen.WIDTH - Spaceship.SIZE) // 2
space_ship_obj_list = [Spaceship(space_ship_img_list, spaceship_x)]

random_enemy = randint(360, 540)
rocket_enemy_list = []
rocket_enemy_i = 0
rocket_enemy_random = 120
enemy_i = 0
enemy_obj_list = []

clock = pg.time.Clock()

back_music.play()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        click_play(event)
        push_rocket(event)

    objects_update()
    check_game()

    if screen_obj.is_game:
        objects_collision()
        create_meteor()
        move_spaceship()
        enemy_push_rocket()
    else:
        button_obj.update(screen)

    clock.tick(Screen.FPS)
    pg.display.flip()
