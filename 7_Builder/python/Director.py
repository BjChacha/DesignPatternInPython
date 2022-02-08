from Builder import Builder

class Director:
    
    def __init__(self, builder: Builder):
        self._builder = builder
    
    def construct(self) -> None:
        builder = self._builder
        builder.make_title("Greeting")
        builder.make_string("从早上到下午")
        builder.make_items([
            "早上好。",
            "晚上好。"
        ])
        builder.make_string("晚上")
        builder.make_items([
            "晚上好。",
            "晚安。",
            "再见。"
        ])
        builder.close()