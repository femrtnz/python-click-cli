## Coding test

At `http://live-test-scores.herokuapp.com/scores` you'll find a service that follows the [Server-Sent Events](https://www.w3.org/TR/2015/REC-eventsource-20150203/) protocol. You can connect to the service using cURL:

        curl http://live-test-scores.herokuapp.com/scores

Periodically, you'll receive a JSON payload that represents a student's test score (a JavaScript number between 0 and 1), the exam number, and a student ID that uniquely identifies a student. For example:

        event: score
        data: {"exam": 3, "studentId": "foo", score: .991}

This represents that student foo received a score of `.991` on exam #3. 

Your job is to build a script that continuously consumes this data, processes it, and persists it to disk. Additionally, you will need to write another script for querying the persisted data.

You may write this script in Python or bash/sh. You may also use any open-source libraries/tools or resources that you find helpful. **As part of the exercise, please replace this README file with instructions for building and running your project.** We will run your code as part of our review process.

Here are the operations we want your query script to support:

1. An operation to list all the users that have received at least one exam score.
2. An operation to list all the exam results for a specified student ID.
3. An operation to list all the exams that have been recorded.
4. An operation to list all the results for a specified exam.

Coding tests are often contrived, and this exercise is no exception. To the best of your ability, make your solution reflect the kind of code you'd want to run on production systems. A few things we're specifically looking for:

* Well-structured, well-written, idiomatic, safe, performant code. 
* Ecosystem understanding. Your code should demonstrate that you understand whatever ecosystem you're coding against – including project organization and use of third-party libraries/tools.
* Thoughtful intention behind the command-line interface and command output.

That's it. Commit your solution to the provided GitHub repository (this one). When you come in, we'll pair with you and walk through your solution and extend it in an interesting way.
