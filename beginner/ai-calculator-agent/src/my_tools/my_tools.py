from agents import function_tool

@function_tool
def Plus(n1:int, n2:int) -> dict:
    """
    Simple plus function that returns the sum of two numbers
    
    Args:
    n1: int
    n2: int
    """
    print("Plus tool fire --->")
    return {
    "operation": "add",
    "inputs": {"n1": n1, "n2": n2},
    "result": n1 + n2
}
@function_tool
def Multiply(n1:int, n2:int) -> dict:
    """
    Simple multiply function that returns the product of two numbers
    
    Args:
    n1: int
    n2: int
    """
    print("Multiply tool fire --->")
    return {
    "operation": "multiply",
    "inputs": {"n1": n1, "n2": n2},
    "result": n1 * n2
}

@function_tool
def Divide(n1:int, n2:int) -> dict:
    """
    Simple divide function that returns the remainder of two numbers
    
    Args:
    n1: int
    n2: int
    """
    print("Divide tool fire --->")
    return {
    "operation": "divide",
    "inputs": {"n1": n1, "n2": n2},
    "result": n1 / n2
}

@function_tool
def Subtract(n1:int, n2:int) -> dict:
    """
    Simple subtraction function that returns the difference of two numbers
    
    Args:
    n1: int
    n2: int
    """
    print("Subtract tool fire --->")
    return {
    "operation": "subtract",
    "inputs": {"n1": n1, "n2": n2},
    "result": n1 - n2
}
