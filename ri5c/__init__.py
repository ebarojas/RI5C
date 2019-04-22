# __init__.py
'''
Settings for Tornado app go here
'''

from tornado.httpserver import HTTPServer
from tornado.options import define, options
from tornado.web import Application
from tornado.ioloop import IOLoop
from ri5c.views import HelloWorld

define('port', default=8000, help='port to listen on')

def main():
    """Construct and serve the tornado application."""
    app = Application([
        ('/', HelloWorld)
    ])
    http_server = HTTPServer(app)
    http_server.listen(options.port)
    print('RI5C is listening on http://localhost:%i' % options.port)
    IOLoop.current().start()

main() # This might need to be removed
