class style:
    default = 0
    bold = 1
    dim = 2
    underlined = 4
    # blink = 5
    reverse = 7
    # hidden = 8


class fg:
    default = 39
    black = 30
    red = 31
    green = 32
    yellow = 33
    blue = 34
    magenta = 35
    cyan = 36
    lightgray = 37


class bg:
    default = 49
    black = 40
    red = 41
    green = 42
    yellow = 43
    blue = 44
    magenta = 45
    cyan = 46
    lightgray = 47


def format(string, style=style.default, fg=fg.default, bg=bg.default):
    _format = ';'.join([str(style), str(fg), str(bg)])
    return '\x1b[%sm%s\x1b[0m' % (_format, string)


up = '\033[F'
