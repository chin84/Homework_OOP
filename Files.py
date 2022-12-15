from pprint import pprint
import file_options


class CookHelper:
    def __init__(self):
        with open('recipes.txt', encoding='utf-8') as f:
            self.cook_book = {}
            for line in f:
                dish = line.strip()
                num = int(f.readline())
                i = 0
                ingr = []
                while i < num:
                    i += 1
                    ingr_str = f.readline().strip()
                    row = {
                        'ingredient_name': ingr_str[0: ingr_str.find(' | ')],
                        'quantity': int(ingr_str[ingr_str.find(' | ') + 3: ingr_str.rfind(' | ')]),
                        'measure': ingr_str[ingr_str.rfind(' | ') + 3:]
                    }
                    ingr.append(row)
                self.cook_book[dish] = ingr
                f.readline()

    def cook_book_view(self):
        pprint(self.cook_book)

    def get_shop_list_by_dishes(self, dishes, person_count):
        shop_list = {}
        for dish in dishes:
            if dish in self.cook_book:
                for row in self.cook_book[dish]:
                    if shop_list.get('ingredient_name') is None:
                        shop_list[row['ingredient_name']] = {'measure': row['measure'],
                                                             'quantity': row['quantity'] * person_count}
                    else:
                        shop_list['ingredient_name']['quantity'] += row['quantity'] * person_count
            else:
                print(f"Рецепт {dish} в вашей книге рецептов не обнаружен")
        return shop_list


if __name__ == '__main__':
    cook_session = CookHelper()
    sl = cook_session.get_shop_list_by_dishes(['Омлет', 'Фахитос', 'Омлет'], 2)
    pprint(sl)
    file_options.txt_file_steaching()


