def admin_only(log):
    def admin_check():
        if id == 1:
            print("Hello")
            log()
        else:
            print("Nope!")
    return admin_check


def decorator_2(log):
    def inner_func():
        print("I am the 2nd func")
        log()
    return inner_func


@decorator_2
@admin_only
def bye_printer():
    print("Bye")


id = 2
bye_printer()