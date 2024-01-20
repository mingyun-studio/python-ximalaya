from ximalaya.client import XimalayaClient


def test_ximalaya_client():
    client1 = XimalayaClient()

    assert client1.host == 'www.ximalaya.com'
    assert client1.headers == {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,en-US;q=0.7,en;q=0.3',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }

    client2 = XimalayaClient('www.example.com', {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0',
        'Accept-Language': 'zh-CN,en-US;q=0.7,en;q=0.3',
        'Referer': 'https://www.ximalaya.com/category/a3/',
    })

    assert client2.host == 'www.example.com'
    assert client2.headers == {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,en-US;q=0.7,en;q=0.3',
        'Referer': 'https://www.ximalaya.com/category/a3/',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }
