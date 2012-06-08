Name:		ark
Summary:	Handle file archives
Version: 4.8.4
Release: 1
Group:		Graphical desktop/KDE
License:	LGPLv2
URL:		http://utils.kde.org/projects/ark
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdebase4-devel >= %{version}
BuildRequires:	qjson-devel
BuildRequires:	kdelibs4-devel >= 2:%{version}
BuildRequires:	libarchive-devel
BuildRequires:	zlib-devel
BuildRequires:	bzip2-devel
BuildRequires:	liblzma-devel

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
%{_kde_datadir}/applications/kde4/ark.desktop
%{_kde_appsdir}/ark
%{_kde_datadir}/config.kcfg/ark.kcfg
%{_kde_datadir}/kde4/services/ark_part.desktop
%{_kde_datadir}/kde4/services/kerfuffle_*
%{_kde_datadir}/kde4/services/ark_dndextract.desktop
%{_kde_datadir}/kde4/servicetypes/kerfufflePlugin.desktop
%{_kde_datadir}/kde4/services/ServiceMenus/ark_*.desktop
%{_kde_docdir}/HTML/*/ark
%{_kde_mandir}/man1/ark.1.*

#---------------------------------------------

%define libkerfuffle %mklibname kerfuffle 4

%package -n %{libkerfuffle}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkerfuffle}
KDE 4 library

%files -n %{libkerfuffle}
%{_kde_libdir}/libkerfuffle.so.*

#---------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	kdelibs4-devel
Requires:	%{libkerfuffle} = %{version}-%{release}

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

