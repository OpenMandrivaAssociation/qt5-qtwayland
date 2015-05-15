%define api %(echo %{version} |cut -d. -f1)
%define major %api
%define beta beta

%define qtwaylandclient %mklibname qt%{api}waylandclient %{major}
%define qtwaylandclientd %mklibname qt%{api}waylandclient -d
%define qtwaylandclient_p_d %mklibname qt%{api}waylandclient-private -d

%define qtwaylandcompositor %mklibname qt%{api}waylandcompositor %{major}
%define qtwaylandcompositord %mklibname qt%{api}compositor -d
%define qtwaylandcompositor_p_d %mklibname qt%{api}compositor-private -d

%define qttarballdir qtwayland-opensource-src-%{version}%{?beta:-%{beta}}
%define _qt5_prefix %{_libdir}/qt%{api}
%bcond_without nonegl

Name:		qt5-qtwayland
Version:	5.5.0
%if "%{beta}" != ""
Release:	0.%{beta}.1
Source0:	http://download.qt-project.org/development_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}-%{beta}/submodules/%{qttarballdir}.tar.xz
%else
Release:	1
Source0:	http://download.qt-project.org/official_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}/submodules/%{qttarballdir}.tar.xz
%endif
# (tpg) https://codereview.qt-project.org/#/c/102816/
Patch0:		0001-Move-surfaces-to-outputs.patch
Summary:	Qt5 - Wayland platform support and QtCompositor module
Group:		Development/KDE and Qt
License:	LGPLv2 with exceptions or GPLv3 with exceptions and GFDL
URL:		http://www.qt-project.org
BuildRequires:	qt5-qtbase-devel >= %{version}
BuildRequires:	pkgconfig(Qt5Quick) >= %{version}
BuildRequires:	pkgconfig(Qt5Core) >= %{version}
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5PlatformSupport)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5OpenGL)
BuildRequires:	qt5-qtquick-private-devel

BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(wayland-scanner)
BuildRequires:	pkgconfig(wayland-server)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-cursor)
BuildRequires:	pkgconfig(wayland-egl)
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glesv2)
BuildRequires:	pkgconfig(xcomposite)
BuildRequires:	pkgconfig(xrender)
BuildRequires:	pkgconfig(libudev)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(mtdev)

BuildRequires:	re2c

BuildRequires:	pkgconfig(xtst)
BuildRequires:	pkgconfig(libpci)
BuildRequires:	pkgconfig(nss)

Requires:	%{qtwaylandcompositor} = %{EVRD}
Requires:	%{qtwaylandclient} = %{EVRD}

%description
Qt5 - Wayland platform support and QtCompositor module.

%files
%{_qt5_bindir}/qtwaylandscanner
%{_qt5_plugindir}/platforms/*.so
%{_qt5_plugindir}/wayland-decoration-client
%{_qt5_plugindir}/wayland-graphics-integration-client

#------------------------------------------------------------------------------

%package -n %{qtwaylandclient}
Summary: Qt%{api} Component Library
Group: System/Libraries

%description -n %{qtwaylandclient}
Qt%{api} Component Library.

%files -n %{qtwaylandclient}
%{_qt5_libdir}/libQt5WaylandClient.so.%{major}*

#------------------------------------------------------------------------------

%package -n %{qtwaylandclientd}
Summary: Devel files needed to build apps based on %name
Group:    Development/KDE and Qt
Requires: %{qtwaylandclient} = %version

%description -n %{qtwaylandclientd}
Devel files needed to build apps based on %name

%files -n %{qtwaylandclientd}
%{_qt5_libdir}/libQt5WaylandClient.so
%{_qt5_libdir}/libQt5WaylandClient.prl
%{_qt5_libdir}/pkgconfig/Qt5WaylandClient.pc
%{_qt5_includedir}/QtWaylandClient
%exclude %{_qt5_includedir}/QtWaylandClient/%version
%{_qt5_prefix}/mkspecs/modules/qt_lib_waylandclient.pri
%{_qt5_libdir}/cmake/Qt5WaylandClient
%{_qt5_libdir}/cmake/Qt5Gui/*

#------------------------------------------------------------------------------

%package -n %{qtwaylandclient_p_d}
Summary: Devel files needed to build apps based on %name
Group:    Development/KDE and Qt

Requires: %{qtwaylandclientd} = %version
Provides: qt5-qtwayland-private-devel = %version

%description -n %{qtwaylandclient_p_d}
Devel files needed to build apps based on %name

%files -n %{qtwaylandclient_p_d}
%{_qt5_includedir}/QtWaylandClient/%version
%{_qt5_prefix}/mkspecs/modules/qt_lib_waylandclient_private.pri

#----------------------------------------------------------------------------

%package -n	%{qtwaylandcompositor}
Summary:	Wayland platform QtCompositor module
Group:		System/Libraries

%description -n %{qtwaylandcompositor}
Qt Wayland QtCompositor module

%files -n %{qtwaylandcompositor}
%{_qt5_libdir}/libQt%{api}Compositor.so.%{major}*
%{_qt5_plugindir}/wayland-graphics-integration-server/libdrm-egl-server.so
%{_qt5_plugindir}/wayland-graphics-integration-server/libwayland-egl.so
%{_qt5_plugindir}/wayland-graphics-integration-server/libxcomposite-egl.so
%ifnarch %arm
%{_qt5_plugindir}/wayland-graphics-integration-server/libxcomposite-glx.so
%endif

#----------------------------------------------------------------------------

%package -n %{qtwaylandcompositord}
Summary:	Development files for the Qt Wayland QtCompositor library
Group:		Development/KDE and Qt
Requires:	%{name} = %{EVRD}
Requires:	%{qtwaylandcompositor} = %{EVRD}
Requires:	%{qtwaylandclient} = %{EVRD}
Requires:	%{qtwaylandclientd} = %{EVRD}

%description -n %{qtwaylandcompositord}
Development files for the Qt Wayland QtCompositor module

%files -n %{qtwaylandcompositord}
%{_qt5_includedir}/QtCompositor
%{_qt5_libdir}/libQt%{api}Compositor.so
%exclude %{_qt5_includedir}/QtCompositor/%version
%{_qt5_libdir}/libQt%{api}Compositor.prl
%{_qt5_libdir}/cmake/Qt%{api}Compositor
%{_qt5_libdir}/pkgconfig/Qt%{api}Compositor.pc
%{_qt5_prefix}/mkspecs/modules/qt_lib_compositor.pri
%{_qt5_exampledir}/wayland

#------------------------------------------------------------------------------
%package -n %{qtwaylandcompositor_p_d}
Summary:	Development files for the Qt Wayland QtCompositor library
Group:		Development/KDE and Qt
Requires:	%{qtwaylandcompositord} = %version
Provides:	qt5-qtcompositor-private-devel = %version

%description -n %{qtwaylandcompositor_p_d}
Development files for the Qt Wayland QtCompositor module

%files -n %{qtwaylandcompositor_p_d}
%{_qt5_includedir}/QtCompositor/%version
%{_qt5_prefix}/mkspecs/modules/qt_lib_compositor_private.pri


%prep
%setup -q -c -n %qttarballdir
pushd %qttarballdir
%apply_patches
popd
# Presence of .git/ qmake into invoking syncqt for us with
# correct arguments at make time.
# else, out-of-src-tree builds fail with stuff like:
# qwaylanddisplay_p.h:52:54: fatal error: QtWaylandClient/private/qwayland-wayland.h: No such file or directory
# #include <QtWaylandClient/private/qwayland-wayland.h>
mkdir .git
mv %qttarballdir %qttarballdir-nogl
cp -r %qttarballdir-nogl %qttarballdir-gl

%build
%global optflags %{optflags} -fPIC
%if %{with nonegl}
pushd %qttarballdir-nogl
# build non-egl support
%qmake_qt5 QT_WAYLAND_GL_CONFIG=nogl
%make
popd
%endif

pushd %qttarballdir-gl
%qmake_qt5 CONFIG+=wayland-compositor
%make
popd

#------------------------------------------------------------------------------

%install
%if %{with nonegl}
pushd %qttarballdir-nogl
%makeinstall_std INSTALL_ROOT=%{buildroot}
popd
%endif
pushd %qttarballdir-gl
%makeinstall_std INSTALL_ROOT=%{buildroot}

# install private headers... needed by hawaii shell
install -pm644 \
  include/QtCompositor/%{version}/QtCompositor/private/{wayland-wayland-server-protocol.h,qwayland-server-wayland.h} \
  %{buildroot}%{_includedir}/qt5/QtCompositor/%{version}/QtCompositor/private/
popd

## .prl/.la file love
# nuke .prl reference(s) to %%buildroot, excessive (.la-like) libs
pushd %{buildroot}%{_libdir}
for prl_file in libQt5*.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
    sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
popd
