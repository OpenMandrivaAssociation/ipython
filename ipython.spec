%define name ipython
%define tar_name ipython
%define version 0.8.0
%define rel 1

Summary: 	An enhanced interactive Python shell
Name: 		%{name}
Version: 	%{version}
Release: 	%mkrel %{rel}
Source0: 	http://ipython.scipy.org/dist/%{tar_name}-%{version}.tar.bz2
Patch0:		setup.py.patch
License: 	BSD-like
Group: 		Development/Python
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires: 	python-devel
Requires: 	python
BuildArch: 	noarch
Url: 		http://ipython.scipy.org

%description

IPython provides a replacement for the interactive Python interpreter with
extra functionality.

Main features:

 * Comprehensive object introspection.

 * Input history, persistent across sessions.

 * Caching of output results during a session with automatically generated
   references.

 * Readline based name completion.

 * Extensible system of 'magic' commands for controlling the environment and
   performing many tasks related either to IPython or the operating system.

 * Configuration system with easy switching between different setups (simpler
   than changing $PYTHONSTARTUP environment variables every time).

 * Session logging and reloading.

 * Extensible syntax processing for special purpose situations.

 * Access to the system shell with user-extensible alias system.

 * Easily embeddable in other Python programs.

 * Integrated access to the pdb debugger and the Python profiler. 

%prep
%setup -q -n %{tar_name}-%{version}
%patch0 -p0

%build
%__python setup.py build

%install

%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot} --record=INSTALLED_FILES.tmp
%__rm -rf %{buildroot}%{_usr}/IPython
%__grep -v /usr/IPython/Extensions INSTALLED_FILES.tmp > INSTALLED_FILES

#%__rm -Rf %{buildroot}/usr/share/doc/ 
#%__grep -v /usr/share/doc INSTALLED_FILES.tmp > INSTALLED_FILES

%clean
%__rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc doc/* README
