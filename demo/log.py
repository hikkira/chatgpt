import logging


def get_logger(log_prefix: str):
    # Create a logger object
    logger = logging.getLogger(log_prefix)
    logger.setLevel(logging.DEBUG)

    # Create console handler and set level to DEBUG
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # Create file handler and set level to INFO
    fh = logging.FileHandler(filename="my_log_file.log", encoding='utf-8')
    fh.setLevel(logging.INFO)

    # Create a formatter
    formatter = logging.Formatter(
        "%(asctime)s.%(msecs)03d - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Add formatter to handlers
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # Add handlers to logger
    logger.addHandler(ch)
    logger.addHandler(fh)
    return logger
