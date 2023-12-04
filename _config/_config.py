from collections import defaultdict
from inspect import currentframe
from typing import Dict
from _common import _common as _common_
from _util import _util_file as _util_file_

__version__ = "0.5"


class PGConfigSingleton:
    def __new__(cls, config_loc: str = ".".join(__file__.split(".")[:-1]) + ".yaml"):
        """
        This class ensures that only one instance exists configuration.
        It loads configuration settings from a YAML file, and if the file is not empty,
        it populates the configuration.

        Args:
            config_loc: The location of the configuration file.
                Defaults to the same directory as the current file with a '.yaml' extension.

        Returns:
            PGConfigSingleton: The singleton instance of the class.

        Raises:
            Exception: If there is an error while loading the YAML file, it is logged and re-raised.
        """

        if not hasattr(cls, "instance"):
            cls.config = defaultdict(str)
            cls.instance = super(PGConfigSingleton, cls).__new__(cls)

            try:
                if not _util_file_.is_file_empty(config_loc):
                    for _name, _val in _util_file_.yaml_load(config_loc).items():
                        cls.config[_name] = _val
            except Exception as err:
                _common_.error_logger(currentframe().f_code.co_name,
                                      err,
                                      logger=None,
                                      mode="error",
                                      ignore_flag=False)
        return cls.instance
