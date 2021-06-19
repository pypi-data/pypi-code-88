# __pragma__ ('skip')
document = React = ReactDOM = None
# __pragma__ ('noskip')

elem = React.createElement
state = React.useState

def render (component, properties, parentId):
    def main ():
        ReactDOM.render (
            React.createElement (component, properties),
            document.getElementById (parentId)
        )

    document.addEventListener ('DOMContentLoaded', main)
    