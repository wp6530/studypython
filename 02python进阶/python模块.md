# pythonģ��

## ����ģ��
>  ����ģ��ļ��ַ���
```python3
import module
from module.xx.xx import xx
from module.xx.xx import xx as rename
from module.xx.xx import * 
```
����ģ����ʵ���Ǹ���Python������ȥ�����Ǹ�py�ļ�
* ����һ��py�ļ������������͸�py�ļ�
* ����һ���������������͸ð��µ� \_\_init__.py �ļ�

> �鿴ģ��·��
```python3
import sys
print(sys.path)
```
> ���·��
```python3
import sys 
import os
project_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_path) 
```
## 