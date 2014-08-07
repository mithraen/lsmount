Name: lsmount
Summary: List all hotplug storage devices
Version: 1.0
Release: alt1
License: GPLv2
Group: System/Base
BuildArch: noarch

Packager: Denis Smirnov <mithraen@altlinux.ru>
Source: %name-%version.tar

# Automatically added by buildreq on Fri Aug 08 2014 (-bb)
# optimized out: perl-Term-ANSIColor perl-Text-Aligner python-base
BuildRequires: perl-Text-Table

%description
%summary

%prep
%setup

%install
install -D -m 755 %name %buildroot%_bindir/%name

%files
%_bindir/%name

%changelog
* Fri Aug 08 2014 Denis Smirnov <mithraen@altlinux.ru> 1.0-alt1
- first build