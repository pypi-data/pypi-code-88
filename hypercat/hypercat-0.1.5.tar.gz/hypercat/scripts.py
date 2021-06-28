from subprocess import check_call

def hcgui() -> None:
    check_call( ["python", "hypercat/hypercatgui.py"] )

