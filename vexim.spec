# $Revision: 1.4 $
Summary:	Virtual Exim
Summary(pl):	Wirtualny Exim
Name:		vexim
Version:	2.0.1
Release:	0.1
License:	BSD-like
Group:		Networking/Daemons
Source0:	http://silverwraith.com/vexim/%{name}%{version}.tar.gz
# Source0-md5:	e0e667e64bc578f64d87d20b749c67d5
Patch0:		%{name}-perl_location.patch
Patch1:		%{name}-pld_locations.patch
URL:		http://silverwraith.com/vexim
PreReq:		exim
Requires:	apache
Requires:	php >= 4.2.1
Requires:	php-pear-DB
Requires:	php-pear-PEAR
Requires:	php-gettext
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Virtual Exim.

%description -l pl
Wirtualny Exim.

%package perl-utils
Summary:	Virtual Exim - Perl utils
Summary(pl):	Wirtualny Exim - narzêdzia w Perlu
Group:		Networking/Daemons
Requires:	perl-DBI

%description  perl-utils
Some Perl utils to create database.

%description perl-utils -l pl
Narzêdzie w Perlu do stworzenia bazy danych.

%prep
%setup -q -n %{name}2
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/home/services/vexim/{config,images,locale}
install -d $RPM_BUILD_ROOT/home/services/vexim/locale/{en_EN,ro_RO,hu_HU,de_DE}
install -d $RPM_BUILD_ROOT/home/services/vexim/locale/{en_EN,ro_RO,hu_HU,de_DE}/LC_MESSAGES

install -d $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}

install LICENSE $RPM_BUILD_ROOT/home/services/vexim/LICENSE
install vexim/*.php $RPM_BUILD_ROOT/home/services/vexim

install vexim/config/*.{php,po,pot} $RPM_BUILD_ROOT/home/services/vexim/config
install vexim/images/*.gif $RPM_BUILD_ROOT/home/services/vexim/images

install vexim/locale/en_EN/LC_MESSAGES/*.{po,mo} $RPM_BUILD_ROOT/home/services/vexim/locale/en_EN/LC_MESSAGES


install setup/create_db.pl $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}/create_db.pl
install setup/{pgsql,mysql}.sql $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}
install docs/vexim-* $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}
install docs/configure $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}/exim.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL LICENSE README TODO docs/*
#%attr(755,root,root) %{_bindir}/*
#%{_datadir}/%{name}
%dir /home/services/vexim
%attr(755,http,http) /home/services/vexim/*
%{_examplesdir}/%{name}
%exclude %{_examplesdir}/create_db.pl

%files perl-utils
%defattr(644,root,root,755)
%{_examplesdir}/create_db.pl
