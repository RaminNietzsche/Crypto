## Process this file with automake to produce Makefile.in
## Created by Anjuta

SUBDIRS = src 

python_cryphtodocdir = ${prefix}/doc/python_cryphto
python_cryphtodoc_DATA = \
	README\
	COPYING\
	AUTHORS\
	ChangeLog\
	INSTALL\
	NEWS


EXTRA_DIST = $(python_cryphtodoc_DATA)


# Remove doc directory on uninstall
uninstall-local:
	-rm -r $(python_cryphtodocdir)
