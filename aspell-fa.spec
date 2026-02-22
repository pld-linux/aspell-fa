Summary:	Persian dictionary for aspell
Summary(pl.UTF-8):	Perski słownik dla aspella
Name:		aspell-fa
Version:	0.11
%define	subv	0
Release:	2
License:	GPL v2+
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/aspell/dict/fa/aspell6-fa-%{version}-%{subv}.tar.bz2
# Source0-md5:	47c8599e529fc291a096c12f0b8372ca
URL:		http://aspell.net/
BuildRequires:	aspell >= 3:0.60
Requires:	aspell >= 3:0.60
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Persian dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Perski słownik (lista słów) dla aspella.

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
%{_prefix}/lib/aspell/*
%{_datadir}/aspell/*
