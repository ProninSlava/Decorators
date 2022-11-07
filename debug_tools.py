from datetime import datetime
from functools import wraps



def decorator(general):

    def new_func(*args, **kwargs):
        time = datetime.now().replace(microsecond=0)

        rezult = general(*args, **kwargs)
        with open('info_not_param.log', 'a', encoding='UTF-8') as f:
            f.write('----------' + '\n')
            f.write('дата и время:' + ' ' +  str(time) + '\n')
            f.write('название функции:' + ' ' +  '"' + general.__name__+  '"' + '\n')
            f.write('аргументы:' + ' ' +  str(args[0])  + '\n')
            f.write('возвращаемое значение:' + ' ' + str(rezult) + '\n')

        return rezult

    return new_func



def decorator_param(path='qqq.log'):
    print('1')
    def decorator_func(general):
        print('2')
        def new_func(*args, **kwargs):
            print('3')
            time = datetime.now().replace(microsecond=0)
            rezult = general(*args, **kwargs)
            with open(path, 'a', encoding='UTF-8') as f:
                f.write('----------' + '\n')
                f.write('дата и время:' + ' ' +  str(time) + '\n')
                f.write('название функции:' + ' ' +  '"' + general.__name__+  '"' + '\n')
                f.write('аргументы:' + ' ' +  str(args[0])  + '\n')
                f.write('возвращаемое значение:' + ' ' + str(rezult) + '\n')
            print('3')
            return rezult

        return new_func

    return decorator_func