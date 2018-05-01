"""
每个模块中需要一个__init__.py文件，告诉python这是一个包含包的目录

使用 import item.subitem.subsubitem 方式导入模块时
最后一个item可以是模块或者包名，但是不能是前一个模块中定义的函数、变量或类名
"""
import sound.effects.echo

from sound.effects import echo

