from TestingYandex.Yandex import yandex_md, yandex_dd


ya_token = 'AQAAAAARW52bAADLW98a2e_BsUIks-NiKEQLs8U'
wrong_ya_token = 'AQAAAAARW52bAADLW98a2e_BsUIks-NiKEQLser'
dir_name = 'TestAPI'

class TestYandexPytest:

    def test_yandex_md_success(self): # Тест упешного создания папки
        assert yandex_md(dir_name, ya_token) == 201

    def test_yandex_md_already_exist(self): # Тест добавления уже существующей папки
        assert yandex_md(dir_name, ya_token) == 409

    def test_yandex_download_success(self): # Тест ошибки авторизации
        assert yandex_md(dir_name, wrong_ya_token) == 401

    @classmethod
    def teardown_class(cls): # Удаляем тестовую папку после завершения тестов
        result = yandex_dd(dir_name, ya_token)
        if result.status_code == 202:
            return print('Папка удалена')



print(yandex_md(dir_name, ya_token))