import pygame

pygame.init()
screen_width,screen_height=500,500


display_surface=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Adding image and background image")

background_image=pygame.transform.scale(pygame.image.load("background.png").convert(),(screen_width,screen_height))

cricketer= pygame.transform.scale(pygame.image.load("cricketer.png").convert_alpha(),(200,150))
rect=cricketer.get_rect(center= (screen_width//2,
                        screen_height//2-30))



def game_loop():
    clock=pygame.time.Clock()
    runnnig = True

    while runnnig:
     for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running= False


        display_surface.blit(background_image, (0,0))
        display_surface.blit(cricketer,rect)


        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__=="image":
   game_loop()

