import logging as log
# logging levels
log.basicConfig(level=log.DEBUG , filename="log.log" , filemode="w")

try:
    1/0
except Exception as e:
    log.exception("An error Occur :")