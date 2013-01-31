INSTALLPATH="/usr/share/pyverlay"
INSTALLTEXT="pyverlay is now installed"
UNINSTALLTEXT="pyverlay has been removed"

install-req:
	@mkdir -p $(INSTALLPATH)
	@cp pyverlay/* $(INSTALLPATH) -f
	@cp README $(INSTALLPATH) -f
	@cp AUTHORS $(INSTALLPATH) -f
	@cp LICENSE $(INSTALLPATH) -f
	@cp bin/pyverlay /usr/bin/ -f
	@cp share/pyverlay.png /usr/share/pixmaps -f
	@cp share/pyverlay.desktop /usr/share/applications/ -f

install: install-req
	@echo $(INSTALLTEXT)

uninstall-req:
	@rm -rf $(INSTALLPATH)
	@rm /usr/share/pixmaps/pyverlay.png
	@rm /usr/share/applications/pyverlay.desktop
	@rm /usr/bin/pyverlay

uninstall: uninstall-req
	@echo $(UNINSTALLTEXT)
