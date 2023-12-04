from inspect import currentframe
from logging import Logger as Log
from _common import _common as _common_


@_common_.exception_handler
def get_size(fpath: str, size_name: str = "MB", logger: Log = None) -> int:
    """
    Calculates the size of a file at a given path in a specified unit.

    This function determines the size of a file located at 'fpath' and converts it into
    a specified unit (e.g., KB, MB, GB). If the specified unit is not valid, it logs an
    error message using the provided logger.

    Args:
        fpath: The path to the file whose size needs to be calculated.
        size_name: The unit of file size measurement. Defaults to 'MB'.
        logger: A logging object for logging error messages. Defaults to None.

    Returns:
        int: The size of the file in the specified unit.

    Raises:
        ValueError: If the specified size_name is not a valid unit from the predefined list.

    """

    size = ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"]
    if size_name not in size:
        _common_.error_logger(currentframe().f_code.co_name,
                             f"size_name {size_name} not found, valid list is {size}",
                              logger=logger,
                              mode="error",
                              ignore_flag=False)
    from os import path
    return int(path.getsize(fpath) / 1024 ** size.index(size_name))


@_common_.exception_handler
def string_index(string: str, pattern: str, first_char: str = None) -> int:
    """
    Finds the index of the first occurrence of a pattern in a string.

    This function implements a string searching algorithm to find the first occurrence of a given pattern
    within a specified string. If a first character is provided, it searches for the pattern starting from
    that character. If the pattern is not found, the function returns -1.

    Args:
        string: The string in which to search for the pattern.
        pattern: The pattern to search for within the string.
        first_char: A character at which to start the search. Defaults to None.

    Returns:
        int: The index of the first occurrence of the pattern in the string, or -1 if not found.

    """
    _lp_ptr, _str_ptr, _lps = 1, 0, [0]
    while _str_ptr < len(pattern):
        if pattern[_str_ptr] == pattern[_lp_ptr]:
            _lps.append(_lp_ptr + 1)
            _lp_ptr, _str_ptr = _lp_ptr + 1, _str_ptr + 1
        elif _lp_ptr == 0:
            _lps.append(0)
            _str_ptr += 1
        else:
            _lp_ptr = _lps[_lp_ptr - 1]

    _lp_ptr, _str_ptr = 0, 0
    while _str_ptr < len(string):
        if first_char and string[_str_ptr] == first_char:
            return _str_ptr
        if string[_str_ptr] == pattern[_lp_ptr]:
            _lp_ptr, _str_ptr = _lp_ptr + 1, _str_ptr + 1
        elif _lp_ptr == 0:
            _str_ptr += 1
        else:
            _lp_ptr = _lps[_lp_ptr - 1]
        if _lp_ptr == len(pattern):
            return _str_ptr - _lp_ptr
    return -1
