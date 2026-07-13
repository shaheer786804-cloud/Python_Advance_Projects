import logging as log
log.basicConfig( level=log.INFO ,filename="log.log" ,filemode="w")

logger = log.getLogger(__name__)
logger.info("Testing the custom logger")