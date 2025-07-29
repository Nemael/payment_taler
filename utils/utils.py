class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

    def __init__(self):
       pass



def talog(*args):
    log = ""
    log = Color.BOLD + '2025-07-15 02:26:35,959 3068 TALER:' + Color.END
    log = Color.BOLD + Color.BLUE + '0000-00-00 00:00:00,000 0000 TALER: ' + Color.END
    for arg in args:
        log += str(arg)
    print(log)
