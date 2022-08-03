create file fwsgi.py
'''
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'Hello world from a simple WSGI application!']
'''

sudo add-apt-repository universe
sudo apt update
sudo apt install python-pip

pip install uwsgi

uwsgi --http :8000 --wsgi-file fwsgi.py

run http://127.0.0.1:8000/