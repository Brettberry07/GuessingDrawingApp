from globals import *

class Button:
    outline = 1
    hovering = False
    color = ""

    def __init__(self, x, y, width, height, light_color, dark_color, text, command=None):
        # super().__init__()
        self.light_color = light_color
        self.dark_color = dark_color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.command = command
        self.text = text
        self.color = dark_color

    def update(self):
        self.is_hover(pygame.mouse.get_pos(), pygame.mouse.get_pressed()[0])
        self.do_command()

    def draw(self):
        # drawing the outline
        self.update()
        pygame.draw.rect(screen, (0, 0, 0), (
        self.x - self.outline, self.y - self.outline, self.width + self.outline * 2, self.height + self.outline * 2))
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

        if self.text != '':
            myfont = pygame.font.SysFont('Consolas', 24)
            text = myfont.render(self.text, 1, (0, 0, 0))
            screen.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))


    def is_hover(self, mouse_pos, is_clicking):
        if is_clicking:
            self.color = (255, 255, 255)
            self.outline = 2
        # To see if the mouse is hovering over the button
        # checks to see if the mouse_pos, a tuple, first
        # value,x, is inside the button, then repeat for y

        '''
        width 200
        height 50

        ################
        #              #
        ################
        
        '''
        if mouse_pos[0] > self.x and mouse_pos[0] < self.x + self.width:
            if mouse_pos[1] > self.y and mouse_pos[1] < self.y + self.height:
                self.hovering = True
                if is_clicking == False:
                    self.color = self.light_color
            else:
                self.outline = 1
                self.color = self.dark_color
                self.hovering = False
        else:
            self.outline = 1
            self.color = self.dark_color
            self.hovering = False

    def do_command(self):
        if self.hovering and pygame.mouse.get_pressed()[0]:
            self.color = (255, 255, 255)
            if self.command is not None:
                self.command()


class Text_Field():
    outline = 1

    def __init__(self, x, y, width, height, text="", center_text=False):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.center_text = center_text

    def draw(self):
        pygame.draw.rect(screen, (0, 0, 0), (
        self.x - self.outline, self.y - self.outline, self.width + self.outline * 2, self.height + self.outline * 2))
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height))
        myfont = pygame.font.SysFont('Consolas', 24)
        text = myfont.render(self.text, 1, (0, 0, 0))
        if self.center_text:
            screen.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))
        else:
            screen.blit(text, (self.x, self.y + (self.height / 2 - text.get_height() / 2)))

    # To center the text or not
    # self.x + (self.width/2 - text.get_width()/2),
    def update_text(self, new_text):
        self.text = new_text