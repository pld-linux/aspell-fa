Summary:	Persian dictionary for aspell
Summary(pl):	Perski s³ownik dla aspella
Name:		aspell-fa
Version:	0.03
%define	subv	0
Release:	1
License:	GPL v2+
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/fa/aspell6-fa-%{version}-%{subv}.tar.bz2
# Source0-md5:	21e1ef0ff91ba16b52f30169002cfd53
URL:		http://wordlist.sourceforge.net/
BuildRequires:	aspell >= 3:0.60
Requires:	aspell >= 3:0.60
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Persian dictionary (i.e. word list) for aspell.

%description -l pl
Perski s³ownik (lista s³ów) dla aspella.

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
%doc Copyright README doc/ChangeLog
%{_libdir}/aspell/*
%{_datadir}/aspell/*
