
# my_shell

My personal custom shell.

# Setup

In the home directory:

```
git clone git@github.com:Ceasar/my_shell.git
ln -s my_shell/shell shell
```

To set as the default shell.

```
cat /etc/shells >> $HOME/shell
chsh -s $HOME/shell
```
