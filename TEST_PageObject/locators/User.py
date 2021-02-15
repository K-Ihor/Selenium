class User:
    class right_menu:
        it = {'css': '#column-right'}  # если захочу искать еще как-то то положу сюда не css а еще и id.. пример(it = {'css': '#column-right', 'id': 'content'}
        wish_list = {'css': it['css'] + ' a:nth-child(5)'}

    class main_top_menu:
        it = {'css': 'ul.nav'}
        Components = {'css': it['css'] + ' li:nth - child(3)'}

    class payment_form:
        it = {'css': '#payment-new'}
