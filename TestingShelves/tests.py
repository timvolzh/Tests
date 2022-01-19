import unittest
import app
# from unittest.mock import patch
import test_data


class TestUnitAppDocuments(unittest.TestCase):

    def test_get_all_doc_owners_names(self): # Тест получения всех владельцев
        self.assertEqual({'Аристарх Павлов', 'Василий Гупкин', 'Геннадий Покемонов', test_data.new_doc_owner_name},
                         app.get_all_doc_owners_names(),
                         'Списки не совпадают')

    def test_get_doc_owner_name(self):# Тест получения имени владельца по номеру документа
        self.assertEqual('Аристарх Павлов', app.get_doc_owner_name(test_data.doc_number), 'Не найден')

    def test_remove_doc_from_shelf(self): # Тест удаления документа
        self.assertEqual(app.delete_doc(test_data.doc_number), (test_data.doc_number, True), 'Документ не удален')

    def test_add_new_doc(self): # Тест добавления документа
        self.assertEqual(app.add_new_doc(test_data.new_doc_type, test_data.new_doc_number,
                                         test_data.new_doc_owner_name, test_data.new_doc_shelf_number),
                         test_data.new_doc_shelf_number, 'Документ не создан')


if __name__ == '__main__':
    unittest.main()
