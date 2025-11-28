# src/utils/logger.py
import sys
from loguru import logger

# Remove default handler
logger.remove()

logger = logger

# Console + File logging
logger.add(
    sys.stderr,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level="INFO",
    colorize=True,
)

logger.add(
    "logs/app.log",
    rotation="10 MB",
    retention="7 days",
    compression="zip",
    level="DEBUG",
    backtrace=True,
    diagnose=True,
)

# Create logs directory if not exists
import os
os.makedirs("logs", exist_ok=True)

__all__ = ["logger"]