Summary:	Virtual Exim
Summary(pl):	Wirtualny Exim
Name:		vexim
Version:	2.0.1
Release:	1.5
License:	BSD-like
Group:		Networking/Daemons
Source0:	http://silverwraith.com/vexim/%{name}%{version}.tar.bz2
# Source0-md5:	d4490e9a4d92ca06bcc945932b7d19f3
Source1:	%{name}.conf
Patch0:		%{name}-perl_location.patch
Patch1:		%{name}-pld_locations.patch
URL:		http://silverwraith.com/vexim/
PreReq:		exim
Requires:	php4 >= 4.2.1
Requires:	php-pear-DB
Requires:	php4-gettext
Requires:	webserver
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_veximdir	%{_datadir}/%{name}
%define		_sysconfdir	/etc/%{name}

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
install -d $RPM_BUILD_ROOT{%{_sysconfdir},/etc/httpd} \
	$RPM_BUILD_ROOT%{_veximdir}/{config,images,locale} \
	$RPM_BUILD_ROOT%{_veximdir}/locale/{en_EN,ro_RO,hu_HU,de_DE} \
	$RPM_BUILD_ROOT%{_veximdir}/locale/{en_EN,ro_RO,hu_HU,de_DE}/LC_MESSAGES \
	$RPM_BUILD_ROOT%{_prefix}/src/examples/%{name} \
	$RPM_BUILD_ROOT/etc/mail

install %{SOURCE1} $RPM_BUILD_ROOT/etc/httpd/%{name}.conf

install vexim/*.{php,css} $RPM_BUILD_ROOT%{_veximdir}
install vexim/config/{a*,f*,h*,i*}.php $RPM_BUILD_ROOT%{_veximdir}/config
install vexim/config/variables.php $RPM_BUILD_ROOT%{_sysconfdir}
ln -sf %{_sysconfdir}/variables.php $RPM_BUILD_ROOT%{_veximdir}/config/variables.php
install vexim/images/*.gif $RPM_BUILD_ROOT%{_veximdir}/images

install vexim/locale/en_EN/LC_MESSAGES/*.mo $RPM_BUILD_ROOT%{_veximdir}/locale/en_EN/LC_MESSAGES
install vexim/locale/ro_RO/LC_MESSAGES/*.mo $RPM_BUILD_ROOT%{_veximdir}/locale/ro_RO/LC_MESSAGES
install vexim/locale/hu_HU/LC_MESSAGES/*.mo $RPM_BUILD_ROOT%{_veximdir}/locale/hu_HU/LC_MESSAGES
install vexim/locale/de_DE/LC_MESSAGES/*.mo $RPM_BUILD_ROOT%{_veximdir}/locale/de_DE/LC_MESSAGES

install setup/create_db.pl $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}/create_db.pl
install docs/vexim-* $RPM_BUILD_ROOT/etc/mail
install docs/configure $RPM_BUILD_ROOT/etc/mail/vexim_exim.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /etc/httpd/httpd.conf ] && ! grep -q "^Include.*%{name}.conf" /etc/httpd/httpd.conf; then
	echo "Include /etc/httpd/%{name}.conf" >> /etc/httpd/httpd.conf
	if [ -f /var/lock/subsys/httpd ]; then
		/usr/sbin/apachectl restart 1>&2
	fi
elif [ -d /etc/httpd/httpd.conf ]; then
	ln -sf /etc/httpd/%{name}.conf /etc/httpd/httpd.conf/99_%{name}.conf
	if [ -f /var/lock/subsys/httpd ]; then
		/usr/sbin/apachectl restart 1>&2
	fi
fi

%preun
if [ "$1" = "0" ]; then
	umask 027
	if [ -d /etc/httpd/httpd.conf ]; then
		rm -f /etc/httpd/httpd.conf/99_%{name}.conf
	else
		grep -v "^Include.*%{name}.conf" /etc/httpd/httpd.conf > \
			/etc/httpd/httpd.conf.tmp
		mv -f /etc/httpd/httpd.conf.tmp /etc/httpd/httpd.conf
	fi
	if [ -f /var/lock/subsys/httpd ]; then
		/usr/sbin/apachectl restart 1>&2
	fi
fi

%files
%defattr(644,root,root,755)
%doc INSTALL README TODO docs/* setup/*.sql
%dir %{_sysconfdir}
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%config(noreplace) %verify(not md5 mtime size) /etc/mail/*
%config(noreplace) %verify(not md5 mtime size) /etc/httpd/%{name}.conf
%attr(640,root,http) %config(noreplace) %{_veximdir}/config/variables.php
%dir %{_veximdir}
%dir %{_veximdir}/config
%{_veximdir}/config/auth*.php
%{_veximdir}/config/functions.php
%{_veximdir}/config/h*.php
%{_veximdir}/config/i18n.php
%{_veximdir}/images
%{_veximdir}/locale
%{_veximdir}/*.*

%files perl-utils
%defattr(644,root,root,755)
%dir %{_examplesdir}/%{name}
%{_examplesdir}/%{name}/create_db.pl
