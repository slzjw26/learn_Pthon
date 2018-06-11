import re


class route:

    mappings = {}

    def __init__(self, url, extra_kargs={}):
        self.url = url
        self.x_kargs = extra_kargs

    def __call__(self, func):
        route.mappings[self.url] = [func, self.x_kargs]
        return func

    @staticmethod
    def search(url):
        # 如果存在命名的参数，则忽略不命名的参数
        # 额外的参数总是传递，并且覆盖同名的命名参数
        for pat, (func, x_kargs) in route.mappings.items():
            match_obj = re.compile(pat).match(url)
            if match_obj:
                kargs = match_obj.groupdict()
                if kargs:
                    args = ()   # 忽略不命名的参数
                else:
                    args = match_obj.groups()
                kargs.update(x_kargs)
                return func, args, kargs
