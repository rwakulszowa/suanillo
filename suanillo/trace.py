from . import id
from .log import Print

def base(log):
    def trace(fun):
        def inner(*args, **kwargs):
            log_ = log.with_id(id.make())
            log_.input((args, kwargs))
            try:
                ans = fun(*args, **kwargs)
                log_.output(ans)
                return ans
            except Exception as e:
                log_.error(e)
                raise e
        return inner
    return trace

simple = base(Print())