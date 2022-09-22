import unittest
from parameterized import parameterized
from unittest.mock import patch

import app


class TestBookkeeping(unittest.TestCase):

    # 1.  Тест функции get_doc_owner_name()
    # ap - (all people) - команда, которая выводит список всех владельцев документов

    # Версия_1
    #     def test_get_all_doc_owners_names(self):
    #         expected = {'Аристарх Павлов', 'Василий Гупкин', 'Геннадий Покемонов'}
    #         result = app.get_all_doc_owners_names()
    #         self.assertEqual(expected, result)

    # # Версия_2
    # def test_get_random_doc_owner(self):
    #     expected = 'Василий Гупкин'
    #     result = app.get_all_doc_owners_names()
    #     self.assertIn(expected, result)

    # #2. Тест функции get_doc_owner_name()
    # # p – (people) – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
    #
    #     @parameterized.expand(
    #         [
    #             ("10006", "Аристарх Павлов"),
    #             ("11-2", "Геннадий Покемонов"),
    #         ]
    #     )
    #     @patch('builtins.input')
    #     def test_get_doc_owner_name(self, doc, name, inp):
    #         inp.return_value = doc
    #         self.assertEqual(app.get_doc_owner_name(), name)

    # 3. Тест функции show_all_docs_info()
    # l – (list) – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
    # Поскольку show_all_docs_info это переборщик show_document_info и не имеет return,
    # тестируем show_document_info()

    # @parameterized.expand(
    #     [
    #         (app.documents[0], 'passport "2207 876234" "Василий Гупкин"'),
    #         (app.documents[1], 'invoice "11-2" "Геннадий Покемонов"'),
    #         (app.documents[2], 'insurance "10006" "Аристарх Павлов"'),
    #
    #     ]
    # )
    # def test_show_document_info(self, doc, expected):
    #     result = app.show_document_info(doc)
    #     self.assertEqual(result, expected)

    # #4. Тест функции get_doc_shelf()
    # # s – (shelf) – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
    #
    #     @parameterized.expand(
    #         [
    #             ("10006", "2"),
    #             ("11-2", "3"),
    #         ]
    #     )
    #     @patch('builtins.input')
    #     def test_get_doc_shelf(self, doc, shelf, inp):
    #         inp.return_value = doc
    #         self.assertEqual(app.get_doc_shelf(), shelf)

    # #5. Тест функции add_new_doc()
    # #     a – (add) – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип,
    # #     имя владельца и номер полки, на котором он будет храниться.
    #
        @parameterized.expand(
            [
                ("666", "licence", "Lucifer Morningstar", "666", "666"),
                ("999", "licence", "Mazikeen", "999", "666")
            ]
        )
        @patch('builtins.input')

        def test_add_new_doc(self, doc_number, doc_type, doc_owner, doc_shelf, shelf, inp):
            inp.return_value = doc_number
            inp.return_value = doc_type
            inp.return_value = doc_owner
            inp.return_value = doc_shelf
            self.assertEqual(app.add_new_doc(), shelf)

    # #6. Тест функции delete_doc()
    # #       d – (delete) – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
    #
    #     @parameterized.expand(
    #         [
    #             ("10006", ('10006', True)),
    #             ("2207 876234", ('10006', True))
    #         ]
    #     )
    #     @patch('builtins.input')
    #
    #     def test_add_new_doc(self, doc_number, expected, inp):
    #         inp.return_value = doc_number
    #         self.assertEqual(app.delete_doc(), expected)