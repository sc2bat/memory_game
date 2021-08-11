import pygame

# 초기화
pygame.init()
screen_width = 1280
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")

# 게임 루프
running = True # 게임이 진행 중인지 확인
while running:
    # event loop
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤인가?
            running = False # 게임이 더 이상 실행 중이지 않음

# 게임종료
pygame.quit()