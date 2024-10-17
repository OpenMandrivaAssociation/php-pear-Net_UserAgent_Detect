%define		_class		Net
%define		_subclass	UserAgent
%define		upstream_name	%{_class}_%{_subclass}_Detect

Name:		php-pear-%{upstream_name}
Version:	2.5.2
Release:	6
Summary:	Determines the Web browser
License:	PHP License
Group:		Development/PHP
URL:		https://pear.php.net/package/Net_UserAgent_Detect/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
The Net_UserAgent object does a number of tests on an HTTP User-Agent
string. The results of these tests are available via methods of the
object. This module is based upon the JavaScript browser detection
code available at
http://www.mozilla.org/docs/web-developer/sniffer/browser_type.html.
This module had many influences from the lib/Browser.php code in
version 1.3 of Horde.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
cd %{upstream_name}-%{version}

pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 2.5.2-4mdv2012.0
+ Revision: 742167
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 2.5.2-3
+ Revision: 679531
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 2.5.2-2mdv2011.0
+ Revision: 613740
- the mass rebuild of 2010.1 packages

* Sun Apr 25 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.5.2-1mdv2010.1
+ Revision: 538754
- update to new version 2.5.2

* Sun Nov 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.5.1-2mdv2010.1
+ Revision: 468725
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Fri Jul 10 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.5.1-1mdv2010.0
+ Revision: 394095
- update to new version 2.5.1

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 2.5.0-2mdv2009.1
+ Revision: 322503
- rebuild

* Sun Oct 12 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.5.0-1mdv2009.1
+ Revision: 292883
- update to new version 2.5.0

* Tue Sep 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.4.0-1mdv2009.0
+ Revision: 279066
- update to new version 2.4.0

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 2.3.0-2mdv2009.0
+ Revision: 237006
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 2.3.0-1mdv2008.1
+ Revision: 136415
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Apr 28 2007 Oden Eriksson <oeriksson@mandriva.com> 2.3.0-1mdv2008.0
+ Revision: 18934
- 2.3.0


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 2.2.0-1mdv2007.0
+ Revision: 82419
- Import php-pear-Net_UserAgent_Detect

* Sat May 20 2006 Oden Eriksson <oeriksson@mandriva.com> 2.2.0-1mdk
- 2.2.0

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 2.1.0-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 2.1.0-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 2.1.0-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 2.1.0-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 2.1.0-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 2.1.0-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 2.1.0-1mdk
- initial Mandriva package (PLD import)

