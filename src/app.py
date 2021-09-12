import falcon
from constants import ENV_VARS

from sqlalchemy             import create_engine
from sqlalchemy.orm         import sessionmaker

from middleware.session_manager import SessionManager

from resources.healthcheck      import HealthcheckResource
from resources.authentication   import AuthenticationResource

engine = create_engine((f"postgresql://{ENV_VARS['DB_USERNAME']}:{ENV_VARS['DB_PASSWORD']}@{ENV_VARS['DB_HOSTNAME']}:{ENV_VARS['DB_PORT']}/{ENV_VARS['DB_NAME']}"), 
    echo=False, pool_size=5, max_overflow=2, pool_pre_ping=True)

session_maker = sessionmaker(bind=engine)

api = falcon.API(middleware=[
                                SessionManager(session_maker)
                            ])

api = falcon.App()

health_check_resource = HealthcheckResource()
api.add_route('/', health_check_resource)
api.add_route('/{place_holder}', health_check_resource)

authentication_resource = AuthenticationResource()
api.add_route('/authentication', authentication_resource)
# api.add_route('/login', authentication_resource, suffix="login")
