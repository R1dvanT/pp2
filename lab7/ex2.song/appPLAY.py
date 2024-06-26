
import time
import pygame as pg
pg.init()

black_friday = r'C:\Users\user\Downloads\Tom Odell - Black Friday.mp3'
unwritten = r'C:\Users\user\Downloads\Natasha_Bedingfield_-_Unwritten_63227637.mp3'
i_know = r'C:\Users\user\Downloads\Irma_-_I_Know_72287177.mp3'


screen = pg.display.set_mode((500, 400))
pg.display.set_caption("PP2 PLAYER 🎶")
clock = pg.time.Clock()

first = pg.mixer.music.load(unwritten)
second = pg.mixer.music.load(i_know)
third = pg.mixer.music.load(black_friday)
music_mix = [black_friday, unwritten, i_know]
pg.mixer.music.play(-1) #цикл 


aurora = pg.image.load(r'c:\Users\user\Downloads\зз.jfif')
screen.blit(aurora, (0, 0))
PLAY = False
running = True
song = 0
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                PLAY = not PLAY
                if PLAY:
                    pg.mixer.music.pause()
                else:
                    pg.mixer.music.unpause()
            elif event.key == pg.K_RIGHT:
                song += 1
                if song == len(music_mix):
                    song = 0
                pg.mixer.music.load(music_mix[song])
                pg.mixer.music.play()
            elif event.key == pg.K_LEFT:
                song -= 1
                if song == -1:
                    song = len(music_mix)-1
                pg.mixer.music.load(music_mix[song])
                pg.mixer.music.play()


    pg.display.flip()
    clock.tick(60)
