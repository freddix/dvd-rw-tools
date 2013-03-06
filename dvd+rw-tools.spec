Summary:	Toolchain for mastering recordable DVD media
Name:		dvd+rw-tools
Version:	7.1
Release:	13
License:	GPL
Group:		Applications/Multimedia
Source0:	http://fy.chalmers.se/~appro/linux/DVD+RW/tools/%{name}-%{version}.tar.gz
# Source0-md5:	8acb3c885c87f6838704a0025e435871
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-cdrkit.patch
Patch2:		%{name}-include.patch
Patch3:		%{name}-dvddl.patch
Patch4:		%{name}-wctomb.patch
Patch5:		%{name}-wexit.patch

URL:		http://fy.chalmers.se/~appro/linux/DVD+RW/
BuildRequires:	libstdc++-devel
BuildRequires:	m4
Requires:	cdrkit
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Collection of tools to master DVD+RW/+R/-R/-RW media.


%package btcflash
Summary:	BTC CD/DVD reader/writer firmware updater
Group:		Applications/Multimedia

%description btcflash
BTC CD/DVD reader/writer firmware updater.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%{__make} \
	CC="%{__cc}"			\
	CFLAGS="%{rpmcflags} -Wall"	\
	CXX="%{__cxx}"			\
	CXXFLAGS="%{rpmcflags} -fno-exceptions -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix} \
	manprefix=%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc index.html
%attr(755,root,root) %{_bindir}/*
%exclude %{_bindir}/btcflash
%{_mandir}/man1/*

%files btcflash
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/btcflash

