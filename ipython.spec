Summary:	 An interactive computing environment for Python 
Name:		 ipython
Version:	 0.11
Release:	 4
Source0:	 http://pypi.python.org/packages/source/i/%{ipython}/%{name}-%{version}.tar.gz
License:	 BSD
Group:		 Development/Python
Url:		 http://ipython.org
BuildArch:	 noarch
Requires:	 python >= 2.6
Requires:	 python-pexpect >= 2.2
Suggests:	 python-mpi4py
Suggests:	 wxPython, python-qt4, pyside >= 1.0.3
Suggests:	 python-pygments 
Suggests:	 python-pyzmq >= 2.1.4
BuildRequires:	 emacs, python-devel

%description
The goal of IPython is to create a comprehensive environment for
interactive and exploratory computing. To support this goal, IPython
has two main components:

* An enhanced interactive Python shell.
* An architecture for interactive parallel computing.

The enhanced interactive Python shell has the following main features:

* Comprehensive object introspection.
* Input history, persistent across sessions.
* Caching of output results during a session with automatically
  generated references.
* Readline based name completion.
* Extensible system of 'magic' commands for controlling the
  environment and performing many tasks related either to IPython or
  the operating system.
* Configuration system with easy switching between different setups
  (simpler than changing $PYTHONSTARTUP environment variables every
  time).
* Session logging and reloading.
* Extensible syntax processing for special purpose situations.
* Access to the system shell with user-extensible alias system.
* Easily embeddable in other Python programs and wxPython GUIs.
* Integrated access to the pdb debugger and the Python profiler.

The parallel computing architecture has the following main features:

* Quickly parallelize Python code from an interactive Python/IPython
  session.
* A flexible and dynamic process model that be deployed on anything
  from multicore workstations to supercomputers.
* An architecture that supports many different styles of parallelism,
  from message passing to task farming.
* Both blocking and fully asynchronous interfaces.
* High level APIs that enable many things to be parallelized in a few
  lines of code.
* Share live parallel jobs with other users securely.
* Dynamically load balanced task farming system.  
* Robust error handling in parallel code.

%prep
%setup -q -n %{name}-%{version}

%build
emacs -batch -f batch-byte-compile docs/emacs/ipython.el

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}
%__mkdir -p %{buildroot}%{_datadir}/emacs/site-lisp/
%__install -m 644 docs/emacs/ipython.el* %{buildroot}%{_datadir}/emacs/site-lisp/
chmod 644 %{buildroot}%{_mandir}/man1/*.1*
find %{buildroot} -name .buildinfo -exec rm -f {} \;
find %{buildroot} -name .git_commit_info.ini -exec rm -rf {} \;

# Drop shebang from non-executable scripts to make rpmlint happy
find %{buildroot}%{py_sitedir} -name "*py" -perm 644 -exec sed -i '/#!\/usr\/bin\/env python/d' {} \;

%files
%defattr(-,root,root)
%doc docs/examples
%{_bindir}/*
%{py_sitedir}/*
%{_datadir}/emacs/site-lisp/*
%{_mandir}/man1/*


%changelog
* Sun Jul 31 2011 Lev Givon <lev@mandriva.org> 0.11-2mdv2011.0
+ Revision: 692581
- Need python-devel to build.

* Sun Jul 31 2011 Lev Givon <lev@mandriva.org> 0.11-1
+ Revision: 692576
- Update to 0.11.

* Sun Apr 10 2011 Lev Givon <lev@mandriva.org> 0.10.2-1
+ Revision: 652184
- Update to 0.10.2.

* Sat Oct 30 2010 Michael Scherer <misc@mandriva.org> 0.10.1-2mdv2011.0
+ Revision: 590316
- rebuild for python 2.7

* Tue Oct 12 2010 Lev Givon <lev@mandriva.org> 0.10.1-1mdv2011.0
+ Revision: 585176
- Update to 0.10.1.

* Wed Aug 12 2009 Lev Givon <lev@mandriva.org> 0.10-1mdv2010.0
+ Revision: 415723
- Update to 0.10.

* Fri Jun 19 2009 Paulo Andrade <pcpa@mandriva.com.br> 0.9.1-3mdv2010.0
+ Revision: 387239
- Correct python 2.6 deprecation warnings in a backwards compatible way.

* Tue Jan 06 2009 Funda Wang <fwang@mandriva.org> 0.9.1-2mdv2009.1
+ Revision: 325674
- rebuild

* Wed Sep 17 2008 Lev Givon <lev@mandriva.org> 0.9.1-1mdv2009.1
+ Revision: 285518
- Update to 0.9.1.
- Update to 0.9.

* Sun Jun 01 2008 Lev Givon <lev@mandriva.org> 0.8.4-1mdv2009.0
+ Revision: 213866
- Update to 0.8.4.

* Thu May 29 2008 Lev Givon <lev@mandriva.org> 0.8.3-1mdv2009.0
+ Revision: 213052
- Update to 0.8.3.

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - kill extra spacing at top of description

* Sun Dec 02 2007 Lev Givon <lev@mandriva.org> 0.8.2-1mdv2008.1
+ Revision: 114366
- Update to 0.8.2.

* Thu May 10 2007 Lev Givon <lev@mandriva.org> 0.8.1-1mdv2008.0
+ Revision: 25997
- Update to 0.8.1.

* Tue Apr 17 2007 Lev Givon <lev@mandriva.org> 0.8.0-1mdv2008.0
+ Revision: 13736
- Update to 0.8.0.


* Thu Dec 21 2006 Gaëtan Lehmann <glehmann@mandriva.org> 0.7.3-1mdv2007.0
+ Revision: 101121
- 0.7.3

* Sun Dec 10 2006 Lev Givon <lev@mandriva.org> 0.7.2-4mdv2007.1
+ Revision: 94433
- Include man pages properly.
- Fix license.
  Make sure package can still build properly with Python < 2.5.

* Mon Dec 04 2006 Lev Givon <lev@mandriva.org> 0.7.2-3mdv2007.1
+ Revision: 90453
- Update to build properly with Python 2.5.

* Sat Oct 28 2006 Lev Givon <lev@mandriva.org> 0.7.2-2mdv2007.1
+ Revision: 73563
- Patch Shell.py to not call deprecated gdk methods when running pylab.
- Import ipython

* Thu Jun 08 2006 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 0.7.2-1mdv2007.0
- New release 0.7.2

* Tue Jan 31 2006 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 0.7.1.fix1-1mdk
- New release 0.7.1.fix1

* Tue Jan 24 2006 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 0.7.1-1mdk
- New release 0.7.1

* Wed Jan 11 2006 Michael Scherer <misc@mandriva.org> 0.7.0-3mdk
- make it rpmbuildupdatable ( and fix the wrong upload with 1mdk )

* Wed Jan 11 2006 Michael Scherer <misc@mandriva.org> 0.7.0-2mdk
- Use new python macro

* Tue Jan 10 2006 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 0.7.0-1mdk
- New release 0.7.0
- drop Patch0 (merged upstream)

* Sun Jun 12 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 0.6.15-1mdk
- New release 0.6.15
- Patch0: fix completion for objects with invalid attribute names
- use mkrel
- remove dot in summary

* Fri Mar 04 2005 Michael Scherer <misc@mandrake.org> 0.6.12-1mdk
- New release 0.6.12

* Thu Feb 17 2005 Michael Scherer <misc@mandrake.org> 0.6.11-1mdk
- New release 0.6.11

* Fri Jan 28 2005 Michael Scherer <misc@mandrake.org> 0.6.10-1mdk
- New release 0.6.10

* Thu Dec 16 2004 Michael Scherer <misc@mandrake.org> 0.6.6-1mdk
- New release 0.6.6

* Sat Dec 04 2004 Michael Scherer <misc@mandrake.org> 0.6.5-2mdk
- Rebuild for new python

* Fri Dec 03 2004 Michael Scherer <misc@mandrake.org> 0.6.5-1mdk
- New release 0.6.5

* Fri Nov 12 2004 Michael Scherer <misc@mandrake.org> 0.6.4-1mdk
- New release 0.6.4
- fix tarname

* Sat Oct 02 2004 Michael Scherer <misc@mandrake.org> 0.6.3-1mdk
- New release 0.6.3

* Thu Jul 01 2004 Michael Scherer <misc@mandrake.org> 0.6.0-1mdk
- First release for Mandrakelinux, based on work from Fernando Perez <fperez@colorado.edu>

