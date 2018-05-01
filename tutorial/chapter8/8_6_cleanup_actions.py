"""
使用finally进行异常之后的清理工作
"""
try:
    raise KeyboardInterrupt
finally:
    print("Goodbye, world!")


