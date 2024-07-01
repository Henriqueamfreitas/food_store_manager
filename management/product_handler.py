from menu import products


def get_product_by_id(product_id):
    if not isinstance(product_id, int):
        raise TypeError("product id must be an int")
    for product in products:
        if (product["_id"] == product_id):
            return product
    return {}


def get_products_by_type(product_type):
    if not isinstance(product_type, str):
        raise TypeError("product type must be a str")
    product_type_list = []
    for product in products:
        if (product["type"] == product_type):
            product_type_list.append(product)
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


def menu_report():
    product_count = len(products)

    unique_types = []
    all_product_types = []
    total_price = 0
    for product in products:
        total_price += product["price"]
        all_product_types.append(product["type"])
        if product["type"] not in unique_types:
            unique_types.append(product["type"])

    average_price = round(total_price / product_count, 2)

    most_common_type_count = 0
    most_common_type = ""
    for product_type in unique_types:
        type_count = all_product_types.count(product_type)
        if type_count > most_common_type_count:
            most_common_type = product_type
            most_common_type_count = type_count

    return f"Products Count: {product_count} - Average Price: ${average_price} - Most Common Type: {most_common_type}"
