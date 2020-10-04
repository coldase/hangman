import pygame
import string

pygame.init()
pygame.font.init()

screen_width = 400
screen_height = 400
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_size)

BLACK = (0,0,0)

img_empty = pygame.image.load("images/empty.png")
img_head = pygame.image.load("images/head.png")
img_body = pygame.image.load("images/body.png")
img_leftleg = pygame.image.load("images/leftleg.png")
img_rightleg = pygame.image.load("images/rightleg.png")
img_leftarm = pygame.image.load("images/leftarm.png")
img_rightarm = pygame.image.load("images/rightarm.png")

myfont = pygame.font.SysFont("Calibri", 50)

def draw_text(text, pos):
    nt = myfont.render(text, False, BLACK)
    screen.blit(nt, pos)

def get_states(state):
    global current
    if state == 1:
        current = img_empty
    if state == 2:
        current = img_head
    if state == 3:
        current = img_body
    if state == 4:
        current = img_leftleg
    if state == 5:
        current = img_rightleg
    if state == 6:
        current = img_leftarm
    if state == 7:
        current = img_rightarm


def replace_letters(current_word, letter):
    current_word_list = [x for x in current_word]
    hidden_word_list  =  ["*" for x in current_word]
    for i, l in enumerate(current_word_list):
        if letter == l:
            hidden_word_list[i] = letter
    return "".join(hidden_word_list)

clock = pygame.time.Clock()
run = True
FPS = 60
current_state = 1
current = img_empty
current_word = "tietokone"
hidden_word = len(current_word) * "*"
current_letter = None

while run:
    clock.tick(FPS)
    keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            run = False

        if event.type == pygame.KEYUP and pygame.key.name(event.key) in string.ascii_lowercase:
            current_letter = pygame.key.name(event.key)
            hidden_word = replace_letters(current_word, current_letter)

        if event.type == pygame.KEYUP and keys[pygame.K_UP]:
            current_state += 1
        if event.type == pygame.KEYUP and keys[pygame.K_DOWN]:
            current_state -= 1
            
    screen.blit(current, (0,0))
    get_states(current_state)
    draw_text(hidden_word, (50,50))
    draw_text(current_letter, (20, 200))
    pygame.display.flip()
pygame.quit()