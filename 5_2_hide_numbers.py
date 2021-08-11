# 숫자 숨기기

import pygame
from random import *

def setup(level):
    # 일정시간 동안 숫자 보임
    global display_time
    display_time = 5 - (level // 3)
    display_time = max(display_time, 1)

    num_count = (level // 3) + 5 
    num_count = min(num_count, 20)

    shuffle_grid(num_count)

def shuffle_grid(num_count):
    rows = 5
    columns = 9
    cell_size = 130
    btn_size = 110
    screen_l_margin = 55
    screen_t_margin = 20

    grid = [[0 for col in range(columns)] for row in range(rows)]
    number = 1 
    while number <= num_count:
        row_idx = randrange(0, rows) # 0 1 2 3 4
        col_idx = randrange(0, columns) 
        
        if grid[row_idx][col_idx] == 0:
            grid[row_idx][col_idx] = number
            number += 1

            center_x = screen_l_margin + (col_idx * cell_size) + (cell_size / 2)
            center_y = screen_t_margin + (row_idx * cell_size) + (cell_size / 2)
            btn = pygame.Rect(0, 0, btn_size, btn_size)
            btn.center = (center_x, center_y)
            num_btns.append(btn)

    print(grid) # 확인


def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)

def display_game_screen():
    # 시간 계산하여 숫자 숨김 여부 
    global hidden
    if not hidden:
        # ms -> sec
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
        if elapsed_time > display_time:
            hidden = True

    for idx, rect in enumerate(num_btns, start=1):
        if hidden: 
            pygame.draw.rect(screen, GRAY, rect)
        else:
            cell_text = game_font.render(str(idx), True, WHITE)
            text_rect = cell_text.get_rect(center=rect.center)
            screen.blit(cell_text, text_rect)

def check_btns(pos):
    global start, start_ticks
    if start: 
        check_num_btns(pos)
    elif start_button.collidepoint(pos):
        start = True
        # 현재 시간을 저장
        start_ticks = pygame.time.get_ticks()

def check_num_btns(pos):
    global hidden 
    for btn in num_btns:
        if btn.collidepoint(pos):
            if btn == num_btns[0]:
                print("Correct")
                del num_btns[0]
                if not hidden:
                    hidden = True
            else:
                print("Wrong")
            break

pygame.init()
screen_width = 1280
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")

game_font = pygame.font.Font(None, 120)

start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height - 120) 
BLACK = (0, 0 , 0) 
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)

num_btns = [] 
# 숫자를 보여주는 시간
display_time = None
# 시간 계산(현재 시간 정보 저장)
start_ticks = None

start = False
hidden = False

setup(1) 

running = True
while running:
    click_pos = None

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False 
        elif event.type == pygame.MOUSEBUTTONUP:
            click_pos = pygame.mouse.get_pos() 
            print(click_pos)

    screen.fill(BLACK)
    if start: 
        display_game_screen() 
    else:
        display_start_screen()

    if click_pos:
        check_btns(click_pos)

    pygame.display.update()

pygame.quit()