%define major 5
%define olddevname %mklibname KF5MailImporter -d
%define devname %mklibname KPim5MailImporter -d

Name: mailimporter
Version:	23.04.3
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	1
Source0: http://download.kde.org/%{ftpdir}/release-service/%{version}/src/%{name}-%{version}.tar.xz
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
BuildRequires: cmake(KF5PimCommonAkonadi)
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt5-assistant
Obsoletes: %{mklibname KF5MailImporter 5} < %{EVRD}
Obsoletes: %{mklibname KF5MailImporterAkonadi 5} < %{EVRD}
Obsoletes: %{mklibname KF5MailImporter} < %{EVRD}
Obsoletes: %{mklibname KF5MailImporterAkonadi} < %{EVRD}

%description
KDE library for importing E-Mail from various sources.

%libpackage KPim5MailImporter %{major}
%libpackage KPim5MailImporterAkonadi %{major}

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{name} = %{EVRD}
Requires: %{mklibname KPim5MailImporter} = %{EVRD}
Requires: %{mklibname KPim5MailImporterAkonadi} = %{EVRD}
%rename %{olddevname}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang libmailimporter

%files -f libmailimporter.lang
%{_datadir}/qlogging-categories5/mailimporter.categories
%{_datadir}/qlogging-categories5/mailimporter.renamecategories

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*.pri
%doc %{_docdir}/qt5/*.{tags,qch}
