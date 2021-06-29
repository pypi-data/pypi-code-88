
def checksum(sentence):
    checksum = 0
    for el in sentence[1:]:
        checksum ^= ord(el)
    return "*" + str(format(checksum, 'x'))


def GTP(id, load_rate, consumption):
    """Gas Turbine Parameters"""
    fields = (
        ("Gas turbine ID", id),
        ("Load rate", load_rate),
        ("Consumption", consumption)
    )

    sentence = "$PFGTP,"
    for i in fields:
        sentence += str(i[1]) + ","

    return sentence + checksum(sentence) + "\t\n"


def SDS(id, state):
    """Safety Door System"""
    fields = (
        ("Door ID", id),
        ("Door state", state)
    )

    sentence = "$PFSDS,"
    for i in fields:
        sentence += str(i[1]) + ","

    return sentence + checksum(sentence) + "\t\n"


def SBS(id, capacity, level, quantity):
    """Safety Ballast System"""
    fields = (
        ("Ballast ID", id),
        ("Ballast capacity", capacity),
        ("Ballast level", level),
        ("Ballast quantity", quantity)
    )

    sentence = "$PFSBS,"
    for i in fields:
        sentence += str(i[1]) + ","

    return sentence + checksum(sentence) + "\t\n"


def SAS(id, state):
    """Safety Alarm System"""
    fields = (
        ("Alarm ID", id),
        ("Alarm state", state)
    )
    sentence = "$PFSAS,"
    for i in fields:
        sentence += str(i[1]) + ","
    return sentence + checksum(sentence) + "\t\n"
