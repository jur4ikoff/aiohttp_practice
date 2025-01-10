from aiohttp import web # Аиохттп
import jinja2 # Шаблонизатор jinja2
import aiohttp_jinja2

# В этой функции производится настройка путей для всего приложения
def setup_routes(application):
    # Импорт
    from app.forum.routes import setup_routes as setup_from_routes
    setup_from_routes(application)

def setup_external_libraries(application: web.Application) -> None:
    # указываем шаблонизатору, что html-шаблоны надо искать в папке templates
    aiohttp_jinja2.setup(application, loader=jinja2.FileSystemLoader("templates"))

if __name__ == "__main__":
    application = web.Application() # Создаем веб-сервер

    # Настройка веб-сервера
    setup_external_libraries(application)
    setup_routes(application)
    # Запускаем веб-сервер
    web.run_app(application)