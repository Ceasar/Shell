import os

from twosheds.transform import transform


def working_directory(transforms, short=False):
    """The current working directory."""
    try:
        pwd = os.getcwdu()
    except OSError:
        return "?"
    else:
        rv = transform(pwd, transforms, inverse=True)
        if short:
            parts = rv.split("/")
            if len(parts) == 1:
                return parts[0]
            else:
                x = "/".join(part[0:1] for part in parts[:-1])
                return "%s/%s" % (x, parts[-1])
