from TestingYandex.Yandex import yandex_md, yandex_dd
from TestingYandex import test_data


class TestYandexPytest:

    def test_yandex_md_success(self): # Тест упешного создания папки
        assert yandex_md(test_data.dir_name, test_data.ya_token) == 201

    def test_yandex_md_already_exist(self): # Тест добавления уже существующей папки
        assert yandex_md(test_data.dir_name, test_data.ya_token) == 409

    def test_yandex_download_success(self): # Тест ошибки авторизации
        assert yandex_md(test_data.dir_name, test_data.wrong_ya_token) == 401

    @classmethod
    def teardown_class(cls): # Удаляем тестовую папку после завершения тестов
        result = yandex_dd(test_data.dir_name, test_data.ya_token)
        if result == 202:
            return print('Папка удалена')
