import pygame
import logging
import logging_config
import gnome_wars.math

logging_config.setup_logging()
logger = logging.getLogger(__name__)


def main():
    # just to show how u would import stuff tbh
    gnome_wars.math.ten()

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    while running:
        # poll for events
        for event in pygame.event.get():
            # Check for keydown event
            if event.type == pygame.KEYDOWN:
                # Check if the 'Q' key is pressed
                if event.key == pygame.K_q:
                    logger.info("Pressed Q")
                    running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")

        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()
