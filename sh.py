import subprocess


def sh(command):
    """Run a command in the shell and capture the output."""
    try:
        return subprocess.check_output(command, shell=True)
    except subprocess.CalledProcessError:
        raise ValueError("command failed")
