from app.main import create_app
from app.main.controllers import api


app = create_app()
app.app_context().push()
api.init_app(app)

if __name__ == "__main__":
    # app.run()
    app.run(host='0.0.0.0', port=5000)