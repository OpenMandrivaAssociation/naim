Name:           naim
Version:        0.11.8.3.2
Release:        3
Epoch:          0
Summary:        An ncurses-based console AIM, ICQ, IRC, and Lily client
Group:          Networking/Instant messaging
License:        GPLv2
URL:            http://naim.n.ml.org/
Source0:        http://naim.googlecode.com/files/naim-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel gawk

%description
naim is a console client for AOL Instant Messenger (AIM), AOL I Seek You (ICQ),
Internet Relay Chat (IRC), and The lily CMC.

%prep
%setup -q

%build
%configure2_5x
%{__make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}
%{__rm} -r %{buildroot}%{_docdir}/%{name}
%{__rm} -r %{buildroot}%{_includedir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc AUTHORS FAQ BUGS README NEWS ChangeLog doc/*.hlp
%attr(0755,root,root) %{_bindir}/extractbuddy.sh
%attr(0755,root,root) %{_bindir}/naim
%attr(0755,root,root) %{_bindir}/nicq
%attr(0755,root,root) %{_bindir}/nirc
%attr(0755,root,root) %{_bindir}/nlily
%{_mandir}/man1/naim.1*
%{_mandir}/man1/nicq.1*
%{_mandir}/man1/nirc.1*
%{_mandir}/man1/nlily.1*



%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 0:0.11.8.3.2-2mdv2011.0
+ Revision: 612988
- the mass rebuild of 2010.1 packages

* Tue Mar 02 2010 Sandro Cazzaniga <kharec@mandriva.org> 0:0.11.8.3.2-1mdv2010.1
+ Revision: 513636
- update to naim-0.11.8.3.2

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0:0.11.8.3.1-4mdv2010.0
+ Revision: 430151
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 0:0.11.8.3.1-3mdv2009.0
+ Revision: 253563
- rebuild

* Thu Jan 03 2008 David Walluck <walluck@mandriva.org> 0:0.11.8.3.1-1mdv2008.1
+ Revision: 143559
- import naim


