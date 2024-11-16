import pygame
pygame.init()
width, height = 500, 500
mw = pygame.display.set_mode((width, height))
mw.fill("gray")
pygame.display.set_caption("Клікер")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
background = BLACK
button_color = BLACK
button_rect = pygame.Rect(8, 8, 205, 110)
font = pygame.font.Font(None, 74)
clock = pygame.time.Clock()
clock.tick(40)
click_c = 0
running = True
while running:
    mw.fill(WHITE)
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            if event.key == pygame.MOUSEBUTTONDOWN:
                if button_rect.colli:
                    click_c += 1
    pygame.draw.rect(mw, button_color, button_rect)
    button_text = font.render("click", True, WHITE)
    button_text2 = font.render("on me", True, WHITE)
    mw.blit(button_text, (button_rect ))
    text = font.render(str(click_c), True, BLACK)
    mw.blit(text, (width//2 - text.get_width()//2, height//2 - text.get_height()//2))


    pygame.display.update()
pygame.quit()
