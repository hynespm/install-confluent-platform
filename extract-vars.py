import os
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

logging.info(os.environ['GITHUB_REF'])