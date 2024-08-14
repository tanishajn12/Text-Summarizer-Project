#The code sets up a logging system that writes log messages to both a file (logs/running_logs.log) and the console.
#It creates a logger named "textSummarizerLogger" that you can use throughout your code to log messages with a consistent 
#format that includes timestamps, severity levels, and module names.


#os module, which provides functions for interacting with the operating system, such as file and directory manipulation.
import os

#sys module, which provides access to system-specific parameters and functions, such as input/output and command-line arguments.
import sys

#logging module, which is used to generate and manage log messages.
import logging


#logging_str: This variable defines the format of the log messages. The format string includes placeholders that will be replaced by actual values when a log message is generated:
#%(asctime)s: The time when the log message was generated.
#%(levelname)s: The severity level of the log message (e.g., INFO, WARNING, ERROR).
#%(module)s: The name of the module (script file) where the log message originated.
#%(message)s: The actual log message.

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

#Defines the name of the directory where the log file will be stored. 
log_dir = "logs"

log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)


# Configures the logging system with the specified settings
logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("textSummarizerLogger")
#Creates a logger object named "textSummarizerLogger". This logger can be used to generate log messages within 
#your application. The name "textSummarizerLogger" is used to identify this particular logger, which can be useful if you have multiple loggers in your application.