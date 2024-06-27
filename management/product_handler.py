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


def add_product(menu, **kwargs):
    highest_id = 0
    if len(menu) == 0:
        kwargs["_id"] = 1
    else:
        for product in menu:
            if product["_id"] > highest_id:
                highest_id = product["_id"]
        kwargs["_id"] = highest_id + 1

    menu.append(kwargs)

    return kwargs
