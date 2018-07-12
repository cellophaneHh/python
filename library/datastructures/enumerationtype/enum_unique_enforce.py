"""
禁止重复定义
"""

import enum


@enum.unique
class BugStatus(enum.Enum):

    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1
    # 加enum.unique之后不能重复定义，会报错
    by_design = 4
    closed = 1
