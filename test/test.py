import logging

logging.basicConfig(level=logging.DEBUG)

for i in range(10):
    logging.debug(f"test log {i}")
    logging.info(f"test log {i}")
    logging.warning(f"test log {i}")
    logging.error(f"test log {i}")
    logging.critical(f"test log {i}")
    print("123")
