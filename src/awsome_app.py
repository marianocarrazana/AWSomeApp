from inspect import signature
import store


class AWSomeApp:
    def __init__(self):
        self.__main = None
        self.__routes = {'GET': {}, 'POST': {}, 'PUT': {}, 'DELETE': {}}

    def __call__(self, event, context):
        store.init()
        main_response = self.__main(event, context)
        print(f"{self.__routes=}")
        response = None
        route = event['pathParameters']['proxy']
        method = event['httpMethod']
        if route in self.__routes[method]:
            response = self.__routes[method][route]()
        return response or main_response

    def main(self, func):
        self.__main = func

    def get(self, route):
        def decorator(callback):
            self.__add_route('GET', route, callback)
            return
        return decorator

    def post(self, route):
        def decorator(callback):
            self.__add_route('POST', route, callback)
            return
        return decorator

    def put(self, route):
        def decorator(callback):
            self.__add_route('PUT', route, callback)
            return
        return decorator

    def delete(self, route):
        def decorator(callback):
            self.__add_route('DELETE', route, callback)
            return
        return decorator

    def __add_route(self, method: str, route: str, callback):
        func = signature(callback)
        params = list(func.parameters)
        print(f"{params=}")
        # TODO implement : https://github.com/marianocarrazana/rouge/blob/85b2279089949d69363021c0d039063a2f23d242/lib/router.php#L25
        self.__routes[method][route] = callback
