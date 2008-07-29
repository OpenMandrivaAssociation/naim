Name:           naim
Version:        0.11.8.3.1
Release:        %mkrel 3
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
%{configure2_5x}
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

