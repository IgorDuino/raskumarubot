import logging
import os
import sys

from configs.env_configs_models import EnvConfigsModel
from core.wlui.formatter import formatter as wlui_formatter
from core.wlui.l_filter import WLUIFilter
from pydantic import ValidationError

root_logger = logging.getLogger()

if root_logger.handlers:
    root_logger.removeHandler(*root_logger.handlers)

consoleHandler = logging.StreamHandler()
consoleHandler.addFilter(WLUIFilter())
consoleHandler.setFormatter(wlui_formatter)
logging.getLogger("httpx").setLevel("CRITICAL")
logging.getLogger("httpcore").setLevel("CRITICAL")
root_logger.addHandler(consoleHandler)

_logger = logging.getLogger(__name__)

try:
    env_parameters = EnvConfigsModel(**os.environ)
except ValidationError as e:
    _logger.critical(exc_info=e, msg="Env parameters validation")
    sys.exit(-1)

if env_parameters.IS_DEBUG:
    root_logger.setLevel(logging.DEBUG)
else:
    root_logger.setLevel(logging.INFO)
