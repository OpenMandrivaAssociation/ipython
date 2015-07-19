Summary:	An interactive computing environment for Python 
Name:		ipython
Version:	2.3.0
Release:	3
License:	BSD
Group:		Development/Python
Url:		http://ipython.org
Source0:	http://pypi.python.org/packages/source/i/%{ipython}/%{name}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	pkgconfig(python)
BuildRequires:  pkgconfig(python3)
BuildRequires:  python2-distribute
BuildRequires:  python3-distribute
Requires:	python >= 2.6
Requires:	python-pexpect >= 2.2
Suggests:	pyside >= 1.0.3
Suggests:	python-mpi4py
Suggests:	python-pygments 
Suggests:	python-pyzmq >= 2.1.4
Suggests:	python-qt4
Suggests:	wxPython
%rename		python3-ipython

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

%package -n python2-ipython
Summary:        An interactive computing environment for Python 2
Group:          Development/Python
License:        BSD
Requires:	python3
Requires:	python3-pexpect
#Suggests:	pyside
#Suggests:	python-mpi4py
#Suggests:	python-pygments
#Suggests:	python-pyzmq >= 2.1.4
#Suggests:	python-qt4
#Suggests:	wxPython

%description -n python2-ipython
IPython built for Python2

%prep
%setup -qc
mv %{name}-%{version} python2
cp -a python2 python3

%install
pushd python3
PYTHONDONTWRITEBYTECODE= python3 setup.py install --root=%{buildroot}
popd

pushd python2
PYTHONDONTWRITEBYTECODE= python2 setup.py install --root=%{buildroot}
popd

chmod 644 %{buildroot}%{_mandir}/man1/*.1*
find %{buildroot} -name .buildinfo -exec rm -f {} \;
find %{buildroot} -name .git_commit_info.ini -exec rm -rf {} \;

# Drop shebang from non-executable scripts to make rpmlint happy
#find %{buildroot}%{py_sitedir} -name "*py" -perm 644 -exec sed -i '/#!\/usr\/bin\/env python/d' {} \;
#find %{buildroot}%{py3_sitedir} -name "*py" -perm 644 -exec sed -i '/#!\/usr\/bin\/env python/d' {} \;

%files
%{_bindir}/*3
%{py3_puresitedir}/*
%{_mandir}/man1/*

%files -n python2-ipython
%{_bindir}/*
%exclude %{_bindir}/*3
%{py2_puresitedir}/*
