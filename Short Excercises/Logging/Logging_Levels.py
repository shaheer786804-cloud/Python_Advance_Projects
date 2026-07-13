import logging as log
# logging levels
log.basicConfig(level=log.ERROR , filename="log.log" , filemode="w")

log.debug("Debugging")
log.info("Info")
log.warning("Warning")
log.error("error")
log.critical("critical")

