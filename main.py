import sys
from loguru import logger


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'

def start_logging():
    log_format: str = '{time:YYYY-MM-DD HH:mm:ss} - {name} - {level} - {function} - {message}'
    logger.remove()
    logger.add('formatted_log.txt', format = log_format, rotation = '1 MB', retention = '5 days')
    # Add a handler that logs only DEBUG messages to stdout
    logger.add(sys.stdout, level = 'DEBUG', filter = lambda record: record["level"].name == "DEBUG")

def main():
    start_logging()
    logger.debug('top')
    msg = f'Python version: {get_python_version()}'
    logger.debug(msg)
    logger.info(msg)
    logger.debug('bottom')

if __name__ == '__main__':
    main()