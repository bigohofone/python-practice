import logging
from child import do_something as child_do_something

parent_logger = logging.getLogger('parent')
parent_logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

stream_handler.setFormatter(formatter)
parent_logger.addHandler(stream_handler)


def do_something():
    parent_logger.info(
        "This is a message from parent"
    )
    child_do_something()
    
    
if __name__ == '__main__':
    do_something()