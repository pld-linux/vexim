# $Revision: 1.1 $
Summary:	Virtual Exim
Summary(pl):	Wirtualny Exim
Name:		vexim
Version:	2.0.1
Release:	0
License:	GPL
Group:      Networking/Daemons
Source0:	http://silverwraith.com/vexim/%{name}%{version}.tar.gz
# Source0-md5:	e0e667e64bc578f64d87d20b749c67d5
#Patch0:		%{name}-what.patch
URL:		http://silverwraith.com/vexim
#BuildRequires:	
PreReq:		exim
#Requires(pre,post):	-
#Requires(preun):	-
#Requires(postun):	-
Requires:	apache
#Provides:	-
#Obsoletes:	-
#Conflicts:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Virtual Exim

%description -l pl
Wirtualny Exim

%prep
%setup -q -n %{name}2

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
install -d $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/home/services/vexim2/

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%postun

%files
%defattr(644,root,root,755)
%doc INSTALL  LICENSE  README  TODO docs/*
#%attr(755,root,root) %{_bindir}/*
#%{_datadir}/%{name}
