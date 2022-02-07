class Triple:
    # 三例模式
    def __new__(cls, *args, **kargs):
        if not hasattr(cls, '_instances'):
            cls._instances = []
        if len(cls._instances) < 3:
            instance = super().__new__(cls)
            cls._instances.append(instance)
            print("创建一个实例。")
        return cls._instances[-1]
        
    @classmethod
    def get_instance(cls, id):
        return cls._instances[id] 

    