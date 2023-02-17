import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json', 'r', encoding='utf-8') as json_f:
        data = json.load(json_f)

    data['orders'].append({'item': item, 'quantity': quantity, 'price': price,
                           'buyer': buyer, 'date': date})

    with open('orders.json', 'w', encoding='utf-8') as json_f:
        json.dump(data, json_f, ensure_ascii=False, indent=4)


write_order_to_json(input('Введите название товара: '),
                    input('Введите количество: '),
                    input('Введите цену: '),
                    input('Введите покупателя: '),
                    input('Введите дату: '))
