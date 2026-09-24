from os.path import dirname, join, realpath

from aiohttp.web import Application

from sqli import (
    incremental_codex_delta,
    incremental_codex_deser,
    incremental_codex_path,
    views,
)

DIR_PATH = dirname(realpath(__file__))


def setup_routes(app: Application):
    app.router.add_route('GET', r'/', views.index)
    app.router.add_route('POST', r'/', views.index)

    app.router.add_route('GET', r'/students/', views.students)
    app.router.add_route('POST', r'/students/', views.students)
    app.router.add_route('GET', r'/students/{id:\d+}', views.student)

    app.router.add_route('GET', r'/courses/', views.courses)
    app.router.add_route('POST', r'/courses/', views.courses)
    app.router.add_route('GET', r'/courses/{id:\d+}', views.course)

    app.router.add_route('POST',
                         r'/students/{student_id:\d+}/evaluate/{course_id:\d+}',
                         views.evaluate)

    app.router.add_route('GET',
                         r'/courses/{course_id:\d+}/review',
                         views.review)
    app.router.add_route('POST',
                         r'/courses/{course_id:\d+}/review',
                         views.review)

    app.router.add_route('POST', r'/logout/', views.logout)
    app.router.add_route("GET", r"/sto-incr/ping", incremental_codex_delta.ping)
    app.router.add_route(
        "GET", r"/sto-incr/file", incremental_codex_path.read_file
    )
    app.router.add_route(
        "GET", r"/sto-incr/load", incremental_codex_deser.load_object
    )
    app.router.add_static('/static', join(DIR_PATH, 'static'))
