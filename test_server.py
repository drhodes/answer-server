import requests
import os

def test_get_answers():
    secret = os.environ["GRADER_SECRET"]
    consumer = os.environ["GRADER_CONSUMER"]
    
    url = 'https://www.mathtech.org:5001/get-answers'
    req = requests.Request(url=url,
                           method="POST",
                           data={
                               "edx-anon-id":"jupyter-35dd7e9124c8847ec5-030ef",
                               "labname":"SimpleLab1",
                           },                           
                           auth=(consumer, secret))
    sess = requests.Session()
    rsp = sess.send(req.prepare())
    print(rsp.text)


def test_submit_answers():
    secret = os.environ["GRADER_SECRET"]
    consumer = os.environ["GRADER_CONSUMER"]
    
    url = 'https://www.mathtech.org:5001/submit-answers'
    req = requests.Request(url=url,
                           method="POST",
                           data={
                               "edx-anon-id":"jupyter-35dd7e9124c8847ec5-030ef",
                               "labname":"SimpleLab1",
                               "lab-answers":'{"q1": 2, "q2": 5}',
                           },                           
                           auth=(consumer, secret))
    sess = requests.Session()
    rsp = sess.send(req.prepare())
    print(rsp.text)
    
    
if __name__ == "__main__":
    test_submit_answers()
    test_get_answers()
