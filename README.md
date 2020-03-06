## Coding test

At `http://live-test-scores.herokuapp.com/scores` you'll find a service that follows the [Server-Sent Events](https://www.w3.org/TR/2015/REC-eventsource-20150203/) protocol. You can connect to the service using cURL:

        curl http://live-test-scores.herokuapp.com/scores

Periodically, you'll receive a JSON payload that represents a student's test score (a JavaScript number between 0 and 1), the exam number, and a student ID that uniquely identifies a student. For example:

        event: score
        data: {"exam": 3, "studentId": "foo", score: .991}

### Requirements

`python 3`

`sseclient-py==1.7`  - you can install running `pip3 install -r requirements.tx`

make sure you run give permission to execute the scripts with
```
chmod +x events.py
chmod +x scoresctl.py
```

### Get Events

`./events.py`

This script will fetch the events from `http://live-test-scores.herokuapp.com/scores`
and persist into a file called events.json. It will also send the events to `stdout`.

In order to stop the script just press `CTRL + C`. It may take a few seconds but it will stop it gracefully.

### Query Events

`./scoresctl.py`

This script implements a python click CLI where we can query data from the events.json file.

#### Commands

`exams`                List all the exams recorded 

`exams --id <ID>`      List all the exams recorded by student ID

`results --exam 11551` List all the results for a specified exam

`users`                List all the users that have received at least one exam score

Example:

`./scoresctl.py exams`

`./scoresctl.py exams --id Cielo68`

`./scoresctl.py results --exam 11551`

`./scoresctl.py users`