INSTALLPATH="/usr/share/ohm-shell"
INSTALLTEXT="ohm-shell is now installed"
UNINSTALLTEXT="ohm-shell has been removed"

install-req:
	@mkdir -p $(INSTALLPATH)
	@cp ohm-shell/* $(INSTALLPATH) -f
	@cp README $(INSTALLPATH) -f
	@cp AUTHORS $(INSTALLPATH) -f
	@cp LICENSE $(INSTALLPATH) -f
	@cp bin/ohm-shell /usr/bin/ -f
	@cp bin/ohm-shell3 /usr/bin/ -f
	@cp share/ohm-shell.png /usr/share/pixmaps -f
	@cp share/ohm-shell.desktop /usr/share/applications/ -f
	@chmod 644 $(INSTALLPATH)/*
	@chmod +x $(INSTALLPATH)/ohm_shell.py
	@chmod 644 /usr/share/pixmaps/ohm-shell.png
	@chmod 644 /usr/share/applications/ohm-shell.desktop
	@chmod 644 /usr/bin/ohm-shell
	@chmod 644 /usr/bin/ohm-shell
	@chmod +x /usr/bin/ohm-shell
	@chmod 644 /usr/bin/ohm-shell3
	@chmod 644 /usr/bin/ohm-shell3
	@chmod +x /usr/bin/ohm-shell3

install: install-req
	@echo $(INSTALLTEXT)

uninstall-req:
	@rm -rf $(INSTALLPATH)
	@rm /usr/share/pixmaps/ohm-shell.png
	@rm /usr/share/applications/ohm-shell.desktop
	@rm /usr/bin/ohm-shell

uninstall: uninstall-req
	@echo $(UNINSTALLTEXT)
