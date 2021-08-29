import pprint
import urllib.request
import json

URL = "https://github.com/ephios-dev/ephios-qualification-fixtures/raw/main/de/_all.json"


def test_download_from_github():
    with urllib.request.urlopen(URL) as url:
        data = json.loads(url.read().decode())
        pprint.pprint(data, width=160)


if __name__ == "__main__":
    test_download_from_github()
