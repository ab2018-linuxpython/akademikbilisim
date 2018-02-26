import requests
import sh
import datetime
import logging, logging.handlers

logger = logging.getLogger("agent")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.handlers.RotatingFileHandler("agent.log"))
FORMAT = "[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s"
logging.basicConfig(format=FORMAT)


data = {
    "hostname": sh.cat("/etc/hostname").stdout.decode().strip(),
    "username": sh.whoami().stdout.decode().strip(),
    "time": datetime.datetime.now().isoformat(),
    "stats": {
        
        }
    }
logger.debug(str(data), extra={})
response = requests.post("http://127.0.0.1:8080/", json=data)
logger.debug(response.text)
logger.info(response.status_code)
