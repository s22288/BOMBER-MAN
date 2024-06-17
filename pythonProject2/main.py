import pygame
import   bomberMan
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)

#postacie
desired_size=(166,160)

bomb_img =pygame.image.load('bomber-mans/bomb/bomb.png')
bomb = pygame.transform.scale(bomb_img,desired_size)
bomb_rect = bomb.get_rect()
bomb_rect.center = 150,200
bomber_man_img = pygame.image.load('bomber-mans/blue/blue-forward.png')

BomberMan = bomberMan.BomberMan(100,100,'red',100,20,2,bomber_man_img,5)
desired_size_man=(60,60)
bomber_man = pygame.transform.scale(BomberMan.image,desired_size_man)
bomber_man_rect = bomber_man_img.get_rect()


pygame.display.set_caption("My Game")
bomber_man_rect.center =BomberMan.x, BomberMan.y
done = False

clock = pygame.time.Clock()
speed = BomberMan.speed

bombs_list = []
def create_bomb(x, y):
    bomb_new =  bomberMan.Bomb('dark', 2, x, y)
    bombs_list.append(bomb_new)

# Function to display all bombs
def display_bombs():
    for bomb in bombs_list:
        screen.blit(bomb.image, bomb.rect)


while not done:

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        print('up')
        bomber_man_rect.y-=speed
    if keys[pygame.K_s]:
        print('down')
        bomber_man_rect.y += speed
    if keys[pygame.K_d]:
        print('right')
        bomber_man_rect.x += speed
    if keys[pygame.K_a]:
        print('left')
        bomber_man_rect.x -= speed
    if keys[pygame.K_SPACE]:
        print('bomb')
        create_bomb(BomberMan.x,BomberMan.y)
    if keys[pygame.K_UP]:
        print('up')
        bomber_man_rect.y -= speed
    if keys[pygame.K_DOWN]:
        print('down')
        bomber_man_rect.y += speed
    if keys[pygame.K_RIGHT]:
        print('right')
        bomber_man_rect.x += speed
    if keys[pygame.K_LEFT]:
        print('left')
        bomber_man_rect.x -= speed
    if keys[pygame.K_BACKSPACE]:
        print('bomb')
        bomb_rect = bomb.get_rect()
        Bomb_create = bomb_rect.center = BomberMan.x, BomberMan.y
        bombs_list.append(Bomb_create)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    print(bombs_list)
    screen.fill(WHITE)
    screen.blit(bomb_img,bomb_rect)
    screen.blit(bomber_man,bomber_man_rect)
    pygame.display.flip()
    display_bombs()

    clock.tick(60)

pygame.quit()
