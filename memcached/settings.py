# coding:utf-8
# author: Articuly
# datetime: 2020/6/18 17:56
# software: PyCharm

class BaseConfig:
    PYMEMCACHE = {
        'server': ('127.0.0.1', 11211),
        'connect_timeout': 1.0,
        'timeout': 0.5,
        'no_delay': True,
        'key_prefix': b'myapp-',
    }


class DevelopmentConfig(BaseConfig):
    pass


config = {
    'development': DevelopmentConfig,

}
