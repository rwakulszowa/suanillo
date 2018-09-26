from .log import Print

def base(log):
    def trace(fun):
        def inner(*args, **kwargs):
            log.input((args, kwargs))
            try:
                ans = fun(*args, **kwargs)
                log.output(ans)
                return ans
            except Exception as e:
                log.error(e)
                raise e
        return inner
    return trace

simple = base(Print())