#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define major 6
%define devname %mklibname KPim6MailImporter -d

Name: plasma6-mailimporter
Version:	24.12.3
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	%{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/mailimporter/-/archive/%{gitbranch}/mailimporter-%{gitbranchd}.tar.bz2#/mailimporter-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{ftpdir}/release-service/%{version}/src/mailimporter-%{version}.tar.xz
%endif
Summary: KDE library for importing E-Mail from various sources
URL: https://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Qml)
BuildRequires: sasl-devel
BuildRequires: boost-devel
BuildRequires: cmake(KPim6Akonadi)
BuildRequires: cmake(KPim6AkonadiSearch)
BuildRequires: cmake(KPim6AkonadiContactCore)
BuildRequires: cmake(KPim6AkonadiMime)
BuildRequires: cmake(KPim6Mime)
BuildRequires: cmake(KF6JobWidgets)
BuildRequires: cmake(KF6Solid)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(Qt6UiTools)
BuildRequires: cmake(KPim6Libkdepim)
BuildRequires: cmake(KF6CalendarCore)
BuildRequires: cmake(KPim6PimCommonAkonadi)
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt6-qttools-assistant
Obsoletes: %{mklibname KF6MailImporter 6} < %{EVRD}
Obsoletes: %{mklibname KF6MailImporterAkonadi 6} < %{EVRD}
Obsoletes: %{mklibname KF6MailImporter} < %{EVRD}
Obsoletes: %{mklibname KF6MailImporterAkonadi} < %{EVRD}

%description
KDE library for importing E-Mail from various sources.

%libpackage KPim6MailImporter %{major}

%libpackage KPim6MailImporterAkonadi %{major}

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{name} = %{EVRD}
Requires: %{mklibname KPim6MailImporter} = %{EVRD}
Requires: %{mklibname KPim6MailImporterAkonadi} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%autosetup -p1 -n mailimporter-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang libmailimporter6

%files -f libmailimporter6.lang
%{_datadir}/qlogging-categories6/mailimporter.categories
%{_datadir}/qlogging-categories6/mailimporter.renamecategories

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
