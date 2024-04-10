import pygame as py
py.init()

WHITE = (255,255,255)
RED = (255,0,0)

W, H = 610, 410
screen = py.display.set_mode((W, H))
py.display.set_caption("Red Ball")

clock = py.time.Clock()
FPS = 60

radius = 25
speed = 20
circle_rect = py.Rect(0,0,50,50)

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            exit()
    
    pressed = py.key.get_pressed()
    
    if pressed[py.K_w] and circle_rect.top > 0:
        circle_rect.top -= speed
    if pressed[py.K_s] and circle_rect.bottom < H:
        circle_rect.bottom += speed
    if pressed[py.K_a] and circle_rect.left > 0:
        circle_rect.left -= speed
    if pressed[py.K_d] and circle_rect.right < W:
        circle_rect.right += speed
    

    screen.fill(WHITE)
    py.draw.circle(screen, RED, circle_rect.center, radius)
    py.display.update()
    clock.tick(FPS)
    