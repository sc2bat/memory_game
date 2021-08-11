# 
# cell_size = 130
# btn_size = 110
# screen_l_margin = 55
# screen_t_margin = 20

# center_x = screen_l_margin + (col_idx * cell_size) + (cell_size / 2)
# center_y = screen_t_margin + (row_idx * cell_size) + (cell_size / 2)

# btn = pygame.Rect(0, 0, btn_size, btn_size)
# btn.center = (center_x, center_y)

# num_btns.append(btn)

import pygame
from random import *

def setup(level):
    num_count = (level // 3) + 5 
    num_count = min(num_count, 20)

    shuffle_grid(num_count)

def shuffle_grid(num_count):
    rows = 5
    columns = 9
    # cell 가로 세로
    cell_size = 130
    # 그려질 버튼 크기
    btn_size = 110
    # 스크린 왼쪽, 위쪽 여백
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

            # cur_grid_cell 위치 기준 x, y 구함
            center_x = screen_l_margin + (col_idx * cell_size) + (cell_size / 2)
            center_y = screen_t_margin + (row_idx * cell_size) + (cell_size / 2)
            # 숫자 버튼 그리기
            btn = pygame.Rect(0, 0, btn_size, btn_size)
            btn.center = (center_x, center_y)
            # 버튼들을 리스트에 
            num_btns.append(btn)

    print(grid) # 확인


def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)

def display_game_screen():
    # print("Game Start")
    for idx, rect in enumerate(num_btns, start=1):
        # 회색에 해당하는 rect 를 그림
        pygame.draw.rect(screen, GRAY, rect)
        # 숫자 텍스트
        cell_text = game_font.render(str(idx), True, WHITE)
        text_rect = cell_text.get_rect(center=rect.center)
        screen.blit(cell_text, text_rect)

def check_btns(pos):
    global start
    if start_button.collidepoint(pos):
        start = True

pygame.init()
screen_width = 1280
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")

# 폰트
game_font = pygame.font.Font(None, 120)

start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height - 120) 
BLACK = (0, 0 , 0) 
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)

# player 가 눌러야하는 버튼
num_btns = [] 

start = False

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