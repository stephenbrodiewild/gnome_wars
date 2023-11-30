import pygame
import logging
import logging_config
import gnome_wars.math
import esper

logging_config.setup_logging()
logger = logging.getLogger(__name__)

FPS = 60
RESOLUTION = 720, 480


##################################
#  Define some Components:
##################################
class Velocity:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y


class Renderable:
    def __init__(self, image, posx, posy, depth=0):
        self.image = image
        self.depth = depth
        self.x = posx
        self.y = posy
        self.w = image.get_width()
        self.h = image.get_height()


################################
#  Define some Processors:
################################
class MovementProcessor:
    def __init__(self, minx, maxx, miny, maxy):
        super().__init__()
        self.minx = minx
        self.maxx = maxx
        self.miny = miny
        self.maxy = maxy

    def process(self):
        # This will iterate over every Entity that has BOTH of these components:
        for ent, (vel, rend) in esper.get_components(Velocity, Renderable):
            # Update the Renderable Component's position by it's Velocity:
            rend.x += vel.x
            rend.y += vel.y
            # An example of keeping the sprite inside screen boundaries. Basically,
            # adjust the position back inside screen boundaries if it tries to go outside:
            rend.x = max(self.minx, rend.x)
            rend.y = max(self.miny, rend.y)
            rend.x = min(self.maxx - rend.w, rend.x)
            rend.y = min(self.maxy - rend.h, rend.y)


class RenderProcessor:
    def __init__(self, window, clear_color=(0, 0, 0)):
        super().__init__()
        self.window = window
        self.clear_color = clear_color

    def process(self):
        # Clear the window:
        self.window.fill(self.clear_color)
        # This will iterate over every Entity that has this Component, and blit it:
        for ent, rend in esper.get_component(Renderable):
            self.window.blit(rend.image, (rend.x, rend.y))
        # Flip the framebuffers
        pygame.display.flip()


class GameState:
    def __init__(self):
        self.running = True


class EventProcessor:
    def __init__(self, player_entity, game_state):
        self.player_entity = player_entity
        self.game_state = game_state

    def process(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.handle_keydown(event)
            elif event.type == pygame.KEYUP:
                self.handle_keyup(event)

    def handle_keydown(self, event):
        vel = esper.component_for_entity(self.player_entity, Velocity)
        if event.key == pygame.K_LEFT:
            vel.x = -3
        elif event.key == pygame.K_RIGHT:
            vel.x = 3
        elif event.key == pygame.K_UP:
            vel.y = -3
        elif event.key == pygame.K_DOWN:
            vel.y = 3
        elif event.key == pygame.K_q:
            self.game_state.running = False

    def handle_keyup(self, event):
        vel = esper.component_for_entity(self.player_entity, Velocity)
        if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
            vel.x = 0
        if event.key in (pygame.K_UP, pygame.K_DOWN):
            vel.y = 0


def create_player_entity():
    player = esper.create_entity()
    esper.add_component(player, Velocity(x=0, y=0))
    esper.add_component(
        player,
        Renderable(image=pygame.image.load("assets/redsquare.png"), posx=100, posy=100),
    )
    return player


def create_enemy_entity():
    enemy = esper.create_entity()
    esper.add_component(
        enemy,
        Renderable(
            image=pygame.image.load("assets/bluesquare.png"), posx=400, posy=250
        ),
    )
    return enemy


def main():
    logger.info("Setting up Pygame")
    pygame.init()
    screen = pygame.display.set_mode(RESOLUTION)
    clock = pygame.time.Clock()
    game_state = GameState()
    
    logger.info("Creating entities")
    player = create_player_entity()
    create_enemy_entity()

    logger.info("Creating processors")
    event_processor = EventProcessor(player_entity=player, game_state=game_state)
    render_processor = RenderProcessor(window=screen)
    movement_processor = MovementProcessor(
        minx=0, maxx=RESOLUTION[0], miny=0, maxy=RESOLUTION[1]
    )

    logger.info("Beginning game loop")
    while game_state.running:
        event_processor.process()
        render_processor.process()
        movement_processor.process()
        clock.tick(FPS)

    logger.info("Quitting")
    pygame.quit()
