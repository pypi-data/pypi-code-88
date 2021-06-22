from dresscode.app import App
from dresscode.page import Page


def handler(page, cid):
    """
    page: the page object
    cid: the component id (here, the button cid)
    """
    # say 'Hello' !
    page.show_toast("Hello component {}".format(cid))
    # you can inspect the dict of components (keys are cid)
    components = page.components  # be curious, inspect the dict !
    # you can retrieve the data from a component
    username = page.read_component("username")
    # or you can display a large text
    page.show_text("Helloo\n{}".format(username), title="My large text")
    # or, ask for a confirmation
    ok = page.ask_confirmation()  # blocks the app, returns a boolean
    # you can even decide to scroll the content of the page
    page.scroll(value=1.0)
    # you can add a new page at runtime !!!
    app = page.app
    app.add_page(Page(pid="new_page", name="New"))
    # and guess what, you can open this new page !
    app.open_page("new_page")
    # and if you are in a hurry to open the home page
    app.open_home()


def get_home_page():
    # home page - a pid will be generated automatically if you don't set it
    page = Page(pid="home", name="Home")
    page.add_entry(cid="username", title="Username")
    # if you don't set a cid, it will be generated
    page.add_button(on_click=handler)  # a cid will be generated automatically

    # Note, if you click the button twice, you will get a:
    # dresscode.exception.DresscodeException
    # Duplicate page id isn't allowed (new_page) !
    # Guess why ! This isn't a bug but a feature ! hahaha !
    return page


app = App(title="Dresscode Demo", width=450, height=150, home="home")

app.add_page(get_home_page())

# lift up !
app.start()
