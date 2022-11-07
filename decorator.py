from datetime import datetime
from debug_tools import decorator_param, decorator


@decorator
def general(n):
    list_generator = [item ** 2 for item in range(1, n)]
    return list_generator



@decorator_param(path='info_with_param.log')
def general(n):
    list_generator = [item ** 2 for item in range(1, n)]
    return list_generator

general(10)