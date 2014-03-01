# TODO: PLDify init script
Summary:	Tools for SRP/IB
Summary(pl.UTF-8):	Narzędzia do SRP/IB
Name:		srptools
Version:	1.0.2
Release:	1
License:	BSD or GPL v2
Group:		Networking/Utilities
Source0:	http://www.openfabrics.org/downloads/srptools/%{name}-%{version}.tar.gz
# Source0-md5:	164cd5b9f783dce19b142d6cd1a1c89a
URL:		http://www.openfabrics.org/
BuildRequires:	libstdc++-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
In conjunction with the kernel ib_srp driver, srptools allows you to
discover and use SCSI devices via the SCSI RDMA Protocol over
InfiniBand.

%description -l pl.UTF-8
W połączeniu ze sterownikiem jądra ib_srp, srptools pozwalają na
wykrywanie i używanie urządzeń SCSI poprzez protokół SCSI RDMA po
InfiniBand.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/rc.d
%{__mv} $RPM_BUILD_ROOT/etc/init.d $RPM_BUILD_ROOT/etc/rc.d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog NEWS README
%attr(755,root,root) %{_sbindir}/srp_daemon
%attr(755,root,root) %{_sbindir}/srp_daemon.sh
%attr(755,root,root) %{_sbindir}/ibsrpdm
%attr(755,root,root) %{_sbindir}/run_srp_daemon
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/srp_daemon.conf
%attr(754,root,root) /etc/rc.d/init.d/srpd
%config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/srp_daemon
#%config(noreplace) %verify(not md5 mtime size) /etc/rsyslog.d/srp_daemon.conf
%{_mandir}/man1/ibsrpdm.1*
%{_mandir}/man1/srp_daemon.1*
