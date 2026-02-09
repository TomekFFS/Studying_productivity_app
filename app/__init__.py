from flask import Flask

def create_app():
    app= Flask(__name__)

    #PLUG IN: tasks feature
    from app.routes.tasks import bp as tasks_bp
    app.register_blueprint(tasks_bp)
    
    #Place for further scaling (adding new features like a calendar or a timer etc)

    @app.route("/")
    def home():
        return "Twój serwer działa<p>kieruj się do <a href='/tasks/'>/tasks</a> aby zobaczyć swoje zadania do wykonania</p>"
    
    return app