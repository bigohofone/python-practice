import logging

child_logger = logging.getLogger('parent.child')

def do_something():
    child_logger.info(
        "This is a message from child"
    )
    
    
if __name__ == '__main__':
    do_something()