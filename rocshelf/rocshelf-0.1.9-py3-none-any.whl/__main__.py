from rocshelf import main

main.set_path()

main.set_config([
    'rocshelf.json'
], {
    'shelf': 'rocshelf.json',
    'route': 'rocshelf.json'
})

main.start_cli()
