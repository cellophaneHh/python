"""
模块搜索路径
1、首先根据名称搜索内置模块
2、如果没有从内置模块中搜索到，则从sys.path中搜索

sys.path初始化包括下列位置
1、包含当前输入脚本的目录(当前目录)
2、PYTHONPATH（和shell中PATH变量格式相同的一个目录列表）
3、安装时定义的默认目录
"""
