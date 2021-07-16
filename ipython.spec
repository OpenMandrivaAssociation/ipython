Summary:	An interactive computing environment for Python 
Name:		ipython
Version:	7.25.0
Release:	1
License:	BSD
Group:		Development/Python
Url:		http://ipython.org
Source0:	https://files.pythonhosted.org/packages/c0/e5/ba19ae58e9bdd80832332873cb4e11a90cf2049df052c1aadeabc2cdadeb/ipython-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
Requires:	python >= 3.6
Requires:	python-pexpect >= 2.2
Recommends:	pyside >= 1.0.3
Recommends:	python-mpi4py
Recommends:	python-pygments 
Recommends:	python-pyzmq >= 2.1.4
%rename		python3-ipython

# Python 2.x has been dropped in the ipython 6.x series
Obsoletes:	python2-ipython

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

%install
PYTHONDONTWRITEBYTECODE= python setup.py install --root=%{buildroot}

chmod 644 %{buildroot}%{_mandir}/man1/*.1*
find %{buildroot} -name .buildinfo -exec rm -f {} \;
find %{buildroot} -name .git_commit_info.ini -exec rm -rf {} \;

%files
%{_bindir}/*
%{py_puresitedir}/*
%{_mandir}/man1/*
