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
    path = os.path.join(cwd, "paper") # Path to dl file

    app = Application([
        (r'/', GraphView),
        # Static files, repeat for other file names
        (r'/(.*\.js)', StaticFileHandler, {"path": cwd} ),
        (r'/download/(barojas_v193\.pdf)', StaticFileHandler, {'path': path} ), # Static serving file
    ])
    http_server = HTTPServer(app)
    http_server.listen(port)
    print('RI5C is listening on port:%i' % port)
    IOLoop.current().start()

if __name__ == "__main__":
    main() 
