%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Summary:	Handle file archives
Name:		plasma6-ark
Version:	24.12.3
Release:	%{?git:0.%{git}.}3
License:	LGPLv2+
Group:		Graphical desktop/KDE
Url:		https://utils.kde.org/projects/ark
%if 0%{?git:1}
Source0:	https://invent.kde.org/utilities/ark/-/archive/%{gitbranch}/ark-%{gitbranchd}.tar.bz2#/ark-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/ark-%{version}.tar.xz
%endif
BuildRequires:	pkgconfig(bzip2)
BuildRequires:	pkgconfig(libarchive)
BuildRequires:	pkgconfig(liblzma)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(shared-mime-info)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6ItemModels)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6ItemModels)
BuildRequires:	cmake(KF6FileMetaData)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6JobWidgets)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6Pty)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(libzip)
BuildRequires:	plasma6-xdg-desktop-portal-kde
Suggests:	p7zip
Suggests:	unzip

%description
Ark is a program for managing various archive formats within the KDE
environment.

%files -f ark.lang
%{_datadir}/qlogging-categories6/ark.categories
%{_bindir}/ark
%{_libdir}/qt6/plugins/kerfuffle
%{_libdir}/qt6/plugins/kf6/parts/arkpart.so
%{_libdir}/qt6/plugins/kf6/kio_dnd/*.so
%{_libdir}/qt6/plugins/kf6/kfileitemaction/*.so
%{_datadir}/metainfo/org.kde.ark.appdata.xml
%{_datadir}/applications/org.kde.ark.desktop
%{_datadir}/config.kcfg/ark.kcfg
%{_datadir}/icons/*/*/apps/ark.*
%{_mandir}/man1/ark.1*
%{_sysconfdir}/xdg/arkrc
%{_datadir}/kconf_update/ark.upd
%{_datadir}/kconf_update/ark_add_hamburgermenu_to_toolbar.sh
%{_libdir}/libkerfuffle.so*

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n ark-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DQT_MAJOR_VERSION=6 \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang ark --with-man --with-html
