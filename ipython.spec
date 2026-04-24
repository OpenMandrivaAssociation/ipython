%define oname IPython

Name:		ipython
Summary:	An interactive computing environment for Python 
Version:	9.13.0
Release:	1
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://ipython.org
Source0:	https://files.pythonhosted.org/packages/source/i/ipython/ipython-%{version}.tar.gz

BuildSystem:  python
BuildArch:	noarch
BuildRequires:	fdupes
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
Requires:	python >= 3.11
Recommends:	pyside >= 1.0.3
Recommends:	python%{pyver}dist(mpi4py)
Recommends:	python%{pyver}dist(pygments)
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

%prep -a
# Remove bundled egg-info
rm -rf %{name}.egg-info

%install -a
# These can be run stand-alone, so make them executable rather than removing shebang
find %{buildroot}%{python_sitelib} -type f -name "*.py" -exec sed -i "s|^#!%{_bindir}/env python$|#!%{__python}|" {} \;
find %{buildroot}%{python_sitelib} -type f -name "*.py" -exec sed -i "s|^#!%{_bindir}/python$|#!%{__python}|" {} \;
find %{buildroot}%{python_sitelib} -type f -name "*.py" -exec grep -q "#!%{__python}" {} \; -exec chmod a+x {} \;

%files
%{_bindir}/%{name}
%{_bindir}/%{name}3
%{_mandir}/man1/%{name}.1.*
%{python_sitelib}/%{oname}
%{python_sitelib}/%{name}-%{version}.dist-info
