from wsgiref.simple_server import make_server
import falcon

class HealthcheckResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_TEXT
        resp.text = ('\nTwo things awe me most, the starry sky '
                     'above me and the moral law within me.\n'
                     '\n'
                     '    ~ Immanuel Kant\n\n')

api = falcon.App()

health_check_resource = HealthcheckResource()
api.add_route('/', health_check_resource)
api.add_route('/{place_holder}', health_check_resource)