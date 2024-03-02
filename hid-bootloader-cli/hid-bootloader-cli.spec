Name:           hid-bootloader-cli
Version:        210130
Release:        1%{?dist}
Summary:        LUFA HID Bootloader CLI
Packager:       Erovia <https://github.com/Erovia>

License:        GPL-3.0-only
URL:            https://www.lufa-lib.org
Source:         https://github.com/abcminiuser/lufa/archive/refs/tags/LUFA-%{version}.tar.gz
# The provided Makefile runs 'gcc' with the '-s' argument,
# we don't want this to be able to generate debug packages
Patch:          https://raw.githubusercontent.com/Erovia/rpms/main/hid-bootloader-cli/no-strip.patch

BuildRequires:  gcc
BuildRequires:  pkgconfig(libusb)
BuildRequires:  make

%description
USB boot loader for AVR microcontrollers.

%define source_dir lufa-LUFA-%{version}
%define build_path Bootloaders/HID/HostLoaderApp

%prep
%setup -q -n %{source_dir}
%patch 0

%build
cd %{build_path}
%make_build

%install
mkdir -p %{buildroot}/usr/bin
cp %{_builddir}/%{source_dir}/%{build_path}/hid_bootloader_cli %{buildroot}/usr/bin/

%files
%license %{build_path}/gpl3.txt
%doc README.txt
%{_bindir}/hid_bootloader_cli

%changelog
* Sat Mar 2 2024 Erovia <erovia@users.noreply.github.com> - 210130-1
- Package release 210130

