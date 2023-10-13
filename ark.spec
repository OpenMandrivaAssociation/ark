%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Handle file archives
Name:		ark
Version:	23.08.2
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
# There's no point in having a separate libpackage for an application
# specific library that doesn't have headers, so let's stop splitting it
%define libkerfuffle_major %(echo %{version} |cut -d. -f1)
%define libkerfuffle %mklibname kerfuffle %{libkerfuffle_major}
%define oldlibkerfuffle17 %mklibname kerfuffle 17
%define oldlibkerfuffle %mklibname kerfuffle 18
Obsoletes:	%{libkerfuffle} < %{EVRD}
Obsoletes:	%{oldlibkerfuffle17} < %{EVRD}
Obsoletes:	%{oldlibkerfuffle} < %{EVRD}
Obsoletes:	%{name}-devel < %{EVRD}

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
%{_libdir}/libkerfuffle.so.%{libkerfuffle_major}*
%{_datadir}/kservices5/ark_part.desktop

#----------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang ark --with-man --with-html
