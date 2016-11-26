%define major 5
%define devname %mklibname KF5MailImporter -d

Name: mailimporter
Version:	16.08.3
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	1
Source0: http://download.kde.org/%{ftpdir}/applications/%{version}/src/%{name}-%{version}.tar.xz
Summary: KDE library for importing E-Mail from various sources
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5Qml)
BuildRequires: sasl-devel
BuildRequires: boost-devel
BuildRequires: cmake(KF5Akonadi)
BuildRequires: cmake(KF5AkonadiSearch)
BuildRequires: cmake(KF5AkonadiContact)
BuildRequires: cmake(KF5AkonadiMime)
BuildRequires: cmake(KF5Mime)
BuildRequires: cmake(KF5JobWidgets)
BuildRequires: cmake(KF5Solid)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5Archive)
BuildRequires: cmake(KF5KDELibs4Support)
BuildRequires: cmake(Qt5UiTools)
BuildRequires: cmake(KF5Libkdepim)
BuildRequires: cmake(KF5CalendarCore)

%description
KDE library for importing E-Mail from various sources.

%libpackage KF5MailImporter %{major}

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{name} = %{EVRD}
Requires: %{mklibname KF5MailImporter %{major}} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%apply_patches
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files
%{_sysconfdir}/xdg/mailimporter.categories

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*.pri
