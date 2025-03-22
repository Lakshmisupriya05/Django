import cherrypy 
cherrypy.config.update({ 
    'server.socket_host': '127.0.0.1', 
    'server.socket_port': 8081
}) 
class MyApp: 
    @cherrypy.expose 
    def index(self): 
        return("This is a plain text response!") 
    @cherrypy.expose 
    def priya_html(self): 
        return open('priya.html').read() 
    @cherrypy.expose 
    def html(self): 
        return""" 
        <html> 
            <head> 
                <title>CherryPy HTML Page.</title> 
            </head> 
            <body> 
                <h1>Never Underestimate yourself </h1> 
                <p>by Swami vivekananda</p> 
            </body> 
        </html> 
        """  
if __name__ == '__main__': 
    cherrypy.quickstart(MyApp())