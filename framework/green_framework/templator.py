from jinja2 import FileSystemLoader
from jinja2.environment import Environment


# def render(template_name, folder='templates', **kwargs):
# """
# :param template_name: имя шаблона
# :param folder: папка в которой ищем шаблон
# :param kwargs: параметры
# :return:
# """
# file_path = join(folder, template_name)
# # Открываем шаблон по имени
# with open(file_path, encoding='utf-8') as f:
#     # Читаем
#     template = Template(f.read())
# # рендерим шаблон с параметрами
# return template.render(**kwargs)
def render(template_name, folder='templates', **kwargs):
    """
    Renders template via template name and with custom kwargs
    :param template_name: name of the template
    :param folder: templates folder, default is "templates'
    :param kwargs: template kwargs
    :return: rendered template
    """
    env = Environment()
    env.loader = FileSystemLoader(folder)
    template = env.get_template(template_name)
    return template.render(**kwargs)
