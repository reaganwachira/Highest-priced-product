Problem Description: Find Highest Priced Product
You are given a list of dictionaries representing products and their prices. Your task is to write a Python function to find and return the product with the highest price.
Function Signature
def find_highest_priced_product(products: List[Dict[str, Union[str, int]]]) -> Dict[str, Union[str, int]]:
Parameters
products: A list of dictionaries, where each dictionary represents a product with keys "name" and "price".
Returns
A dictionary representing the product with the highest price.
Constraints
The input list products will have at least one dictionary.
The "price" values are positive integers.
The product names are unique.
This problem statement outlines the task to find the product with the highest price from a list of dictionaries, along with the function signature, parameters, return value, example usage, and constraints.
