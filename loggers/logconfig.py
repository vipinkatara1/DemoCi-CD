import logging


handler = logging.FileHandler(f"orderapi.log")
formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')