import prometheus_client as prom
import requests
import warnings
warnings.filterwarnings("ignore")

RESPONSE_TIME = prom.Gauge('external_url_response_ms', 'Url response time in ms', ["url"])
STATUS_CODE = prom.Gauge('external_url_status', 'Url status', ["url"])
url_list = ["https://httpstat.us/503", "https://httpstat.us/200"]
url_statuscode = []

def get_url_status(url: str) -> dict:
    r = requests.get(url, verify=False, timeout=5)
    status = r.status_code
    print(f'url_up {url} : {1 if status==200 else 0}')
    return 1 if status==200 else 0

def get_response_time(url: str) -> dict:
    r = requests.get(url, verify=False, timeout=5)
    response_time = r.elapsed.total_seconds()
    print(f'Response_time {url} : {response_time}')
    return response_time

#this function displays the results properly on the web page
def get_url_metrics():
    while True:
        for url in url_list:
            url_status = get_url_status(url)
            STATUS_CODE.labels(url=url).set(url_status)
            response_time = get_response_time(url)
            RESPONSE_TIME.labels(url=url).set(response_time)

if __name__ == '__main__':
    prom.start_http_server(8000)
    get_url_metrics()
