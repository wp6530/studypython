# python模块

## 导入模块
>  导入模块的几种方法
```python3
import module
from module.xx.xx import xx
from module.xx.xx import xx as rename
from module.xx.xx import * 
```
导入模块其实就是告诉Python解释器去解释那个py文件
* 导入一个py文件，解释器解释该py文件
* 导入一个包，解释器解释该包下的 \_\_init__.py 文件

> 查看模块路径
```python3
import sys
print(sys.path)
```
> 添加路径
```python3
import sys 
import os
project_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_path) 
```
## 