
# ceash - CEAsar SHell

ceash is an sh-compatible command language interpreter that executes commands read from the standard input.

# Setup

In the home directory:

```
pip install twosheds
git clone git@github.com:Ceasar/my_shell.git
ln -s my_shell/shell shell
```

To set as the default shell.

```
cat /etc/shells >> $HOME/shell
chsh -s $HOME/shell
```
