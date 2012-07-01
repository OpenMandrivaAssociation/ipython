%define name	 ipython
%define version  0.13
%define	rel		 1	
%if %mdkversion < 201100
%define release	 %mkrel %rel
%else
%define	release %rel
%endif

Summary:	 IPython: Productive Interactive Computing
Name:		 %{name}
Version:	 %{version}
Release:	 %{release}
Source0:	 http://pypi.python.org/packages/source/i/%{ipython}/%{name}-%{version}.tar.gz
Source1:	 ipython.elc
Source2:	 html.tar.xz
License:	 BSD
Group:		 Development/Python
Url:		 http://ipython.org
BuildRoot:	 %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	 noarch
Requires:	 python >= 2.6
Requires:	 python-pexpect >= 2.2
Suggests:	 python-mpi4py
Suggests:	 wxPython, python-qt4, pyside >= 1.0.3
Suggests:	 python-pygments 
Suggests:	 python-pyzmq >= 2.1.4
Suggests:	 python-tornado >= 2.1
Suggests:	 python-httplib2
Suggests:	 python-sqlalchemy
Suggests:	 python-simplejson
BuildRequires:	 emacs, python-devel
Suggests:	 emacs-python-mode
%if %{mdkversion} > 201100
BuildRequires:	emacs-python-mode
%endif

%description
IPython provides a rich toolkit to help you make the most out of using
Python interactively. Its main components are:

* Powerful Python shells (terminal- and Qt-based).
* A web-based notebook with the same core features but support for
  rich media, text, code, mathematical expressions and inline plots.
* Support for interactive data visualization and use of 
  GUI toolkits.
* Flexible, embeddable interpreters to load into your own
  projects.
* A high-performance library for high level and interactive 
  parallel computing that works in multicore systems, clusters, 
  supercomputing and cloud scenarios.

%prep
%setup -q -n %{name}-%{version}

%build
PYTHONDONTWRITEBYTECODE= %__python setup.py build
%if %{mdkversion} > 201100
emacs -batch -f batch-byte-compile docs/emacs/ipython.el
%else
cp %SOURCE1 docs/emacs/
%endif
tar Jxf %SOURCE2

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}
%__mkdir -p %{buildroot}%{_datadir}/emacs/site-lisp/
%__install -m 644 docs/emacs/ipython.el* %{buildroot}%{_datadir}/emacs/site-lisp/
chmod 644 %{buildroot}%{_mandir}/man1/*.1*
find html -type d -exec chmod 755 {} \;
find html -type f -exec chmod 644 {} \;
find html -name .buildinfo -exec rm -f {} \;
find %{buildroot} -name .buildinfo -exec rm -f {} \;
find %{buildroot} -name .git_commit_info.ini -exec rm -rf {} \;

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc html docs/examples 
%{_bindir}/*
%{py_sitedir}/*
%{_datadir}/emacs/site-lisp/*
%{_mandir}/man1/*
