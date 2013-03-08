Summary:	Handle file archives
Name:		ark
Version:	4.10.0
Release:	1
Group:		Graphical desktop/KDE
License:	LGPLv2
Url:		http://utils.kde.org/projects/ark
%define is_beta %(if test `echo %version |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
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
KDE 4 library

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

