import logging

logger = logging.getLogger(__name__)


def add_int(x: int, y: int) -> int:
    """add two integer 
    Args:
        x (int): input 1
        y (int): input 2
    Returns:
        int: output
    """
    logger.debug(f"add two integers")
    return x + y
