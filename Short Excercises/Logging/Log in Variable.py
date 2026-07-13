import logging as log
# logging levels
log.basicConfig(level=log.DEBUG , filename="log.log" , filemode="w")

y = 3
log.info(f"The value of y is {y}")