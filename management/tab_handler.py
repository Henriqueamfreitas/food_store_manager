from menu import products


def calculate_tab(dict_list):
    total = 0
    for consumed_item in dict_list:
        for product in products:
            if (product["_id"] == consumed_item["_id"]):
                total += product["price"] * consumed_item["amount"]

    rounded_total = round(total, 2)
    return {"subtotal": f"${rounded_total}"}
