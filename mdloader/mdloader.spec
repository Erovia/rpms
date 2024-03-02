Name:           mdloader
Version:        1.0.7
Release:        1%{?dist}
Summary:        Massdrop Firmware Loader
Packager:       Erovia <https://github.com/Erovia>

License:        GPL-3.0-only
URL:            https://github.com/Massdrop/mdloader
Source:         https://github.com/Massdrop/%{name}/archive/refs/tags/%{version}.tar.gz
# The provided Makefile overwrites the 'gcc' flags,
# we don't want this to be able to generate the debug packages
Patch:          https://raw.githubusercontent.com/Erovia/rpms/main/%{name}/no-flags.patch

BuildRequires:  gcc
BuildRequires:  make

%description
Massdrop Firmware Loader - for CTRL / ALT / SHIFT / Rocketeer keyboards

%prep
%autosetup

%build
%make_build

%install
mkdir -p %{buildroot}/usr/bin
cp build/mdloader %{buildroot}/usr/bin/mdloader

%files
%license LICENSE
%doc README.md
%{_bindir}/mdloader

%changelog
* Sat Mar 2 2024 Erovia <erovia@users.noreply.github.com> - 1.0.7-1
- Package release 1.0.7

