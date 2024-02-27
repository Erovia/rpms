%define sourcetar bootloadHID.2012-12-08

Name:           bootloadhid
Version:        2012.12.08
Release:        1%{?dist}
Summary:        HID-based USB bootloader for AVR microcontrollers
Packager:       Erovia <https://github.com/Erovia>

License:        GPL-2.0-only OR GPL-3.0-only
URL:            https://www.obdev.at/products/vusb/bootloadhid.html
Source:         https://www.obdev.at/downloads/vusb/%{sourcetar}.tar.gz 

BuildRequires:  gcc
BuildRequires:  pkgconfig(libusb)
BuildRequires:  make

%description
USB boot loader for AVR microcontrollers.

# Disable debug package creation as it fails
%global debug_package %{nil}

%prep
%setup -q -n %{sourcetar}

%build
cd commandline
%make_build

%install
mkdir -p %{buildroot}/usr/bin
cp %{_builddir}/%{sourcetar}/commandline/bootloadHID %{buildroot}/usr/bin/bootloadHID
# As no debug packages are created, the binary is not stripped automatically
strip --strip-unneeded %{buildroot}/usr/bin/bootloadHID

%files
%license License.txt
%doc Readme.txt
%{_bindir}/bootloadHID

%changelog
* Tue Feb 27 2024 Erovia <erovia@users.noreply.github.com> - 2012.12.08-1
- Package release 2012.12.08

