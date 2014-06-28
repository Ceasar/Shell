.PHONY: install add_shell default

NAME = Shell
PWD = $(shell pwd)
INSTALL = /usr/local/bin/$(NAME)

install:
	pip install -r requirements.txt

$(INSTALL):
	ln -is $(PWD)/$(NAME) $(INSTALL)

# requires root privileges
standard: $(INSTALL)
	echo $(INSTALL) >> /etc/shells

default: $(INSTALL)
	chsh -s $(INSTALL)
