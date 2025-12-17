import logging

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
logger.addHandler(stream_handler)

file_handler = logging.FileHandler('example.log')
file_handler.setLevel(logging.CRITICAL)
logger.addHandler(file_handler)


class CustomFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return 'Filter this message' not in record.getMessage()


custom_filter = CustomFilter()
logger.addFilter(custom_filter)


def do_something():
    logger.info("Hi!")
    logger.info("[Filter this message] Hi!")
    logger.critical("Hurts!")
    
    
if __name__ == '__main__':
    do_something()