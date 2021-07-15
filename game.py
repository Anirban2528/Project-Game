import pygame
import time
import random
from pygame import mixer


def game():
  mixer.init()
  pygame.init()
  
  mixer.music.load(r'C:\Users\ABC\Desktop\ProjectGame\Music\music1.mp3')
  boom = mixer.Sound(r'C:\Users\ABC\Desktop\ProjectGame\Sounds\boom.mp3')
  hit_bird = mixer.Sound(r'C:\Users\ABC\Desktop\ProjectGame\Sounds\shot.mp3')
  light_blue = (0,0,255)
  display_surface = pygame.display.set_mode((600,400))

  try:
    with open(r'C:\Users\ABC\Desktop\ProjectGame\Score\score.txt','r') as r:
      data = r.read().split()
  except:
    data = ['','0']
  pygame.display.set_caption('I AM A HUNTER')

  image = pygame.image.load(r'C:\Users\ABC\Desktop\ProjectGame\Images\Sample.png')
  hunter = pygame.image.load(r'C:\Users\ABC\Desktop\ProjectGame\Images\Hunter.png')
  hunter_fire = pygame.image.load(r'C:\Users\ABC\Desktop\ProjectGame\Images\Hunterfire1.png')
  bird_up = pygame.image.load(r'C:\Users\ABC\Desktop\ProjectGame\Images\b0.png')
  bird_down = pygame.image.load(r'C:\Users\ABC\Desktop\ProjectGame\Images\b1.png')
  bird_fall1 = pygame.image.load(r'C:\Users\ABC\Desktop\ProjectGame\Images\fall1.png')
  bird_fall2 = pygame.image.load(r'C:\Users\ABC\Desktop\ProjectGame\Images\fall2.png')
  bkg = pygame.image.load(r'C:\Users\ABC\Desktop\ProjectGame\Images\background.png')
  gameover = pygame.image.load(r'C:\Users\ABC\Desktop\ProjectGame\Images\gameover.png')
  bird = [bird_up,bird_down]
  birdf = [bird_fall1,bird_fall2]
  Font=pygame.font.SysFont('monospace',  15)
  count=0
  skip=10
  x=100
  base_font = pygame.font.Font(None, 32)
  user_text = ''
  input_rect = pygame.Rect(200, 200, 140, 32)
  outline_rect = pygame.Rect(200, 200, 140, 36)
  color = pygame.Color('#00b756')
  display_surface.fill(light_blue)
  k=False
  score = 0
  life = 3
  high = int(data[1])
  active = False
  scorer = Font.render('{}'.format(data[0]), False, 'black','#add8e6')
  loops=1
  entry=0
  while True:
      if loops==1 and entry==0:
          entry=1
          mixer.music.play(-1)
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              mixer.music.stop()
              pygame.quit()
              quit()
          
          if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_BACKSPACE:
                  user_text = user_text[:-1]
              elif event.unicode!=chr(13):
                  user_text += event.unicode
              elif event.unicode==chr(13):
                  k = True
                  break
      if k==True:
        mixer.music.stop()
        mixer.music.load(r'C:\Users\ABC\Desktop\ProjectGame\Music\music2.mp3')
        loops=2
        entry=0
        pygame.display.update()
        display_surface.fill(light_blue)
        break
      
      display_surface.blit(bkg,(0,0))
      pygame.draw.rect(display_surface, 'black', outline_rect)
      pygame.draw.rect(display_surface, color, input_rect)
      text_surface = base_font.render(user_text, True, (255, 255, 0))
      display_surface.blit(text_surface, (200,200))
      input_rect.w = max(100, text_surface.get_width()+10)
      outline_rect.w = max(100, text_surface.get_width()+10)
      pygame.display.flip()
   
  while True:
    if loops==2 and entry==0:
        entry=1
        mixer.music.play(-1)
    h_score=Font.render("{}".format(high), False, 'black','#add8e6')
    y_score = Font.render('{}'.format(score), False, 'black','#add8e6')
    lyf = Font.render('{}'.format(life), False, 'black','#9fd836')
    if x==0:
      x=random.randint(30,100)
    display_surface.blit(image,(0,0))
    display_surface.blit(hunter,(0,300))
    display_surface.blit(y_score,(65,7))
    display_surface.blit(h_score,(535,4.5))
    display_surface.blit(scorer,(475,29))
    display_surface.blit(lyf,(515,382))
    if count%2==0:
      display_surface.blit(bird[0],(skip,x-2))
      mov=0
    else:
      display_surface.blit(bird[1],(skip,x))
      mov=1
    time.sleep(.07)
    
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        if score>int(data[1]):
          with open(r'C:\Users\ABC\Desktop\ProjectGame\Score\score.txt','w') as w:
            w.write(user_text.replace('  ',' ') + ' ' + str(score))
        pygame.quit()
        quit()
      elif event.type==pygame.MOUSEBUTTONUP:
        mouse_x,mouse_y = event.pos
        display_surface.blit(hunter_fire,(75,300))
        mixer.Sound.play(boom)
        pygame.display.update()
        if mouse_x-16<skip<mouse_x+15 and mouse_y-16<x<mouse_y+15:
          position=skip
          fall=x
          score+=5
          mixer.Sound.play(hit_bird)
          mixer.music.pause()
          while fall<=150:
            display_surface.blit(image,(0,0))
            display_surface.blit(hunter,(0,300))
            display_surface.blit(y_score,(65,7))
            display_surface.blit(h_score,(535,4.5))
            display_surface.blit(scorer,(475,29))
            display_surface.blit(lyf,(515,382))
            for event in pygame.event.get():
              if event.type==pygame.MOUSEBUTTONUP:
                life-=1
            if life==0:
              active = True
              mixer.music.stop()
              mixer.music.load(r'C:\Users\ABC\Desktop\ProjectGame\Music\music3.mp3')
              entry=0
              loops=3
              if score>int(data[1]):
                with open(r'C:\Users\ABC\Desktop\ProjectGame\Score\score.txt','w') as w:
                  w.write(user_text.replace('  ',' ') + ' ' + str(score))
              pygame.display.update()
              Font=pygame.font.SysFont('monospace',  35)
              y_score = Font.render('{}'.format(score), False, 'black','#4CBA39')
              while active:
                  if loops==3 and entry==0:
                    pygame.music.play()
                    entry=1
                  display_surface.blit(gameover,(0,0))
                  display_surface.blit(y_score,(365,220))
                  for event in pygame.event.get():
                     if event.type == pygame.QUIT:
                        mixer.music.stop()
                        pygame.quit()
                        quit()
                     if event.type == pygame.KEYDOWN:
                        score=0
                        skip=10
                        x=0
                        count=0
                        active=False
                        k=False
                        life=3
                        pygame.display.update()
                        mixer.music.stop()
                        game()
                  pygame.display.update()
            if fall%2==0:
              display_surface.blit(birdf[0],(position,fall))
            else:
              display_surface.blit(birdf[1],(position,fall))
            time.sleep(.05)
            pygame.display.update()
            if fall+5>150:
              mixer.music.unpause()
            fall+=5
          skip=10
          count=-1
          x=0
        else:
          life-=1
          if life==0:
            active = True
            mixer.music.stop()
            mixer.music.load(r'C:\Users\ABC\Desktop\ProjectGame\Music\music3.mp3')
            entry=0
            loops=3
            if score>int(data[1]):
              with open(r'C:\Users\ABC\Desktop\ProjectGame\Score\score.txt','w') as w:
                w.write(user_text.replace('  ',' ') + ' ' + str(score))
            pygame.display.update()
            Font=pygame.font.SysFont('monospace',  35)
            y_score = Font.render('{}'.format(score), False, 'black','#4CBA39')
            while active:
                if loops==3 and entry==0:
                    mixer.music.play()
                    entry=1
                display_surface.blit(gameover,(0,0))
                display_surface.blit(y_score,(365,220))
                for event in pygame.event.get():
                   if event.type == pygame.QUIT:
                      mixer.music.stop()
                      pygame.quit()
                      quit()
                   if event.type == pygame.KEYDOWN:
                      score=0
                      skip=10
                      x=0
                      count=0
                      active=False
                      k=False
                      life=3
                      pygame.display.update()
                      mixer.music.stop()
                      game()
                pygame.display.update()
          
      else: continue
    count+=1
    skip+=5
    if skip>=595:
      skip=45
      count=-1
      x=0
      
    
    pygame.display.update()
game()