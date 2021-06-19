# __pragma__ ('skip')
document = React = ReactDOM = None
alert = console = None
# __pragma__ ('noskip')

elem = createElement = React.createElement
state = useState = React.useState

def render (component, properties, parentId):
    def main ():
        ReactDOM.render (
            React.createElement (component, properties),
            document.getElementById (parentId)
        )

    document.addEventListener ('DOMContentLoaded', main)
