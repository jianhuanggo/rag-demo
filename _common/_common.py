import functools
from sys import exit
from logging import Logger as Log
from typing import List, Union, Tuple, Callable, Dict, Any, TypeVar


RT = TypeVar('RT')

__version__ = "0.5"


def info_logger(message: str = "",
                func_str: str = "",
                logger: Log = None,
                addition_msg: str = "") -> None:
    """
    Logs or prints an informational message, optionally including the calling function's name and additional message.

    This function allows for flexible logging of informational messages. If a logger object is provided, the message
    is logged using that logger; otherwise, it is printed to the standard output. The function also supports adding
    the name of the function that generated the message and an additional message for more context.

    Args:
        message: The primary message to be logged or printed.
        func_str: The string representation of the calling function's name. If provided, it is prepended to the message.
        logger: A logging.Logger object used for logging the message. If None, the message is printed instead.
        addition_msg: An additional message that can be appended to the primary message for more context.

    Raises:
        Exception: Propagates any exception that might occur during logging or printing.
    """
    try:
        if func_str:
            message = f"{func_str}: {message}"
        logger.info(f"{message} {addition_msg}") if logger else print(f"{message} {addition_msg}")
    except Exception as err:
        raise err


def error_logger(func_str: str, error,
                 logger: Log = None,
                 addition_msg: str = "",
                 mode: str = "critical",
                 ignore_flag: bool = True,
                 set_trace: bool = False) -> None:
    """
    Logs an error message based on the specified logging mode.

    Args:
        func_str: The name of the function where the error occurred.
        error: The error object or message to be logged.
        logger: The logging object to be used. Defaults to None.
        addition_msg: Additional message to be appended to the error message. Defaults to "".
        mode: The logging level - 'critical', 'debug', 'error', or 'info'. Defaults to "critical".
        ignore_flag: Flag to determine whether to ignore the error or exit. Defaults to True.
        set_trace: If True, logs a stack trace along with the error message. Defaults to False.

    Raises:
        RuntimeError: If the logging mode is invalid.

    """

    def _not_found(*args, **kwargs):
        raise "error mode should be 'critical', 'debug', 'error' and 'info'"
    if logger:
        _logger_mode = {"critical": logger.critical,
                        "debug": logger.debug,
                        "error": logger.error,
                        "info": logger.info
                        }
    try:
        _logger_mode.get(mode, _logger_mode)(f"Error in {func_str} {addition_msg} {error}") if logger \
            else print(f"Error in {func_str} {addition_msg} {error}")
        if logger and set_trace: logger.exception("trace")
        return exit(99) if not ignore_flag else None
    except Exception as err:
        raise err


def exception_handler(func):
    """
    A decorator that wraps a function with exception handling logic.

    This decorator catches any exceptions thrown by the decorated function and logs them
    using the 'error_logger' function. It also allows for injecting a logger through
    function keyword arguments.

    Args:
        func: The function to be decorated.

    Returns:
        Callable: The wrapped function with exception handling.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as err:
            error_logger(func.__name__,
                         err,
                         logger=kwargs.get("logger"),
                         mode="error",
                         ignore_flag=False)

    return wrapper
