import logging
import time

logging.basicConfig(
                      filename="D://Pic//test.log",
                      format='%(asctime)s:%(levelname)s:%(message)s',
                      datefmt='%m/%d/%Y %I:%M:%S %p'

)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("This is debug message")
logger.info("This is info message")
logger.warning("This is a warning message")
logger.error("Error Message")

