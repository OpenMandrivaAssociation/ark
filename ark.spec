Summary:	Handle file archives
Name:		ark
Version:	4.11.1
Release:	1
Group:		Graphical desktop/KDE
License:	LGPLv2
Url:		http://utils.kde.org/projects/ark
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	ftp://ftp.kde.org/pub/kde/%{ftpdir}/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdebase4-devel
BuildRequires:	kdelibs4-devel
BuildRequires:	bzip2-devel
BuildRequires:	pkgconfig(QJson)
BuildRequires:	pkgconfig(libarchive)
BuildRequires:	pkgconfig(liblzma)
BuildRequires:	pkgconfig(zlib)
Suggests:	p7zip
Suggests:	unzip

%description
Ark is a program for managing various archive formats within the KDE
environment.

%files
%{_kde_bindir}/ark
%{_kde_libdir}/kde4/kerfuffle_*
%{_kde_libdir}/kde4/arkpart.so
%{_kde_libdir}/kde4/libextracthere.so
%{_kde_applicationsdir}/ark.desktop
%{_kde_appsdir}/ark
%{_kde_datadir}/config.kcfg/ark.kcfg
%{_kde_iconsdir}/hicolor/*/apps/ark*
%{_kde_services}/ark_part.desktop
%{_kde_services}/kerfuffle_*
%{_kde_services}/ark_dndextract.desktop
%{_kde_services}/ServiceMenus/ark_*.desktop
%{_kde_servicetypes}/kerfufflePlugin.desktop
%{_kde_docdir}/HTML/*/ark
%{_kde_mandir}/man1/ark.1.*

#---------------------------------------------

%define libkerfuffle_major 4
%define libkerfuffle %mklibname kerfuffle %{libkerfuffle_major}

%package -n %{libkerfuffle}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkerfuffle}
KDE 4 library.

%files -n %{libkerfuffle}
%{_kde_libdir}/libkerfuffle.so.%{libkerfuffle_major}*

#---------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	kdelibs4-devel
Requires:	%{libkerfuffle} = %{EVRD}

%description devel
Files needed to build applications based on %{name}.

%files devel
%{_kde_libdir}/libkerfuffle.so

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.0-1
- New version 4.11.0

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.0-1
- New version 4.10.0

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.1-1
- New version 4.9.1

* Mon Aug 13 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.0-1
- New version 4.9.0
- Update file list

* Thu Jul 19 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.8.97-1
- New version 4.8.97
- Make better use of KDE path macros
- Convert BuildRequires to pkgconfig style

* Mon Jul 02 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.8.95-1
- New version 4.8.95

* Fri Jun 08 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 4.8.4-1
- update to 4.8.4

* Thu May 10 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 4.8.3-1
- update to 4.8.3

* Sun Mar 11 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 4.8.2-1
- update to 4.8.2

* Sun Mar 11 2012 Arkady L. Shane <arkady.shane@rosalab.ru>
- update to
* Sun Mar 11 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 4.8.1-1
- update to 4.8.1

* Sun Feb 26 2012 Andrey Bondrov <abondrov@mandriva.org> 4.8.0-2
+ Revision: 780808
- Add kdebase-devel and qjson-devel to BuildRequires, update file list

* Thu Jan 19 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.8.0-1
+ Revision: 762440
- New upstream tarball

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.97-1
+ Revision: 758031
- New upstream tarball

* Thu Dec 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.95-1
+ Revision: 744507
- New upstream tarball

* Fri Dec 09 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.90-1
+ Revision: 739343
- New upstream tarball

* Thu Nov 24 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.80-1
+ Revision: 733003
- Import Ark
- Create folder
