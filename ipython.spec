%define name	 ipython
%define version  0.10.1
%define rel 	 2

Summary: 	An enhanced interactive Python shell
Name: 		%{name}
Version: 	%{version}
Release: 	%mkrel %{rel}
Source0: 	http://ipython.scipy.org/dist/%{name}-%{version}.tar.gz
Patch0:		setupbase.py.patch
License: 	BSD-like
Group: 		Development/Python
Url: 		http://ipython.scipy.org
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:      noarch
Requires:	python-zope-interface >= 3.4.1
Requires:	python-twisted >= 8.0.1
Requires:	python-foolscap >= 0.2.6
Requires:	python-pexpect >= 2.2
Requires:	python-OpenSSL
Suggests:	python-mpi4py
Suggests:	wxPython
BuildRequires: 	emacs
%py_requires -d 

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
%setup -q -n %{name}-%{version}
%patch0 -p0

%build
emacs -batch -f batch-byte-compile docs/emacs/ipython.el

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILELIST
%__mkdir -p %{buildroot}%{_datadir}/emacs/site-lisp/
%__install -m 644 docs/emacs/ipython.el* %{buildroot}%{_datadir}/emacs/site-lisp/
%__rm -f %{buildroot}%{_docdir}/%{name}/manual/ipython.pdf
cp -f README.txt %{buildroot}%{_docdir}/%{name}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/emacs/site-lisp/*
%{_docdir}/%{name}
%{_mandir}/man1/*
%{py_sitedir}/*
