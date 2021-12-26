import requests
import os

def test_get_notebook():
    secret = os.environ["GRADER_SECRET"]
    consumer = os.environ["GRADER_CONSUMER"]
    
    url = 'https://www.mathtech.org:5001'
    req = requests.Request(url=url,
                           method="POST",
                           data={
                               "userid":"35dd7e9124c8847ec5-030ef",
                               "labname":"SimpleLab1",
                           },                           
                           auth=(consumer, secret))
    sess = requests.Session()
    rsp = sess.send(req.prepare())
    print(rsp.text)
    
    
if __name__ == "__main__":
    test_get_notebook()
