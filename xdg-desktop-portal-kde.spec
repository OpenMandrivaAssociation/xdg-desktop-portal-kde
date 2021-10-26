%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: xdg-desktop-portal-kde
Version:	5.23.2
Release:	1
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Summary: Backend implementation for xdg-desktop-portal using Qt/KDE
URL: http://kde.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5Wayland)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5Declarative)
BuildRequires: cmake(KF5Kirigami2)
BuildRequires: cmake(KF5Plasma)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Concurrent)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5PrintSupport)
BuildRequires: cmake(Qt5QuickWidgets)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cups-devel
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libpipewire-0.3)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: cmake(PlasmaWaylandProtocols)
BuildRequires: cmake(Qt5WaylandClient)
BuildRequires: qt5-qtwayland
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(epoxy)
Requires: xdg-desktop-portal
Provides: xdg-desktop-portal-implementation

%description
Backend implementation for xdg-desktop-portal using Qt/KDE.

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%{_libdir}/libexec/xdg-desktop-portal-kde
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.kde.service
%{_datadir}/xdg-desktop-portal
%{_datadir}/xdg-desktop-portal-kde
%{_datadir}/applications/org.freedesktop.impl.portal.desktop.kde.desktop
%{_datadir}/knotifications5/xdg-desktop-portal-kde.notifyrc
