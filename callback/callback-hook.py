def run(task, on_error):
    try:
        task()
    except Exception:
        on_error()

def success():
    print("success!")

def exception():
    x = 1 / 0

def failure():
    print("failure!")

run(success, failure)
run(exception, failure)