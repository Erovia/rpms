%define sourcetar bootloadHID.2012-12-08

Name:           bootloadhid
Version:        2012.12.08
Release:        2%{?dist}
Summary:        HID-based USB bootloader for AVR microcontrollers
Packager:       Erovia <https://github.com/Erovia>

License:        GPL-2.0-only OR GPL-3.0-only
URL:            https://www.obdev.at/products/vusb/bootloadhid.html
Source:         https://www.obdev.at/downloads/vusb/%{sourcetar}.tar.gz 
# The provided Makefile overwrites the 'gcc' flags,
# we don't want this to be able to generate the debug packages
Patch:          https://raw.githubusercontent.com/Erovia/rpms/main/%{name}/no-flags.patch

BuildRequires:  gcc
BuildRequires:  pkgconfig(libusb)
BuildRequires:  make

%description
USB boot loader for AVR microcontrollers.

%prep
%setup -q -n %{sourcetar}
%patch 0

%build
cd commandline
%make_build

%install
mkdir -p %{buildroot}/usr/bin
cp %{_builddir}/%{sourcetar}/commandline/bootloadHID %{buildroot}/usr/bin/bootloadHID

%files
%license License.txt
%doc Readme.txt
%{_bindir}/bootloadHID

%changelog
* Sun Mar 3 2024 Erovia <erovia@users.noreply.github.com> - 2012.12.08-2
- Fix debug package generation

* Tue Feb 27 2024 Erovia <erovia@users.noreply.github.com> - 2012.12.08-1
- Package release 2012.12.08

