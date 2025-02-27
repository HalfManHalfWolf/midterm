# Author: Calipha Musa
# Date: 2/27/25

import re
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def analyze(log_file):
    failed_attempts = []

    failed_logins = re.compile(r"Login failed: (\w+)")

    try:
        with open(log_file, 'r') as file:
            for line in file:
                match = failed_logins.search(line)
                if match:
                    username = match.group(1)
                    failed_attempts.append(username)
                    logging.info(f"Failed login for user: {username}")
                    print(f"Failed login for user: {username}")

                    if failed_attempts.count(username) > 3:
                        logging.warning(f"INTRUDER ALERT!!!: {username}")

                else:
                    print("No failed login attempts")

    except FileNotFoundError:
        logging.error(f"The file {log_file} was not found.")
        print(f"The file {log_file} was not found.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        print(f"An error occurred: {e}")

log_file = 'secure-error-log.txt'

analyze(log_file)
