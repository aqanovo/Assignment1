def typeBasedTransformer(**kwargs):
    transformed_kwargs = {}
    
    for key, value in kwargs.items():
        if isinstance(value, (int, float)):  # Check if the value is an integer or float
            transformed_kwargs[key] = value ** 2  # Square the number
        elif isinstance(value, str):  # Check if the value is a string
            transformed_kwargs[key] = value[::-1]  # Reverse the string
        elif isinstance(value, bool):  # Check if the value is a boolean
            transformed_kwargs[key] = not value  # Invert the boolean
        elif isinstance(value, (list, tuple)):  # Check if the value is a list or tuple
            transformed_kwargs[key] = value[::-1]  # Reverse the order of elements
        elif isinstance(value, dict):  # Check if the value is a dictionary
            transformed_kwargs[key] = {v: k for k, v in value.items()}  # Swap keys and values
        else:  # For unsupported types, leave the value unchanged
            transformed_kwargs[key] = value
    
    return transformed_kwargs

# Example usage:
result = typeBasedTransformer(
    num=4,
    pi=2.5,
    text="Hello",
    flag=True,
    items=[1, 2, 3],
    mapping={"a": 1, "b": 2},
    unsupported=complex(1, 1)  # Unsupported type
)

print(result)
