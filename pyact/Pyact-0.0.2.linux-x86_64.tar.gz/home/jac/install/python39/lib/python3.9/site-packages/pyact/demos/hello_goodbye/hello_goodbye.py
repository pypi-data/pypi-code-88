import pyact as pa

def greeter ():
    message, setMessage = pa.state (('Press Hello or Goodbye', 'black'))

    def sayHello ():
        setMessage (('Hello to you as well', 'green'))

    def sayGoodbye ():
        setMessage (('Goodbye to you as well', 'red'))

    return [
        pa.elem ('button', {'onClick': sayHello}, 'Hello'),
        pa.elem ('button', {'onClick': sayGoodbye}, 'Goodbye'),
        pa.elem ('div', {'style': {'color': message [1]}}, message [0])
    ]

pa.render (greeter, None, 'root')

