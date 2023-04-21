%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Handle file archives
Name:		ark
Version:	23.04.0
Release:	1
License:	LGPLv2+
Group:		Graphical desktop/KDE
Url:		http://utils.kde.org/projects/ark
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(bzip2)
BuildRequires:	pkgconfig(QJson)
BuildRequires:	pkgconfig(libarchive)
BuildRequires:	pkgconfig(liblzma)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(shared-mime-info)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5ItemModels)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5ItemModels)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5JobWidgets)
BuildRequires:	cmake(KF5KHtml)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5Pty)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Concurrent)
BuildRequires:	cmake(libzip)
Suggests:	p7zip
Suggests:	unzip

%description
Ark is a program for managing various archive formats within the KDE
environment.

%files -f ark.lang
%{_datadir}/qlogging-categories5/ark.categories
%{_bindir}/ark
%{_libdir}/qt5/plugins/kerfuffle
%{_libdir}/qt5/plugins/kf5/parts/arkpart.so
%{_libdir}/qt5/plugins/kf5/kio_dnd/*.so
%{_libdir}/qt5/plugins/kf5/kfileitemaction/*.so
%{_datadir}/metainfo/org.kde.ark.appdata.xml
%{_datadir}/applications/org.kde.ark.desktop
%{_datadir}/config.kcfg/ark.kcfg
%{_datadir}/icons/*/*/apps/ark.*
%{_mandir}/man1/ark.1*
%{_sysconfdir}/xdg/arkrc
%{_datadir}/kconf_update/ark.upd
%{_datadir}/kconf_update/ark_add_hamburgermenu_to_toolbar.sh

#---------------------------------------------

%define libkerfuffle_major %(echo %{version} |cut -d. -f1)
%define libkerfuffle %mklibname kerfuffle %{libkerfuffle_major}
%define oldlibkerfuffle17 %mklibname kerfuffle 17
%define oldlibkerfuffle %mklibname kerfuffle 18

%package -n %{libkerfuffle}
Summary:	KDE archiving library
Group:		System/Libraries
Obsoletes:	%{oldlibkerfuffle17} < %{EVRD}
Obsoletes:	%{oldlibkerfuffle} < %{EVRD}

%description -n %{libkerfuffle}
%{name} library.

%files -n %{libkerfuffle}
%{_libdir}/libkerfuffle.so.%{libkerfuffle_major}*

#---------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libkerfuffle} = %{EVRD}

%description devel
Files needed to build applications based on %{name}.

%files devel
# (tpg) no files here?

#----------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang ark --with-man --with-html
