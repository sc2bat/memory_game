import pygame

# 시작화면 보여주기
def display_start_screen():
    # 원 그리기 흰색, 시작버튼 중심 반지름 60 두께 5
    pygame.draw.circle(screen, WHITE, start_btn.center, 60, 5)

pygame.init()
screen_width = 1280
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")

# 시작 버튼
start_btn = pygame.Rect(0, 0, 120, 120) # 120, 120 사각형 만들고
start_btn.center = (120, screen_height - 120) # 화면 기준 좌측 아래쪽에 위치
# 색
BLACK = (0, 0 , 0) # Rgb
WHITE = (255, 255, 255)

running = True
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False 

    # 배경
    screen.fill(BLACK)
    # 시작 화면
    display_start_screen()
    # 화면 업데이트
    pygame.display.update()

pygame.quit()