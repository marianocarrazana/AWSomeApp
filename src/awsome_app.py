import store
import re


class AWSomeApp:
    def __init__(self):
        self.__main = None
        self.__routes = []

    def __call__(self, event, context):
        store.init()
        main_response = self.__main(event, context)
        print(f"{self.__routes=}")
        response = None
        request_route = f"{event['httpMethod']} {event['pathParameters']['proxy']}"
        print(f"{request_route=}")
        for route in self.__routes:
            match = re.search(re.compile(route['route']), request_route)
            if match:
                print(f"Found route:{route['route']}")
                params = match.groupdict()
                print(f"{params=}")
                response = route['callback'](**params)
                break
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
        regexp = route.replace('/', '/')
        print(f"{regexp=}")
        with_names = re.sub(r'{([^\/:]+)(:[^\/]*)?}',
                            '(?P<\\1>[^\/]+)', regexp)
        final_route = f"^{method} {with_names}$"
        print(f"{final_route=}")
        self.__routes.append({'route': final_route, 'callback': callback})
