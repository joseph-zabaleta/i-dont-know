from subprocess import check_call

def start() -> None:
    check_call(
        ["python","i_dont_care/main.py"]
    )