from menu import products
from management.product_handler import (
    get_product_by_id,
    get_products_by_type,
    add_product,
    menu_report,
    add_product_extra
)
from management.tab_handler import calculate_tab

if __name__ == "__main__":
    # TAREFA 1
    print(get_product_by_id(3))
    print(get_products_by_type("fruit"))

    # TAREFA 2
    new_product = {
        "title": "X-Python",
        "price": 5.0,
        "rating": 5,
        "description": "Sanduiche de Python",
        "type": "fast-food"
    }
    print(add_product(products, **new_product))

    table_1 = [{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}]
    table_2 = [
        {"_id": 10, "amount": 3},
        {"_id": 20, "amount": 2},
        {"_id": 21, "amount": 5},
    ]

    print(calculate_tab(table_1))
    print(calculate_tab(table_2))
    # output
    # {'subtotal': '$216.1'}
    # {'subtotal': '$188.29'}

    # TAREFA 3
    try:
        print(get_product_by_id("3000000000000000000"))
    except TypeError as e:
        print(str(e))

    try:
        print(get_products_by_type(3))
    except TypeError as e:
        print(str(e))
    print(menu_report())

    # TAREFA EXTRA
    required_keys = ("description", "price", "rating", "title", "type")
    # Produto com chaves obrigatórias faltando
    new_product_2 = {
        "title": "X-Python",
        "price": 5.0,
        "rating": 5,
        # "description": "Sanduiche de Python",
        "type": "fast-food",
        "extra_key_1": "extra_value_1",
        "extra_key_2": "extra_value_2"
    }
    # Produto com chaves extras
    new_product = {
        "title": "X-Python",
        "price": 5.0,
        "rating": 5,
        "description": "Sanduiche de Python",
        "type": "fast-food",
        "extra_key_1": "extra_value_1",
        "extra_key_2": "extra_value_2"
    }
    # ERROR
    try:
        print(add_product_extra(products, *required_keys, **new_product_2))
    except KeyError as e:
        print(str(e))
    # CERTO
    try:
        print(add_product_extra(products, *required_keys, **new_product))
    except KeyError as e:
        print(str(e))
