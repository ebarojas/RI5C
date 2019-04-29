'''
Settings for Tornado app go here
'''
import os
from tornado.httpserver import HTTPServer
from tornado.options import define, options
from tornado.web import Application,StaticFileHandler
from tornado.ioloop import IOLoop
from ri5c.views import GraphView


define('port', default=8000, help='port to listen on')

def main():
    """Construct and serve the tornado application."""
    cwd = os.getcwd() # static files
    port = int(os.environ.get("PORT", 8000))

    app = Application([
        (r'/', GraphView),
        # Static files, repeat for other file names
        (r'/(.*\.js)', StaticFileHandler, {"path": cwd} ),
    ])
    http_server = HTTPServer(app)
    http_server.listen(port)
    print('RI5C is listening on http://localhost:%i' % port)
    IOLoop.current().start()

if __name__ == "__main__":
    main() 
