from flask import Flask , render_template 
from routes.home import home_route
from routes.user import user_route

app = Flask(__name__)


app.register_blueprint(home_route)
app.register_blueprint(user_route , url_prefix='/user')

   
app.run(debug=True)