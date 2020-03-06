import json
import sseclient
import signal
import requests

__author__ = "Felipe Amaral"

filename = 'events.json'
url = 'http://live-test-scores.herokuapp.com/scores'


class StreamEvent:
    def get_events(self, killer):
        response = requests.get(url, stream=True)
        client = sseclient.SSEClient(response)

        events = open(filename, 'a+')

        for event in client.events():
            if killer.kill_now:
                events.close()
                break
            print(json.loads(event.data))
            json.dump(json.loads(event.data), events)
            events.write('\n')


class GracefulKiller:
    kill_now = False

    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, signum, frame):
        self.kill_now = True


if __name__ == '__main__':
    killer = GracefulKiller()
    stream = StreamEvent()
    stream.get_events(killer)

    print("Events saved on file " + filename)
