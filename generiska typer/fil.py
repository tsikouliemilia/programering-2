from typing import Generic, TypeVar

T = TypeVar("T")

class Box(Generic[T]):

    def __init__(self,value:T)-> None:
        self.value: T = value
    def get_value(self) -> T:
        return self.value
    
int_box = Box[int](10)
str_box = Box[str]("Hej")

num = int_box.get_value()
text = str_box.get_value()

print(num)
print(text)