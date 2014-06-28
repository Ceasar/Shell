
Shell
====================

**Shell** is an sh-compatible command language interpreter that executes
commands read from the standard input.

Installation
------------

To install Shell, simply:

.. code-block:: bash

    $ git clone git@github.com:Ceasar/Shell.git
    $ cd Shell
    # install requirements
    $ make install
    # symlink to /usr/local/bin
    $ make link

Optionally, to set as the default shell:

.. code-block:: bash

    # make Shell a standard shell. requires root privileges.
    $ sudo make standard
    # change the default shell to Shell
    $ make default
