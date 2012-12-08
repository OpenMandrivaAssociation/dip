Summary:	Handles the connections needed for dialup IP links
Name:		dip
Version:	3.3.7o
Release:	%mkrel 36
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


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 3.3.7o-35mdv2011.0
+ Revision: 663778
- mass rebuild

* Wed Feb 02 2011 Funda Wang <fwang@mandriva.org> 3.3.7o-34
+ Revision: 635161
-ldb is not needed
- tighten BR

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 3.3.7o-33mdv2011.0
+ Revision: 604790
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 3.3.7o-32mdv2010.1
+ Revision: 522453
- rebuilt for 2010.1

* Fri Sep 25 2009 Olivier Blin <oblin@mandriva.com> 3.3.7o-31mdv2010.0
+ Revision: 448875
- disable build on mips (from Arnaud Patard)

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 3.3.7o-30mdv2010.0
+ Revision: 413356
- rebuild

* Fri Jan 09 2009 Frederic Crozat <fcrozat@mandriva.com> 3.3.7o-29mdv2009.1
+ Revision: 327461
- Use dialout group, not uucp

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 3.3.7o-28mdv2009.0
+ Revision: 220626
- rebuild

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 3.3.7o-27mdv2008.1
+ Revision: 179960
- fix build
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Sun Mar 18 2007 Oden Eriksson <oeriksson@mandriva.com> 3.3.7o-25mdv2007.1
+ Revision: 145877
- fix dep (gccmakedep)
- Import dip

* Sun Mar 18 2007 Oden Eriksson <oeriksson@mandriva.com> 3.3.7o-25mdv2007.1
- use the %%mrel macro
- bunzip patches

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 3.3.7o-24mdk
- Rebuild

* Sat Jul 10 2004 Christiaan Welvaart <cjw@daneel.dyndns.org> 3.3.7o-23mdk
- fix Patch9 for gcc 3.3+

* Sun Jun 20 2004 Christiaan Welvaart <cjw@daneel.dyndns.org> 3.3.7o-22mdk
- add BuildRequires: db-devel

* Mon Jun 14 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 3.3.7o-21mdk
- fix gcc-3.4 build (P12)
- don't do stuff within parantheses

