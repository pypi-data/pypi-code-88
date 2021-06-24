from uvicorn import main

if __name__ == '__main__':
    main.params[0].default = 'asgi2rmq:app'
    main()
