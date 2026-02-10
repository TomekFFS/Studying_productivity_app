from flask import Flask, redirect, url_for

def create_app():
    app= Flask(__name__)

    #PLUG IN: tasks feature
    from app.routes.hub import bp as hub_bp
    app.register_blueprint(hub_bp)
    
    #Place for further scaling (adding new features like a calendar or a timer etc)

    @app.route("/")
    def home():
        return redirect(url_for('hub.list_tasks')) #redirecting to the tasks page
    
    return app