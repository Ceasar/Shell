from sh import sh


def branch():
    """The current git branch."""
    try:
        return sh("git symbolic-ref --short HEAD 2> /dev/null").strip()
    except ValueError:
        return None


def status():
    try:
        return sh("git status --porcelain 2> /dev/null")
    except ValueError:
        return None
