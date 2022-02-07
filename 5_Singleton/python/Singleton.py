class Singleton:

    @classmethod
    def get_instance(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = cls.__new__(cls)
            print("生成了一个实例。")
        return cls._instance


class Singleton2:
    # another implement
    def __new__(cls, *args, **kargs):
        if not hasattr(cls, "_instance"):
            # 这里用super()不能用cls，否则会报错：maximum recursion
            cls._instance = super().__new__(cls)
            print("生成了一个实例。")
        return cls._instance