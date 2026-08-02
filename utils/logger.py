import logging
import os

# Create log directory if it does not exist
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Configure the logger instance
logger = logging.getLogger("API_Automation_Framework")
logger.setLevel(logging.INFO)

# Define clear, readable log formatting patterns
formatter = logging.Formatter(
    fmt="%(asctime)s [%(levelname)s] (%(filename)s:%(lineno)d) - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# 1. Console stream handler (for real-time pipeline monitoring)
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# 2. File output handler (for persistent audit trails)
file_handler = logging.FileHandler(os.path.join(log_dir, "framework.log"), encoding="utf-8")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
