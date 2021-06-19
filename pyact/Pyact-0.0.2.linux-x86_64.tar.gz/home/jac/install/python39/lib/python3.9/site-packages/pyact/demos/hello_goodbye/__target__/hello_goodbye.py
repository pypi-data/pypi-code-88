import pyreact as pr

def greeter ():
    message, setMessage = pr.state (('Press Hello or Goodbye', 'black'))

    def sayHello ():
        setMessage (('Hello to you as well', 'green'))

    def sayGoodbye ():
        setMessage (('Goodbye to you as well', 'red'))

    return [
        pr.elem ('button', {'onClick': sayHello}, 'Hello'),
        pr.elem ('button', {'onClick': sayGoodbye}, 'Goodbye'),
        pr.elem ('div', {'style': {'color': message [1]}}, message [0])
    ]

pr.render (greeter, None, 'root')

