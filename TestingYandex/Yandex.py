import requests


def yandex_md(dir_name, ya_token):
    headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(ya_token)}
    make_dir_url = 'https://cloud-api.yandex.net/v1/disk/resources'
    result = requests.put(url=make_dir_url, headers=headers, params={'path': dir_name})
    return result.status_code


def yandex_dd(dir_name, ya_token):
    headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(ya_token)}
    make_dir_url = 'https://cloud-api.yandex.net/v1/disk/resources'
    result = requests.delete(url=make_dir_url, headers=headers, params={'path': dir_name})
    return result.status_code

if __name__ == '__main__':
    ya_token = 'AQAAAAARW52bAADLW98a2e_BsUIks-NiKEQLs8U'
    dir_name = 'Photo_backup2'
    print(yandex_md(dir_name, ya_token))