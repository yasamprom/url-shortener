from locust import HttpUser, task, between
import json

class WebsiteTestUser(HttpUser):
    wait_time = between(0.5, 3.0)

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.client.post('/shorten',
                        json.dumps({"main_url": "http://google.com",
                        "alias": "",
                        "expires_at":  "2025-03-30T21:01:08.088737"}),
                        headers={'accept': 'application/json', 'Content-Type': 'application/json'}
                        )
        pass

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        pass

    @task(1)
    def shorten(self):
        self.client.post('/shorten',
                        json.dumps({"main_url": "http://ozon.ru",
                        "alias": "",
                        "expires_at":  "2025-03-30T21:01:08.088737"}),
                        headers={'accept': 'application/json', 'Content-Type': 'application/json'}
                        )
    
    @task(2)
    def search(self):
        self.client.get('/search/http%3A%2F%2Fgoogle.com')