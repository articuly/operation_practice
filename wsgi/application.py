def simple_app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type',
                         'text/plain;charset=utf-8')]
    result = "Hello World"
    print(environ.items())
    if environ['PATH_INFO'] == "/abc":
        result = "ABC"
    if environ['PATH_INFO'] == "/myfun":
        result = myfun()
    start_response(status, response_headers)
    return [bytes(result, encoding="utf-8"), b'\n']


def myfun():
    return "welcome..."
