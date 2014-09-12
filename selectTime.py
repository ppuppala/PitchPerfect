import cherrypy

class SelectTime(object):
    @cherrypy.expose
    def index(self):
        return "Select a time: "

