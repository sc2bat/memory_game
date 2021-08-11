# 게임화면으로 넘어가는 동작

import pygame

def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)

# pos에 해당하는 버튼 확인
def check_btns(pos):
    global start # 전역 변수
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

# 게임 시작여부
start = False

running = True
while running:
    # 변수
    click_pos = None

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False 
    # 사용자가 클릭을 했을때
        elif event.type == pygame.MOUSEBUTTONUP:
            click_pos = pygame.mouse.get_pos() # 클릭 좌표 정보
            print(click_pos)

    screen.fill(BLACK)
    if start: # 게임 화면 표시
        display_game_screen() # 게임 화면
    else:
        display_start_screen() # 시작 화면

    # click_pos 가 None 이 아니라면 어딘가 클릭했다면
    if click_pos:
        check_btns(click_pos)

    pygame.display.update()

pygame.quit()