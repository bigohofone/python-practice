import logging


logging.basicConfig(
	level=logging.INFO
)


def do_something():
    logging.debug("디버그")
    logging.info("알림")
    logging.warning("경고")
    logging.error("오류")
    logging.critical("중요")
    
    
if __name__ == '__main__':
    do_something()