current = $(PWD)
worlds_dir=$(DESTDIR)$(datadir)/worldforge/worlds

dist-hook:
	mkdir -p $(distdir)
	(cd $(top_srcdir) && tar cf - `find . -name \*.xml` | ( cd $(current) && cd $(distdir) && tar xf -))

install-data-local:
	mkdir -p $(worlds_dir)
	(cd $(top_srcdir) && tar cf - `find . -name \*.xml`) | (cd $(worlds_dir) && tar xpf -)

uninstall-local:
	find $(worlds_dir) -name  \*.xml | xargs rm -f
