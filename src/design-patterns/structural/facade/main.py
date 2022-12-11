"""
We’re building a social media management tool.
On a few screens, we need to display the recent tweets of a given user.
Look at the code in facade/Demo.
This class shows the steps required to talk to the Twitter API.
We need to get a request token first.
We’ll then exchange the request token with an access token.
To get the recent tweets, we need to send the access token to Twitter API.
We have to repeat similar steps for other operations such as composing a new tweet, liking a tweet, etc.
What are the problems with the current implementation?
Use the facade pattern to solve these problems.
"""


from time import sleep
from uuid import uuid1


class Connection:
    def __init__(self, id: str, ip_address: str) -> None:
        self.id = id
        self.ip_address = ip_address

    def disconnect(self):
        print(
            f"[LOG] Connection {self.id} disconnected from {self.ip_address}.")


class Message:
    def __init__(self, msg: str) -> None:
        self.payload = msg


class NotificationServer:
    def connect(self, ip_address: str) -> Connection:
        print(f"[LOG] Connecting to '{ip_address}'...")
        sleep(1)
        conn = Connection(uuid1(), ip_address)
        print(f"[LOG] Connection '{conn.id}' established.")
        return conn

    def authenticate(self, appID: str, key: str):
        print(
            f"[LOG] Authenticating app ID '{appID}' with key '{key}'...")
        sleep(1)
        return uuid1()

    def send(self, auth_token: str, message: Message, target: str):
        print(
            f"[LOG] Sending '{message.payload}' with token '{auth_token}' to '{target}'...")
        sleep(1)


class NotificationService:
    def __init__(self) -> None:
        ...

    def send(self, message: str, target: str):
        server = NotificationServer()
        conn = server.connect("24.256.32.26")
        auth_token = server.authenticate(uuid1(), uuid1())
        msg = Message(message)
        server.send(auth_token, msg, target)
        conn.disconnect()


if __name__ == "__main__":
    svc = NotificationService()
    svc.send("Hello there!", f"device-{uuid1()}")
