Name:           wb32-dfu-updater
Version:        1.0.0
Release:        1%{?dist}
Summary:        A Device Firmware Update based USB programmer for WB32 chips
Packager:       Erovia <https://github.com/Erovia>

License:        Apache-2.0
URL:            https://github.com/WestberryTech/wb32-dfu-updater
Source:         https://github.com/WestberryTech/%{name}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libusb-1.0) >= 1.0.0
BuildRequires:  cmake

%description
A command-line programmer for downloading and uploading firmware to/from WB32 chips via USB.

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}_cli

%changelog
* Mon Feb 26 2024 Erovia <erovia@users.noreply.github.com> - 1.0.0-1
- Package release 1.0.0
