%define name	 ipython
%define version  0.12
%define release	 %mkrel 2

Summary:	 IPython: Productive Interactive Computing
Name:		 %{name}
Version:	 %{version}
Release:	 %{release}
Source0:	 http://pypi.python.org/packages/source/i/%{ipython}/%{name}-%{version}.tar.gz
Source1:	 ipython.elc
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
* Tools for high level and interactive parallel computing.

%prep
%setup -q -n %{name}-%{version}

%build
%if %{mdkversion} > 201100
emacs -batch -f batch-byte-compile docs/emacs/ipython.el
%else
cp %SOURCE1 docs/emacs/
%endif

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}
%__mkdir -p %{buildroot}%{_datadir}/emacs/site-lisp/
%__install -m 644 docs/emacs/ipython.el* %{buildroot}%{_datadir}/emacs/site-lisp/
chmod 644 %{buildroot}%{_mandir}/man1/*.1*
find %{buildroot} -name .buildinfo -exec rm -f {} \;
find docs/html -name .buildinfo -exec rm -f {} \;
find %{buildroot} -name .git_commit_info.ini -exec rm -rf {} \;

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc docs/html docs/examples 
%{_bindir}/*
%{py_sitedir}/*
%{_datadir}/emacs/site-lisp/*
%{_mandir}/man1/*
