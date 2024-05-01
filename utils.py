import os  
import platform 
from string import Template

def fi(template_str, variables):  
    """  
    使用变量字典替换模板字符串中的变量。
    - 【参数】模板字符串：`包含要替换的变量的模板字符串`。

    - 【参数】替换的变量字典：`要在模板字符串中替换的变量字典`。

    - 返回结果：`替换了变量的模板字符串`。
    """  
    template = Template(template_str)  
    replaced_str = template.substitute(variables)  
    return replaced_str

def clear_console():  
    """
    自动识别系统执行清空命令

    - `Windows`: 执行 `cls` 命令

    - `Linux / Mac`: 执行 `clear` 命令
    """
    if platform.system().lower() == 'windows':
        os.system('cls')
    else:
        os.system('clear')