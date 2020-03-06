import click
import json

__author__ = "Felipe Amaral"

filename = "events.json"


@click.group()
def list():
    pass


@list.command()
def users():
    """An operation to list all the users that have
       received at least one exam score"""
    users = set()
    with open(filename) as f:
        for line in f:
            loaded = json.loads(line)
            users.add(loaded['studentId'])
        print('\n'.join(users))


@list.command()
@click.option('--id', help="Will search by student ID")
def exams(id):
    """An operation to list all the exams"""
    with open(filename) as f:
        exams = set()
        for line in f:
            loaded = json.loads(line)
            if id:
                if loaded['studentId'] == id:
                    exams.add(loaded['exam'])
            else:
                exams.add(loaded['exam'])
        print(exams)


@list.command()
@click.option('--exam', help="Will search by exam", required=True, type=int)
def results(exam):
    """An operation to list all the results for a specified exam"""
    with open(filename) as f:
        for line in f:
            loaded = json.loads(line)
            if loaded['exam'] == exam:
                print(loaded['score'])


cli = click.CommandCollection(sources=[list])

if __name__ == '__main__':
    cli()
