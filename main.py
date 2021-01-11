import os
import sys
import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Cursor(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_image('cursor.png')
        self.visible = False
        self.x, self.y = 0, 0

    def change_visible(self, k):
        self.visible = k

    def change_coords(self, x, y):
        self.x, self.y = x, y

    def ret_coords(self):
        return self.x, self.y


if __name__ == '__main__':
    pygame.init()
    size = width, height = 500, 500
    pygame.mouse.set_visible(False)
    screen = pygame.display.set_mode(size)
    running = True
    mouse = Cursor()
    while running:
        screen.fill('black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if pygame.mouse.get_focused():
                mouse.change_visible(True)
                if event.type == pygame.MOUSEMOTION:
                    x, y = event.pos
                    mouse.change_coords(x, y)
            if not pygame.mouse.get_focused():
                mouse.change_visible(False)
        if mouse.visible:
            screen.blit(mouse.image, mouse.ret_coords())
        pygame.display.flip()
