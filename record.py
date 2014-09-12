import cherrypy

class Record(object):
    @cherrypy.expose
    def index(self):
        return "Start recording."

