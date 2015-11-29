%define 	fname	AuthKit
Summary:	An authentication and authorization toolkit for WSGI applications and frameworks
Summary(pl.UTF-8):	Pakiet narzędzi do uwierzytelniania i autoryzacji dla aplikacji WSGI
Name:		python-%{fname}
Version:	0.4.5
Release:	1
License:	MIT
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/A/AuthKit/%{fname}-%{version}.tar.gz
# Source0-md5:	0336ba96de32ea97f6058bed5549b30c
URL:		http://authkit.org
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	python >= 1:2.5
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AuthKit is an authentication and authorization toolkit for WSGI
applications and frameworks.
- Built for WSGI applications and middleware
- Sophisticated and extensible permissions system
- Built in support for HTTP basic, HTTP digest, form, cookie and
  OpenID authentication methods plus others
- Easily define users, passwords and roles
- Designed to be totally extensible so you can use the components to
  integrate with a database, LDAP connection or your own custom system
- Plays nicely with the Pylons web framework

%description -l pl.UTF-8
AuthKit dostarcza pakiet narzędzi do uwierzytelniania i autoryzacji
dla frameworków i aplikacji WSGI.
- Opracowany z myślą o aplikacjach i middleware WSGI
- Złożony i rozszerzalny mechanizm uprawnień
- Wbudowane wsparcie dla metod uwierzytelniania HTTP basic, HTTP
  digest form, cookie oraz OpenID, jak również innych
- Proste definiowanie użytkowników, haseł oraz ról
- Zaprojektowany tak, by być w pełni rozszerzalny, zatem można go
  wykorzystać integrując z bazą danych, serwerem LDAP jak również
  autorskim systemem
- Dobrze współpracuje z frameworkiem webowym Pylons

%prep
%setup -q -n %{fname}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/authkit
%{py_sitescriptdir}/%{fname}-%{version}-py*.egg-info
