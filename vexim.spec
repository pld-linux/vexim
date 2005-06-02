Summary:	Virtual Exim
Summary(pl):	Wirtualny Exim
Name:		vexim
Version:	2.0.1
Release:	1.1
License:	BSD-like
Group:		Networking/Daemons
Source0:	http://silverwraith.com/vexim/%{name}%{version}.tar.bz2
# Source0-md5:	d4490e9a4d92ca06bcc945932b7d19f3
Patch0:		%{name}-perl_location.patch
Patch1:		%{name}-pld_locations.patch
URL:		http://silverwraith.com/vexim/
PreReq:		exim
Requires:	php >= 4.2.1
Requires:	php-pear-DB
Requires:	php-gettext
Requires:	webserver
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_veximdir	%{_datadir}/%{name}

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

install -d $RPM_BUILD_ROOT%{_veximdir}/{config,images,locale}
install -d $RPM_BUILD_ROOT%{_veximdir}/locale/{en_EN,ro_RO,hu_HU,de_DE}
install -d $RPM_BUILD_ROOT%{_veximdir}/locale/{en_EN,ro_RO,hu_HU,de_DE}/LC_MESSAGES
install -d $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}
install -d $RPM_BUILD_ROOT/etc/mail

install vexim/*.php $RPM_BUILD_ROOT%{_veximdir}
install vexim/config/*.{php,po,pot} $RPM_BUILD_ROOT%{_veximdir}/config
install vexim/images/*.gif $RPM_BUILD_ROOT%{_veximdir}/images

install vexim/locale/en_EN/LC_MESSAGES/*.mo $RPM_BUILD_ROOT%{_veximdir}/locale/en_EN/LC_MESSAGES
install vexim/locale/ro_RO/LC_MESSAGES/*.mo $RPM_BUILD_ROOT%{_veximdir}/locale/ro_RO/LC_MESSAGES
install vexim/locale/hu_HU/LC_MESSAGES/*.mo $RPM_BUILD_ROOT%{_veximdir}/locale/hu_HU/LC_MESSAGES
install vexim/locale/de_DE/LC_MESSAGES/*.mo $RPM_BUILD_ROOT%{_veximdir}/locale/de_DE/LC_MESSAGES

install setup/create_db.pl $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}/create_db.pl
install setup/{pgsql,mysql}.sql $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}
install docs/vexim-* $RPM_BUILD_ROOT/etc/mail
install docs/configure $RPM_BUILD_ROOT/etc/mail/vexim_exim.conf
install docs/configure $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}/exim.conf

find $RPM_BUILD_ROOT%{_veximdir} -name '*.po' -o -name '*.pot' | xargs rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL LICENSE README TODO docs/*
%{_examplesdir}/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/mail/*
%dir %{_veximdir}
%{_veximdir}/config
%{_veximdir}/images
%{_veximdir}/locale
%{_veximdir}/*.php

%files perl-utils
%defattr(644,root,root,755)
%{_examplesdir}/%{name}/create_db.pl
