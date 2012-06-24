Summary:	Persian dictionary for aspell
Summary(pl):	Perski s�ownik dla aspella
Name:		aspell-fa
Version:	0.02
%define	subv	0
Release:	1
License:	GPL v2+
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/fa/aspell6-fa-%{version}-%{subv}.tar.bz2
# Source0-md5:	4583ef4b8b2456f737e3d60ede1e9034
URL:		http://wordlist.sourceforge.net/
BuildRequires:	aspell >= 3:0.60
Requires:	aspell >= 3:0.60
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Persian dictionary (i.e. word list) for aspell.

%description -l pl
Perski s�ownik (lista s��w) dla aspella.

%prep
%setup -q -n aspell6-fa-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_libdir}/aspell/*
%{_datadir}/aspell/*
