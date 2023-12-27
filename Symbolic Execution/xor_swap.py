# Swapping two values using XOR
from typing import Any 

class Expr:
    def __init__(self, s: str) -> None:
        self.s = s

    def __str__(self) -> str:
        return self.s
    
    def __xor__(self, other: Any) -> str:
        return Expr("(" + self.s + "^" + other.s + ")")
    
def XOR_swap(X: Expr, Y: Expr) -> Any:
    X = X ^ Y
    Y = Y ^ X
    X = X ^ Y
    return X, Y

if __name__ == "__main__":
    new_X, new_Y = XOR_swap(Expr("X"), Expr("Y"))
    print("new_X : ", new_X)
    print("new_Y : ", new_Y)