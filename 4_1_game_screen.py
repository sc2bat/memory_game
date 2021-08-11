# 게임화면기본
# num_count = (level // 3) + 5
# num_count = min(num_count, 20)
# 격자를 그리고 나서 숫자를 랜덤으로 채움
# 리스트를 중복으로 활용
# grid = [[0 for col in range(columns)] for row in range(rows)]
# [[0, 0, 0 , 0, 2, 0, 0, 0],
#  [0, 0, 1 , 0, 0, 0, 0, 0],
#  [0, 0, 0 , 0, 3, 0, 0, 0],
#  [5, 0, 0 , 0, 0, 0, 4, 6],
#  [0, 0, 0 , 0, 0, 0, 0, 0]]

import pygame
from random import *

# level
def setup(level):
    # 숫자 몫을 구한뒤 더하기
    num_count = (level // 3) + 5 
    # 20 이상이면 20으로 
    num_count = min(num_count, 20)

    # 격자 그리기 및 랜덤 숫자 배치
    shuffle_grid(num_count)

# 숫자 셔플***
def shuffle_grid(num_count):
    rows = 5
    columns = 9
# 5 * 9 격자 생성
    grid = [[0 for col in range(columns)] for row in range(rows)]
    # 시작 1부터 num_count 까지
    number = 1 
    while number <= num_count:
        row_idx = randrange(0, rows) # 0 1 2 3 4
        col_idx = randrange(0, columns) 
        
        if grid[row_idx][col_idx] == 0:
            # 숫자 지정
            grid[row_idx][col_idx] = number
            number += 1

    print(grid) # 확인


def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)

def check_btns(pos):
    global start
    if start_button.collidepoint(pos):
        start = True    

def display_game_screen():
    print("Game Start")

pygame.init()
screen_width = 1280
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")

start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height - 120) 
BLACK = (0, 0 , 0) 
WHITE = (255, 255, 255)

start = False

# 게임 시작 전
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