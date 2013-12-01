
ceash - CEAsar SHell
====================

ceash is an sh-compatible command language interpreter that executes commands
read from the standard input.

Installation
------------

To install ceash, simply:

.. code-block:: bash

    $ git clone git@github.com:Ceasar/ceash.git
    $ cd ceash
    # install requirements
    $ make install
    # symlink to /usr/local/bin
    $ make link

Optionally, to set as the default shell:

.. code-block:: bash

    # make ceash a standard shell. requires root privileges.
    $ sudo make standard
    # change the default shell to ceash
    $ make default
