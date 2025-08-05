import os
from loguru import logger


base_dir = os.path.dirname(__file__)
log_dir = os.path.join(base_dir, "logs")
os.makedirs(log_dir, exist_ok=True)

# Setup logging with daily rotation
# Verbose log
verbose_log_file = "verbose_log_{time:YYYY-MM-DD!UTC}.log"

logger.add(
    os.path.join(log_dir, verbose_log_file),
    rotation="00:00",
    retention="30 days",
    compression=zip,
    level="DEBUG",
    format="{time:YYYY-MM-DD HH:mm:ss.SSS!UTC} UTC | {name}:{function}:{line} | {level} | {message}",
    filter=lambda record: record["extra"].get("log_type") == "verbose",
)

verbose_logger = logger.bind(log_type="verbose")
