Summary:	An interactive computing environment for Python 
Name:		ipython
Version:	0.13.1
Release:	2
License:	BSD
Group:		Development/Python
Url:		http://ipython.org
Source0:	http://pypi.python.org/packages/source/i/%{ipython}/%{name}-%{version}.tar.gz
Source1:        ipython.elc
Source2:        html.tar.xz
BuildArch:	noarch

BuildRequires:	emacs
BuildRequires:	pkgconfig(python)
BuildRequires:  emacs-python-mode
Requires:	python >= 2.6
Requires:	python-pexpect >= 2.2
Suggests:	pyside >= 1.0.3
Suggests:	python-mpi4py
Suggests:	python-pygments 
Suggests:	python-pyzmq >= 2.1.4
Suggests:	python-qt4
Suggests:	wxPython

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
%setup -q

%build
emacs -batch -f batch-byte-compile docs/emacs/ipython.el

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}
mkdir -p %{buildroot}%{_datadir}/emacs/site-lisp/
install -m 644 docs/emacs/ipython.el* %{buildroot}%{_datadir}/emacs/site-lisp/
chmod 644 %{buildroot}%{_mandir}/man1/*.1*
find %{buildroot} -name .buildinfo -exec rm -f {} \;
find %{buildroot} -name .git_commit_info.ini -exec rm -rf {} \;

# Drop shebang from non-executable scripts to make rpmlint happy
find %{buildroot}%{py_sitedir} -name "*py" -perm 644 -exec sed -i '/#!\/usr\/bin\/env python/d' {} \;

%files
%doc docs/examples
%{_bindir}/*
%{py_sitedir}/*
%{_datadir}/emacs/site-lisp/*
%{_mandir}/man1/*

