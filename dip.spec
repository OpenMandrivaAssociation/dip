Summary:	Handles the connections needed for dialup IP links
Name:		dip
Version:	3.3.7o
Release:	%mkrel 34
License:	GPL
Group:		Communications
URL:		ftp://sunsite.unc.edu/pub/Linux/system/network/serial
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/network/serial/dip337o-uri.tar.bz2
Patch0:		dip-3.3.7o-misc.patch
Patch1:		dip-3.3.7o-suffix.patch
Patch2:		dip-3.3.7o-fsstnd.patch
Patch3:		dip-3.3.7o-glibc.patch
Patch4:		dip-3.3.7o-sparc.patch
Patch5:		dip-3.3.7o-andor.patch
Patch6:		dip-arm.patch
Patch7:		dip-gcc295.patch
Patch8:		dip-3.3.7o-include.patch
# From Yellow Dog Linux 1.2
Patch9:		dip-3.3.7o-ppc.patch
Patch10:	dip-3.3.7o-gcc-3.3.patch
Patch11:	dip-3.3.7o-amd64.patch
Patch12:	dip-3.3.7o-gcc3.4-fix.patch
BuildRequires:	gccmakedep
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
ExcludeArch:	%mips
Requires:	setup >= 2.7.16

%description
Dip is a modem dialer.  Dip handles the connections needed for dialup IP links
like SLIP or PPP.  Dip can handle both incoming and outgoing connections, using
password security for incoming connections.  Dip is useful for setting up PPP
and SLIP connections, but isn't required for either. Netcfg uses dip for
setting up SLIP connections.

Install dip if you need a utility which will handle dialup IP connections.

%prep

%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch4 -p0
%patch5 -p1 -b .andor
%patch3 -p1 -b .glibc
%patch6 -p1 -b .arm
%patch7 -p1 -b .gcc295
%patch8 -p0 -b .include
%patch9 -p1 -b .ppc
%patch10 -p1 -b .gcc3.3
%patch11 -p1 -b .amd64
%patch12 -p1 -b .gcc34

%build
make depend
cd skey; make clean; make linux; cd -
uname -a|grep SMP && make -j 2 RPM_OPT_FLAGS="$RPM_OPT_FLAGS" || %make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_mandir}/man8

install -c -s dip %{buildroot}%{_sbindir}
ln -sf dip %{buildroot}%{_sbindir}/diplogini
install -c -m 0444 dip.8 %{buildroot}%{_mandir}/man8
ln -sf dip.8%{_extension} %{buildroot}%{_mandir}/man8/diplogin.8%{_extension}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%attr(0755,root,dialout) %{_sbindir}/dip
%{_sbindir}/diplogini
%{_mandir}/man8/dip.8*
%{_mandir}/man8/diplogin.8*
