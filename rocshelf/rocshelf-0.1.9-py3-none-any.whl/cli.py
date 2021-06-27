""" Основные команды для взаимодействия с приложением через командную строку.

Надстройка над модулем rcore.cli.
Который работает с помощью модуля rcore.cliengine.

Использовать rocshelf через CLI можно несколькими способами:
    Обращение к модулю на глобальном уровне:
        python -m rocshelf
    Написание скрипта вызова ( подробнее в документации rocshelf ):
        python frontend-rocshelf.py

        При запуске этого файла должна вызываться функции main.start_cli

"""

from rcore.cli import CLIOutput, Command, Option, Validator
from rcore.utils import input_yes_no

from rocshelf import exception as ex
from rocshelf import main
from rocshelf.components import relations, shelves
from rocshelf.components.routes import GetRoute
from rocshelf.middleware import UICompile, UIRoute, UIShelves


def _print_counter(counter):
    if counter['created'] != 0:
        print(f'Создано {counter["created"]} шелф элементов.')
    if counter['edited'] != 0:
        print(f'Изменено {counter["edited"]} шелф элементов.')
    if counter['deleted'] != 0:
        print(f'Удалено {counter["deleted"]} шелф элементов.')

    if counter['existing'] != 0:
        print(f'Уже имелось {counter["existing"]} шелф элементов.')
    if counter['missed'] != 0:
        print(f'Пропущено {counter["missed"]} шелф элементов.')


def _entrypoint(cliOut: CLIOutput):
    find_true = [cliOut.req[key] for key in cliOut.req if key != 'help']
    if True in find_true:
        main.print_rocshelf_info(**cliOut.req)
    else:
        cliOut.next()


def _help(cliOut: CLIOutput):
    find_true = [cliOut.req[key] for key in cliOut.req if key != 'help']
    if True in find_true:
        main.print_rocshelf_help_info(**cliOut.req)
    else:
        cliOut.next()


def _compile(cliOut: CLIOutput):
    UICompile(cliOut.req['framework']).compile()


def _shelf(cliOut: CLIOutput):

    next_command = str(cliOut.next_command)

    if next_command not in ['sync', 'create', 'delete', 'get'] or cliOut.next_command is None:
        cliOut.help()
        return

    if next_command != 'sync':
        sh = cliOut.next_command.req['shelf']
        name = cliOut.next_command.req['name']

        ui = UIShelves(sh, name)
        ui.output = 'print'

        if next_command == 'create':
            if 'layout' in cliOut.next_command.req:
                ui.create(cliOut.next_command.req['layout'])

            else:
                ui.create(False)

        elif next_command == 'delete':
            ui.delete()

        elif next_command == 'get':
            ui.get()

        _print_counter(ui.counter)

    else:
        layout = False
        if 'layout' in cliOut.next_command.req:
            layout = cliOut.next_command.req['layout']

        ui = UIShelves('sh', 'name')
        ui.sync(layout)

        if input_yes_no('Провести синхронизацию маршрутов?'):
            route_ui = UIRoute('name')
            route_ui.sync(layout)
            ui.merge_counts(route_ui.counter)

        _print_counter(ui.counter)


def _route_create(cliOut: CLIOutput):
    name = cliOut.req['name']
    page = False if 'page' not in cliOut.req else cliOut.req['page']
    layout = False if 'layout' not in cliOut.req else cliOut.req['layout']

    ui = UIRoute(name)
    ui.create(page, layout)

    shelf = shelves.GetShelf.name('page', page)

    if not shelf.check():
        if input_yes_no('Создать shelf-page с идентификатором - {page}?'):
            shelf_ui = UIShelves('page', page)
            shelf_ui.create(layout)
            ui.merge_counts(shelf_ui.counter)

    _print_counter(ui.counter)


def _route_delete(cliOut: CLIOutput):
    name = cliOut.req['name']

    ui = UIRoute(name)

    try:
        route = GetRoute.route(name)

        shelf = shelves.GetShelf.name('page', route.page)

        if shelf.check():
            if input_yes_no('Удалить shelf-page с идентификатором - ' + route.page + '?'):
                shelf_ui = UIShelves('page', route.page)
                shelf_ui.delete()
                ui.merge_counts(shelf_ui.counter)
    except ex.ex.errors.ItemNotFound:
        pass

    ui.delete()

    _print_counter(ui.counter)


def _route_sync(cliOut: CLIOutput):
    ui = UIRoute('name')
    ui.sync(
        False if 'layout' not in cliOut.req else cliOut.req['layout']
    )
    _print_counter(ui.counter)


entrypoint_command = Command('entrypoint', 'Entry point for interacting with the CLI', _entrypoint)


def init_cli():
    """ Инициализация CLI. Создание дерева команд """

    entrypoint_command.append(
        Option('description', 'Кэш', Validator(bool, [], False)),
        Option('clear', 'Очистить Кэш', Validator(bool, [], False)),
        Option('version', 'Версия приложения', Validator(bool, [], False)),
    )

    command = Command('help', 'Вспомогательные команды', _help)
    command.append(
        Option('configuration', 'Описание конфигурации', Validator(bool, [], False))
    )
    entrypoint_command.append(command)

    command = Command('compile', 'Компиляция сайта', _compile)
    command.append(
        Option(
            'framework', 'Для какого шаблонизатора адаптировать',
            Validator(str, relations.supported_framework, relations.supported_framework[0])
        )
    )
    entrypoint_command.append(command)

    command_shelf = Command('shelf', 'Работа с элементами', _shelf)
    entrypoint_command.append(command_shelf)

    command = Command('create', 'Создать элемент')
    command.append(
        Option('shelf', 'Тип элемента', Validator(str, shelves.SHELFTYPES)),
        Option('name', 'Путь и Имя элемента', Validator(str)),
        Option('layout', 'Использовать шаблоны файлов', Validator(bool, [], False))
    )
    command_shelf.append(command)

    command = Command('delete', 'Удалить элемент')
    command.append(
        Option('shelf', 'Тип элемента', Validator(str, shelves.SHELFTYPES)),
        Option('name', 'Имя элемента', Validator(str))
    )
    command_shelf.append(command)

    command = Command('sync', 'Синхронизировать элементы опираясь на файл конфигурации')
    command.append(
        Option('layout', 'Использовать шаблоны файлов', Validator(bool, [], False))
    )
    command_shelf.append(command)

    command_route = Command('route', 'Работа с маршрутами')
    entrypoint_command.append(command_route)

    command = Command('create', 'Создать маршрут', _route_create)
    command.append(
        Option('name', 'Индивидуальное имя маршрута', Validator(str)),
        Option('page', 'Имя shelf page', Validator(str))
    )
    command_route.append(command)

    command = Command('delete', 'Удалить маршрут', _route_delete)
    command.append(
        Option('name', 'Индивидуальное имя маршрута', Validator(str))
    )
    command_route.append(command)

    command = Command('sync', 'Проверить страницы на которые ссылаются маршруты', _route_sync)
    command.append(
        Option('layout', 'Использовать шаблоны файлов', Validator(bool, [], False))
    )
    command_route.append(command)
