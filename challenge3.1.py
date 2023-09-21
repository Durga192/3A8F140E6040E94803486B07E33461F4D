
def linear_search_product(products, target):
    indices = []
    for i in range(len(products)):
        if products[i] == target:
            indices.append(i)
    return indices
products = ["apple", "banana", "orange", "banana", "pear"]
target = "banana"
result = linear_search_product(products, target)
print(result) 

target = "grape"
result = linear_search_product(products, target)
print(result)