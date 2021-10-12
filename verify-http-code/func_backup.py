import io
import logging
import requests
from fdk import response


def handler(ctx, data: io.BytesIO = None):
    url = "http://140.238.126.98:5000"

    logging.getLogger().info("Start of Verify HTTP Code")

    try:
        resp = requests.head(url)
        if resp.status_code == 200:
            logging.getLogger().info("URL is accessible")
            return True
        else:
            logging.getLogger().info("URL is not accessible")
            return False

    except requests.exceptions.ConnectionError:
        logging.getLogger().info("Connection Error")
        return False
