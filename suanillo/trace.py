def simple(fun):
    def inner(*args, **kwargs):
        print("> {}, {}".format(args, kwargs))
        try:
            ans = fun(*args, **kwargs)
            print("< {}".format(ans))
            return ans
        except Exception as e:
            print("<! {}".format(e))
            raise e
    return inner