import datetime
import edifice
from edifice.components.forms import FormDialog

# StateManagers are key-value stores that UI components can bind to reactively:
# a change in the StateManager will refresh all subscribed UI components
fields = edifice.StateManager({
    "Name": "", # text input
    "Age": 20,  # text input with validation
    "Date": datetime.date(2021, 2, 1), # 3 dropdowns
    "Country": ("USA", ["USA", "UK", "France", "Japan"]), # dropdown
    "agreed": True, # checkbox
})

edifice.App(FormDialog(fields)).start()

print(fields["Name"])

class App:
    pass
