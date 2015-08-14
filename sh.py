import subprocess


def sh(command):
    """Run a command in the shell and capture the output."""
    try:
        return subprocess.check_output(command, shell=True)
    except subprocess.CalledProcessError as e:
        raise ValueError("'%s' failed: %s" % (command, e))
