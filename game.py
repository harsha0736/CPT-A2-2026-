import pygame
import sys
import random

pygame.init()
height = 500
width = 700
block_size = 20
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("🐍 Snake Game")
Black = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
RED= (255, 0, 0)


#speed of snake per fps
clock = pygame.time.Clock()
font= pygame.font.SysFont(None,36)

#Snake and food 
def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, GREEN,(*block, block_size, block_size))

#food position
def draw_food(pos):
    pygame.draw.rect(screen,RED, (*pos, block_size, block_size))
#message function
def message(text, color):
    mesg = font.render(text, True, color)
    screen.blit(mesg, [width // 4, height // 2])    

def game_loop():
    snake=[(100, 100)]
    direction = 'RIGHT'
    change= direction
    food=[random.randrange(0,width,block_size), random.randrange(0,height,block_size)]
    score = 0
    #game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    change = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    change = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    change = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    change = 'RIGHT'
        direction = change
        x, y = snake[0]
        if direction == 'UP':
            y -= block_size
        elif direction == 'DOWN':
            y += block_size
        elif direction == 'LEFT':
            x -= block_size
        elif direction == 'RIGHT':
            x += block_size
        head=(x, y)
        if x<0 or x>=width or y<0 or y>=height or head in snake:
            screen.fill(Black)
            message("Game Over! Score:" + str(score),RED)
            pygame.display.update()
            pygame.time.delay(2000)
            return
        snake.insert(0, head)
        if head == tuple(food):
            score += 1
            food = [random.randrange(0, width, block_size), random.randrange(0, height, block_size)]
        else:
            snake.pop()
        screen.fill(Black)
        draw_snake(snake)
        draw_food(food)
        score_text = font.render("Score: " + str(score), True, WHITE)
        screen.blit(score_text, (10, 10))
        pygame.display.update()
        clock.tick(10)
game_loop()