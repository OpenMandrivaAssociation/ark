%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Handle file archives
Name:		ark
Version:	17.04.2
Release:	1
License:	LGPLv2+
Group:		Graphical desktop/KDE
Url:		http://utils.kde.org/projects/ark
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	bzip2-devel
BuildRequires:	pkgconfig(QJson)
BuildRequires:	pkgconfig(libarchive)
BuildRequires:	pkgconfig(liblzma)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(shared-mime-info)
BuildRequires:	cmake(ECM)
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
Suggests:	p7zip
Suggests:	unzip

%description
Ark is a program for managing various archive formats within the KDE
environment.

%files -f ark.lang
%config %{_sysconfdir}/xdg/ark.categories
%{_bindir}/ark
%{_libdir}/qt5/plugins/kerfuffle
%{_libdir}/qt5/plugins/arkpart.so
%{_libdir}/qt5/plugins/kf5/kio_dnd/*.so
%{_libdir}/qt5/plugins/kf5/kfileitemaction/*.so
%{_datadir}/metainfo/org.kde.ark.appdata.xml
%{_datadir}/applications/org.kde.ark.desktop
%{_datadir}/kservices5/*.desktop
%{_datadir}/kservicetypes5/kerfufflePlugin.desktop
%{_datadir}/kxmlgui5/ark
%{_datadir}/mime/packages/kerfuffle.xml
%{_datadir}/config.kcfg/ark.kcfg
%{_datadir}/icons/*/*/apps/ark.*
%{_mandir}/man1/ark.1*
%lang(ca) %{_mandir}/ca/man1/ark.1*
%lang(de) %{_mandir}/de/man1/ark.1*
%lang(es) %{_mandir}/es/man1/ark.1*
%lang(fr) %{_mandir}/fr/man1/ark.1*
%lang(gl) %{_mandir}/gl/man1/ark.1*
%lang(it) %{_mandir}/it/man1/ark.1*
%lang(nl) %{_mandir}/nl/man1/ark.1*
%lang(pt) %{_mandir}/pt/man1/ark.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/ark.1*
%lang(sr) %{_mandir}/sr/man1/ark.1*
%lang(sv) %{_mandir}/sv/man1/ark.1*
%lang(uk) %{_mandir}/uk/man1/ark.1*
%doc %{_docdir}/HTML/en/ark
%lang(de) %doc %{_docdir}/HTML/de/ark
%lang(es) %doc %{_docdir}/HTML/es/ark
%lang(et) %doc %{_docdir}/HTML/et/ark
%lang(fr) %doc %{_docdir}/HTML/fr/ark
%lang(gl) %doc %{_docdir}/HTML/gl/ark
%lang(it) %doc %{_docdir}/HTML/it/ark
%lang(nl) %doc %{_docdir}/HTML/nl/ark
%lang(pl) %doc %{_docdir}/HTML/pl/ark
%lang(pt) %doc %{_docdir}/HTML/pt/ark
%lang(pt_BR) %doc %{_docdir}/HTML/pt_BR/ark
%lang(ru) %doc %{_docdir}/HTML/ru/ark
%lang(sr) %doc %{_docdir}/HTML/sr/ark
%lang(sv) %doc %{_docdir}/HTML/sv/ark
%lang(uk) %doc %{_docdir}/HTML/uk/ark

#---------------------------------------------

%define libkerfuffle_major 17
%define libkerfuffle %mklibname kerfuffle %{libkerfuffle_major}

%package -n %{libkerfuffle}
Summary:	KDE archiving library
Group:		System/Libraries

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
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang ark
