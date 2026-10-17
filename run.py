
from livereload import Server
from app import app

server = Server(app.wsgi_app)

server.watch("templates/*.html")
server.watch("static/*.css")
server.watch("static/*.js")

server.serve(
    host="127.0.0.1",
    port=5000,
    debug=True
)
