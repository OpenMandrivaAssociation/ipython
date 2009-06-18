%define name	 ipython
%define tar_name ipython
%define version  0.9.1
%define rel 	 3

Summary: 	An enhanced interactive Python shell
Name: 		%{name}
Version: 	%{version}
Release: 	%mkrel %{rel}
Source0: 	http://ipython.scipy.org/dist/%{tar_name}-%{version}.tar.lzma
Patch0:		setupbase.py.patch

# compatible with earlier versions of python, based on sample at
# http://code.djangoproject.com/attachment/ticket/8078/sets.diff
Patch1:		python-2.6.patch

License: 	BSD-like
Group: 		Development/Python
Url: 		http://ipython.scipy.org
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: 	python
Requires:	python-zope-interface >= 3.4.1
Requires:	python-twisted >= 8.0.1
Requires:	python-foolscap >= 0.2.6
Requires:	python-pexpect >= 2.2
Suggests:	python-mpi4py
Suggests:	wxPython
BuildRequires: 	python-devel, emacs
BuildArch: 	noarch

%description
IPython is a free software project (released under the BSD license)
which tries to:

* Provide an interactive shell superior to Python's default. IPython
  has many features for object introspection, system shell access,
  and its own special command system for adding functionality when
  working interactively. It tries to be a very efficient environment
  both for Python code development and for exploration of problems
  using Python objects (in situations like data analysis).

* Serve as an embeddable, ready to use interpreter for your own
  programs. IPython can be started with a single call from inside
  another program, providing access to the current namespace. This
  can be very useful both for debugging purposes and for situations
  where a blend of batch-processing and interactive exploration are
  needed.

* Offer a flexible framework which can be used as the base
  environment for other systems with Python as the underlying
  language. Specifically scientific environments like Mathematica,
  IDL and Matlab inspired its design, but similar ideas can be
  useful in many fields.

* Allow interactive testing of threaded graphical toolkits. IPython
  has support for interactive, non-blocking control of GTK, Qt and
  WX applications via special threading flags. The normal Python
  shell can only do this for Tkinter applications.

%prep
%setup -q -n %{tar_name}-%{version}
%patch0 -p0
%patch1 -p1

%build
%__python setup.py build
emacs -batch -f batch-byte-compile docs/emacs/ipython.el

%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot} --record=FILELIST
%__mkdir -p %{buildroot}%{_datadir}/emacs/site-lisp/
%__install -m 644 docs/emacs/ipython.el* %{buildroot}%{_datadir}/emacs/site-lisp/

%clean
%__rm -rf %{buildroot}

%files -f FILELIST
%defattr(-,root,root)
%{_datadir}/emacs/site-lisp/*

