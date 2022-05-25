class Printable:
    def __init__(self) -> None:
        self.name = "Printable"
    
    def __repr__(self) -> str:
        return str(self.__dict__)