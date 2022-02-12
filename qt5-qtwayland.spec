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
Version:	5.15.3
%if "%{beta}" != ""
Release:	0.%{beta}.1
%define qttarballdir qtwayland-everywhere-src-%{version}-%{beta}
Source0:	http://download.qt.io/development_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}-%{beta}/submodules/%{qttarballdir}.tar.xz
%else
Release:	7
%define qttarballdir qtwayland-everywhere-src-5.15.2
Source0:	http://download.qt.io/official_releases/qt/%(echo %{version}|cut -d. -f1-2)/5.15.2/submodules/%{qttarballdir}.tar.xz
%endif
Group:		Development/KDE and Qt
License:	LGPLv2 with exceptions or GPLv3 with exceptions and GFDL
URL:		http://www.qt.io
Patch0:		qtwayland-5.14-GL-headers.patch

# From KDE https://invent.kde.org/qt/qt/qtwayland -b kde/5.15
Patch1000:	0001-Bump-version.patch
Patch1001:	0002-Scanner-Avoid-accessing-dangling-pointers-in-destroy.patch
Patch1002:	0003-Make-setting-QT_SCALE_FACTOR-work-on-Wayland.patch
Patch1003:	0004-Do-not-try-to-eglMakeCurrent-for-unintended-case.patch
Patch1004:	0005-Make-setting-QT_SCALE_FACTOR-work-on-Wayland.patch
Patch1005:	0006-Ensure-that-grabbing-is-performed-in-correct-context.patch
Patch1006:	0007-Fix-leaked-subsurface-wayland-items.patch
Patch1007:	0008-Use-qWarning-and-_exit-instead-of-qFatal-for-wayland.patch
Patch1008:	0009-Fix-memory-leak-in-QWaylandGLContext.patch
Patch1009:	0010-Client-Send-set_window_geometry-only-once-configured.patch
Patch1010:	0011-Translate-opaque-area-with-frame-margins.patch
Patch1011:	0012-Client-Send-exposeEvent-to-parent-on-subsurface-posi.patch
Patch1012:	0013-Get-correct-decoration-margins-region.patch
Patch1013:	0014-xdgshell-Tell-the-compositor-the-screen-we-re-expect.patch
Patch1014:	0015-Fix-compilation.patch
Patch1015:	0016-client-Allow-QWaylandInputContext-to-accept-composed.patch
Patch1016:	0017-Client-Announce-an-output-after-receiving-more-compl.patch
Patch1017:	0018-Fix-issue-with-repeated-window-size-changes.patch
Patch1018:	0019-Include-locale.h-for-setlocale-LC_CTYPE.patch
Patch1019:	0020-Client-Connect-drags-being-accepted-to-updating-the-.patch
Patch1020:	0021-Client-Disconnect-registry-listener-on-destruction.patch
Patch1021:	0022-Client-Set-XdgShell-size-hints-before-the-first-comm.patch
Patch1022:	0023-Fix-build.patch
Patch1023:	0024-Fix-remove-listener.patch
Patch1024:	0025-Hook-up-queryKeyboardModifers.patch
Patch1025:	0026-Do-not-update-the-mask-if-we-do-not-have-a-surface.patch
Patch1026:	0027-Correctly-detect-if-image-format-is-supported-by-QIm.patch
Patch1027:	0028-Wayland-client-Fix-crash-when-windows-are-shown-hidd.patch
Patch1028:	0029-Client-Don-t-always-recreate-frame-callbacks.patch
Patch1029:	0030-Client-Always-destroy-frame-callback-in-the-actual-c.patch
Patch1030:	0031-Fix-the-logic-for-decoding-modifiers-map-in-Wayland-.patch
Patch1031:	0032-Wayland-client-use-wl_keyboard-to-determine-active-s.patch
Patch1032:	0033-Client-do-not-empty-clipboard-when-a-new-popup-windo.patch
Patch1033:	0034-Fix-backport-context-destruction-was-omitted.patch
Patch1034:	0035-Set-preedit-cursor-when-cursor-equals-to-0.patch
Patch1035:	0036-Client-Implement-DataDeviceV3.patch
Patch1036:	0037-Client-Delay-deletion-of-QDrag-object-until-after-we.patch
Patch1037:	0038-Client-Avoid-processing-of-events-when-showing-windo.patch
Patch1038:	0039-Handle-registry_global-out-of-constructor.patch
Patch1039:	0040-Connect-flushRequest-after-forceRoundTrip.patch
Patch1040:	0041-Move-the-wayland-socket-polling-to-a-separate-event-.patch
Patch1041:	0042-Check-pointer-for-null-before-use-in-ASSERT.patch
Patch1042:	0043-Do-not-create-decorations-when-the-shellSurface-is-n.patch
Patch1043:	0044-Use-wl_surface.damage_buffer-on-the-client-side.patch
Patch1044:	0045-Fix-crash-if-no-input-method-module-could-be-loaded.patch
Patch1045:	0046-Client-Remove-mWaitingForUpdateDelivery.patch

BuildRequires:	qmake5 >= %{version}
BuildRequires:	pkgconfig(Qt5Quick) >= %{version}
BuildRequires:	pkgconfig(Qt5Core) >= %{version}
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5OpenGL)
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
%ifnarch %{arm} %{aarch64}
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
BuildRequires:	kernel-release-headers
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
%autosetup -n %{qttarballdir} -p1
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
