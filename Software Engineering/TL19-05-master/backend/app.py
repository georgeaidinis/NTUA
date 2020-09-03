from flask_restplus import Api

from modules.MapCode.rest_api import NAMESPACE as mapCode_ns
from modules.Users.rest_api import NAMESPACE as Users_ns
from modules.Resources.rest_api import NAMESPACE as Resources_ns
from modules.Admin.rest_api import NAMESPACE as Admin_ns
from modules.Healthcheck.rest_api import NAMESPACE as Healthcheck_ns
from modules.Reset.rest_api import NAMESPACE as Reset_ns

api = Api(title='ElectroMarket',
          version='1.0', description='', prefix='/energy/api', doc='/doc')

# Route
api.add_namespace(mapCode_ns)
api.add_namespace(Users_ns)
api.add_namespace(Resources_ns)
api.add_namespace(Admin_ns)
api.add_namespace(Healthcheck_ns)
api.add_namespace(Reset_ns)


