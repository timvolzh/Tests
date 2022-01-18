import requests


def _yandex_upload(dir_name, ya_token):
    headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(ya_token)}
    make_dir_url = 'https://cloud-api.yandex.net/v1/disk/resources'

    try:
        md = requests.put(url=make_dir_url, headers=headers, params={'path': dir_name})
    except requests.exceptions.HTTPError:
        status = requests.exceptions.HTTPError()
        return status
    md.raise_for_status()
    return md.status_code


if __name__ == '__main__':
    ya_token = 'AQAAAAARW52bAADLW98a2e_BsUIks-NiKEQLs8U'
    dir_name = 'Photo_backup2'
    print(_yandex_upload(dir_name, ya_token))