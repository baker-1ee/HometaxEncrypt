import logging.config
import json

with open('logging.json', 'rt') as f:
    config = json.load(f)
    logging.config.dictConfig(config)
log = logging.getLogger()
