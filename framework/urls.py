from datetime import date
from views import *


# front controller
def secret_front(request):
    request['date'] = date.today()


def other_front(request):
    request['key'] = 'key'


fronts = [secret_front, other_front]

routes = {
    '/': Index(),
    '/index/': Index(),
    '/page/': Page(),
    '/contact/': Contact(),
    # '/examples/': Examples(),
    #
    # '/another_page/': Another_page(),
}
