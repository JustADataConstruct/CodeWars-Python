"""
6kyu "Simple web framework #1: Create a basic router" kata
https://www.codewars.com/kata/588a00ad70720f2cd9000005/python
In this Kata, you have to design a simple routing class for a web framework.

The router should accept bindings for a given url, http method and an action.

Then, when a request with a bound url and method comes in, it should return the result of the action.
15-12-2021
"""

import codewars_test as test


class Router():
    def __init__(self) -> None:
        self.gets = {}
        self.posts = {}

    def bind(self, url: str, method: str, action):
        if method == "GET":
            self.gets[url] = action
        elif method == "POST":
            self.posts[url] = action

    def runRequest(self, url: str, method: str) -> str:
        if method == "GET":
            return self.gets[url]() if url in self.gets else 'Error 404: Not Found'
        else:
            return self.posts[url]() if url in self.posts else 'Error 404: Not Found'


test.describe('Should handle GET routes')
router = Router()
router.bind('/hello', 'GET', lambda: 'hello world')
router.bind('/login', 'GET', lambda: 'Please log-in.')

test.assert_equals(router.runRequest('/hello', 'GET'), 'hello world')
test.assert_equals(router.runRequest('/login', 'GET'), 'Please log-in.')

test.describe('Should handle POST routes')

router = Router()
router.bind('/vote', 'POST', lambda: 'Voted.')
router.bind('/comment', 'POST', lambda:  'Comment sent.')

test.assert_equals(router.runRequest('/vote', 'POST'), 'Voted.')
test.assert_equals(router.runRequest('/comment', 'POST'), 'Comment sent.')

test.describe('Should handle mixed routes.')

router = Router()
router.bind('/login', 'GET', lambda: 'Please log-in.')
router.bind('/login', 'POST', lambda: 'Logging-in.')

test.assert_equals(router.runRequest('/login', 'GET'), 'Please log-in.')
test.assert_equals(router.runRequest('/login', 'POST'), 'Logging-in.')


test.describe('Should return 404 for non-existing routes.')

router = Router()
test.assert_equals(router.runRequest(
    '/this-url-does-not-exist', 'GET'), 'Error 404: Not Found')


test.describe('Should modify existing routes')

router = Router()
router.bind('/page', 'GET', lambda: 'First binding.')
router.bind('/page', 'GET', lambda: 'Modified binding.')

test.assert_equals(router.runRequest('/page', 'GET'), 'Modified binding.')
