import Yandex

ya_token = 'AQAAAAARW52bAADLW98a2e_BsUIks-NiKEQLs8U'
dir_name = 'Photo_backup2'

class TestYandexPytest:

     def test_yandex_download_success(self):
        assert Yandex._yandex_upload(dir_name, ya_token) == 201


print(Yandex._yandex_upload(dir_name, ya_token))