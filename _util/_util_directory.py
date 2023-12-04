import os
import shutil
from inspect import currentframe
from logging import Logger as Log
from _common import _common as _common_


@_common_.exception_handler
def create_directory(dirpath: str, logger: Log = None) -> bool:
    """
    Creates a directory at the specified path.

    This function attempts to create a new directory at the given path. If the directory already exists,
    it returns True without creating a new one. If an error occurs during directory creation, it logs
    the error using the provided logger.

    Args:
        dirpath: The path where the directory should be created.
        logger: A logger object for logging messages. Defaults to None.

    Returns:
        bool: True if the directory is successfully created or already exists, False otherwise.
    """
    try:
        o_umask = os.umask(0)
        os.makedirs(dirpath)
    except FileExistsError:
        return True
    except OSError:
        if not os.path.isdir(dirpath):
            _common_.error_logger(currentframe().f_code.co_name,
                                 f"creation of the directory {dirpath} failed",
                                  logger=logger,
                                  mode="error",
                                  ignore_flag=True)
    except Exception as err:
        _common_.error_logger(currentframe().f_code.co_name,
                              err,
                              logger=logger,
                              mode="error",
                              ignore_flag=True)
    else:
        _common_.info_logger(f"Successfully created the directory {dirpath}",
                             logger=logger)
    finally:
        os.umask(o_umask)

    return True


@_common_.exception_handler
def remove_directory(dirpath: str, logger: Log = None) -> bool:
    """
    Deletes a specified directory along with all its contents.

    This function attempts to remove the directory located at 'dirpath', including all
    files and subdirectories contained within it. The removal is performed using the
    `shutil.rmtree` method from the Python standard library.

    Args:
        dirpath: The path of the directory to be removed.
        logger: A logger object for logging error messages, if needed. Defaults to None.

    Returns:
        bool: True, indicating the function was called. Note that this does not necessarily
        mean the directory was successfully removed, as no error checking is performed.

    """


    shutil.rmtree(dirpath)
    return True




