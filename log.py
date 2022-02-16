import logging

logging.basicConfig(
    format="[%(asctime)s][%(name)s][%(levelname)s] ~ %(message)s",
    level=logging.INFO
)

logger = logging.getLogger() # create instance of logging class (with configs above)

logger.info('abc')