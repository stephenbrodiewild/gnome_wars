import logging

# Create a logger for each module
logger = logging.getLogger(__name__)


def ten():
    logger.info("Returning 10")
    return 10
