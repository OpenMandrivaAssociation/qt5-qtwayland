%define api %(echo %{version} |cut -d. -f1)
%define major %api
%define beta %{nil}

%define qtwaylandclient %mklibname qt%{api}waylandclient %{major}
%define qtwaylandclientd %mklibname qt%{api}waylandclient -d
%define qtwaylandclient_p_d %mklibname qt%{api}waylandclient-private -d

%define qtwaylandcompositor %mklibname qt%{api}waylandcompositor %{major}
%define qtwaylandcompositord %mklibname qt%{api}compositor -d
%define qtwaylandcompositor_p_d %mklibname qt%{api}compositor-private -d

%define _qt5_prefix %{_libdir}/qt%{api}

Summary:	Qt5 - Wayland platform support and QtCompositor module
Name:		qt5-qtwayland
Version:	5.15.15
%if "%{beta}" != ""
Release:	0.%{beta}.1
%define qttarballdir qtwayland-everywhere-src-%{version}-%{beta}
Source0:	http://download.qt.io/development_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}-%{beta}/submodules/%{qttarballdir}.tar.xz
%else
Release:	1
%define qttarballdir qtwayland-everywhere-opensource-src-%{version}
Source0:	http://download.qt.io/official_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}/submodules/%{qttarballdir}.tar.xz
%endif
Group:		Development/KDE and Qt
License:	LGPLv2 with exceptions or GPLv3 with exceptions and GFDL
URL:		https://www.qt.io
Patch0:		qtwayland-5.14-GL-headers.patch

# From KDE https://invent.kde.org/qt/qt/qtwayland -b kde/5.15
%(P=1001; cd %{_sourcedir}; for i in [0-9][0-9][0-9][0-9]-*.patch; do echo -e "Patch$P:\t$i"; P=$((P+1)); done)

BuildRequires:	qmake5 >= %{version}
BuildRequires:	pkgconfig(Qt5Quick) >= %{version}
BuildRequires:	pkgconfig(Qt5Core) >= %{version}
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5OpenGL)
BuildRequires:	cmake(Qt5GlxSupport)
BuildRequires:	cmake(Qt5VulkanSupport)
BuildRequires:	qt5-qtquick-private-devel
BuildRequires:	qt5-qtqmlmodels-private-devel
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(wayland-scanner) >= 1.10.0
BuildRequires:	pkgconfig(wayland-server)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-cursor)
BuildRequires:	pkgconfig(wayland-egl)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glesv2)
BuildRequires:	pkgconfig(xcomposite)
BuildRequires:	pkgconfig(xrender)
BuildRequires:	pkgconfig(libudev)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(mtdev)
BuildRequires:	pkgconfig(libinput)
BuildRequires:	re2c
BuildRequires:	pkgconfig(xtst)
BuildRequires:	pkgconfig(libpci)
BuildRequires:	pkgconfig(nss)
# (tpg) needed for QtServiceSupport/private/qgenericunixservices_p.h
BuildRequires:	%{_lib}qt5servicesupport-static-devel
# (tpg) needed for QtFontDatabaseSupport/private/qgenericunixfontdatabase_p.h
BuildRequires:	%{_lib}qt5fontdatabasesupport-static-devel
BuildRequires:	%{_lib}qt5themesupport-static-devel
BuildRequires:	%{_lib}qt5eventdispatchersupport-static-devel
BuildRequires:	%{_lib}qt5eglsupport-static-devel
%ifnarch %{arm}
# Needed if and only if Qt is build with desktop OpenGL
BuildRequires:	%{_lib}qt5glxsupport-static-devel
%endif
# Required bit is libQt5XkbCommonSupport.a -- maybe that should move
# to a separate package given it doesn't seem as X[kb] specific as the
# name implies.
BuildRequires:	%{_lib}qt5gui5-x11-devel
BuildRequires:	%{_lib}qt5linuxaccessibilitysupport-static-devel
BuildRequires:	pkgconfig(Qt5LinuxAccessibilitySupport)
# For drm_fourcc.h
BuildRequires:	kernel-headers
BuildRequires:	pkgconfig(libdrm)
# For the Provides: generator
BuildRequires:	cmake >= 3.11.0-1
Requires:	%{qtwaylandcompositor} = %{EVRD}
Requires:	%{qtwaylandclient} = %{EVRD}

%description
Qt5 - Wayland platform support and QtCompositor module.

%files
%{_qt5_bindir}/qtwaylandscanner
%{_qt5_plugindir}/platforms/*.so
%{_qt5_plugindir}/wayland-decoration-client
%{_qt5_plugindir}/wayland-graphics-integration-client
%dir %{_qt5_plugindir}/wayland-graphics-integration-server
%{_qt5_plugindir}/wayland-shell-integration
%{_libdir}/qt5/qml/QtWayland

#------------------------------------------------------------------------------

%package -n %{qtwaylandclient}
Summary:	Qt%{api} Component Library
Group:		System/Libraries

%description -n %{qtwaylandclient}
Qt%{api} Component Library.

%files -n %{qtwaylandclient}
%{_qt5_libdir}/libQt5WaylandClient.so.%{major}*

#------------------------------------------------------------------------------

%package -n %{qtwaylandclientd}
Summary:	Devel files needed to build apps based on %{name}
Group:		Development/KDE and Qt
Requires:	%{name} = %{EVRD}
Requires:	%{qtwaylandclient} = %{EVRD}

%description -n %{qtwaylandclientd}
Devel files needed to build apps based on %{name}.

%files -n %{qtwaylandclientd}
%{_qt5_libdir}/libQt5WaylandClient.so
%{_qt5_libdir}/libQt5WaylandClient.prl
%{_qt5_libdir}/pkgconfig/Qt5WaylandClient.pc
%{_qt5_includedir}/QtWaylandClient
%exclude %{_qt5_includedir}/QtWaylandClient/%{version}
%{_qt5_prefix}/mkspecs/modules/qt_lib_waylandclient.pri
%{_qt5_libdir}/cmake/Qt5WaylandClient
%{_qt5_libdir}/cmake/Qt5Gui/*

#------------------------------------------------------------------------------

%package -n %{qtwaylandclient_p_d}
Summary:	Devel files needed to build apps based on %{name}
Group:		Development/KDE and Qt

Requires:	%{qtwaylandclientd} = %{EVRD}
Provides:	qt5-qtwayland-private-devel = %{EVRD}

%description -n %{qtwaylandclient_p_d}
Devel files needed to build apps based on %{name}.

%files -n %{qtwaylandclient_p_d}
%{_qt5_includedir}/QtWaylandClient/%{version}
%{_qt5_prefix}/mkspecs/modules/qt_lib_waylandclient_private.pri

#----------------------------------------------------------------------------

%package -n %{qtwaylandcompositor}
Summary:	Wayland platform QtCompositor module
Group:		System/Libraries

%description -n %{qtwaylandcompositor}
Qt Wayland QtCompositor module.

%files -n %{qtwaylandcompositor}
%{_qt5_libdir}/libQt%{api}WaylandCompositor.so.%{major}*
%optional %{_libdir}/qt5/plugins/wayland-graphics-integration-server/libqt-wayland-compositor-dmabuf-server-buffer.so
%optional %{_libdir}/qt5/plugins/wayland-graphics-integration-server/libqt-wayland-compositor-linux-dmabuf-unstable-v1.so
%{_libdir}/qt5/plugins/wayland-graphics-integration-server/libqt-wayland-compositor-drm-egl-server-buffer.so
%{_libdir}/qt5/plugins/wayland-graphics-integration-server/libqt-wayland-compositor-shm-emulation-server.so
%{_libdir}/qt5/plugins/wayland-graphics-integration-server/libqt-wayland-compositor-vulkan-server.so
%{_libdir}/qt5/plugins/wayland-graphics-integration-server/libqt-wayland-compositor-wayland-egl.so
%{_libdir}/qt5/plugins/wayland-graphics-integration-server/libqt-wayland-compositor-wayland-eglstream-controller.so
%{_libdir}/qt5/plugins/wayland-graphics-integration-server/libqt-wayland-compositor-xcomposite-egl.so
# Built if and only if Qt uses desktop OpenGL rather than OpenGL ES
%optional %{_libdir}/qt5/plugins/wayland-graphics-integration-server/libqt-wayland-compositor-xcomposite-glx.so

#----------------------------------------------------------------------------

%package -n %{qtwaylandcompositord}
Summary:	Development files for the Qt Wayland QtCompositor library
Group:		Development/KDE and Qt
Requires:	%{name} = %{EVRD}
Requires:	%{qtwaylandcompositor} = %{EVRD}
Requires:	%{qtwaylandclient} = %{EVRD}
Requires:	%{qtwaylandclientd} = %{EVRD}

%description -n %{qtwaylandcompositord}
Development files for the Qt Wayland QtCompositor module.

%files -n %{qtwaylandcompositord}
%{_qt5_includedir}/QtWaylandCompositor
%{_qt5_libdir}/libQt%{api}WaylandCompositor.so
%exclude %{_qt5_includedir}/QtWaylandCompositor/%{version}
%{_qt5_libdir}/libQt%{api}WaylandCompositor.prl
%{_qt5_libdir}/cmake/Qt%{api}WaylandCompositor
%{_qt5_libdir}/pkgconfig/Qt%{api}WaylandCompositor.pc
%{_qt5_prefix}/mkspecs/modules/qt_lib_waylandcompositor.pri
%{_qt5_exampledir}/wayland

#------------------------------------------------------------------------------
%package -n %{qtwaylandcompositor_p_d}
Summary:	Development files for the Qt Wayland QtCompositor library
Group:		Development/KDE and Qt
Requires:	%{qtwaylandcompositord} = %{EVRD}
Provides:	qt5-qtcompositor-private-devel = %{EVRD}

%description -n %{qtwaylandcompositor_p_d}
Development files for the Qt Wayland QtCompositor module.

%files -n %{qtwaylandcompositor_p_d}
%{_qt5_includedir}/QtWaylandCompositor/%{version}
%{_qt5_prefix}/mkspecs/modules/qt_lib_waylandcompositor_private.pri

%prep
%autosetup -n %(echo %{qttarballdir}|sed -e 's,-opensource,,') -p1
%{_qt5_prefix}/bin/syncqt.pl -version %{version}

%build
%global optflags %{optflags} -O3 -fPIC
%qmake_qt5 CONFIG+=generated_headers
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

## .prl/.la file love
# nuke .prl reference(s) to %%buildroot, excessive (.la-like) libs
cd %{buildroot}%{_libdir}
for prl_file in libQt5*.prl ; do
    sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
    if [ -f "$(basename ${prl_file} .prl).so" ]; then
	rm -fv "$(basename ${prl_file} .prl).la"
	sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
    fi
done
cd -
