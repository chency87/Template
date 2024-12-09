import sys
import os
# Get the current directory (where your_script.py resides)
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)
from src import *
import random, logging
from sqlalchemy import text
from corekit.src import *

logger = logging.getLogger('src.test')
logger.info('this is a test of log')

from src.pipeline.graph import *