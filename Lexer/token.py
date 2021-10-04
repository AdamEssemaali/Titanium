class Token:
    def __init__(self,ztype,value,index,line) -> None:
        self.type = ztype
        self.value = value
        self.index = index
        self.line = line