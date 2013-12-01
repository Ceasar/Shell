.PHONY: install link add_shell default

PWD = $(shell pwd)
INSTALL = /usr/local/bin/ceash

install:
	pip install -r requirements.txt

link:
	ln -is $(PWD)/ceash $(INSTALL)

# requires root privileges
standard: $(INSTALL)
	echo $(INSTALL) >> /etc/shells

default: $(INSTALL)
	chsh -s $(INSTALL)
