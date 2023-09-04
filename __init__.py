import requests
import threading


def url_searching(url_pool: list):
    threads = []

    def get_url(url_single):
        response_list = []
        response = requests.get(url=url_single)
        response_list.append(response)
    for url in url_pool:
        threads.append(
            threading.Thread(
                target=get_url, args=(url,)
            )
        )
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    urls = [
        f'www.buff/goods/{index}.com'
        for index in range(36000, 37000)
    ]
    url_searching(url_pool=urls)
