import cherrypy
import selectTime
import record

if __name__ == '__main__':
	cherrypy.config.update(
		{ 
			'server.socket_host': '192.168.1.101', 
			'server.socket_port': 80,
		}
	)

	record_config = {'/record':
		{
			'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
     	   	'tools.trailing_slash.on': False,
		}
	}
    
	cherrypy.tree.mount(selectTime.SelectTime())
	cherrypy.tree.mount(record.Record(), "/record", config=record_config)

	cherrypy.engine.start()
	cherrypy.engine.block()