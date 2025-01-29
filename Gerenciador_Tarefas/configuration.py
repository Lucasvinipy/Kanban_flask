from routes.home import home_route
from routes.user import user_route
from database.tarefa import db

def configure_all(app):
    configure_db(app)  # Configura o banco de dados
    configure_routes(app)  # Configura as rotas

def configure_routes(app):
    app.register_blueprint(home_route)
    app.register_blueprint(user_route, url_prefix='/user')

def configure_db(app):
    # Configuração do banco de dados
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345678@localhost/kanban'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializa o SQLAlchemy com o app
    db.init_app(app)

    # Cria as tabelas no banco de dados (se não existirem)
    with app.app_context():
        db.create_all()