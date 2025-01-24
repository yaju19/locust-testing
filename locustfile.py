from locust import HttpUser, task, between, constant

class LoginUser(HttpUser):
    # wait_time = between(1, 5)  # Simulates users waiting between 1 and 5 seconds between tasks
    wait_time = constant(0) 

    @task
    def login(self):
        self.client.post("/login/", json={
          "email": " ",
          "password": "password",
          "tenant": "spice",
          "medium": "email",
          "device_info": {
              "screen_size": "1536 x 864",
              "logical_cores": 8,
              "os": "Windowsx64"
          }
        })



