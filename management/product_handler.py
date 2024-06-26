from menu import products


def get_product_by_id(product_id):
    for element in products:
        if (element["_id"] == product_id):
            return element
    return {}


def get_products_by_type(product_type):
    product_type_list = []
    for element in products:
        if (element["type"] == product_type):
            product_type_list.append(element)
    return product_type_list
