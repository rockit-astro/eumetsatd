Name:      observatory-eumetsat-client
Version:   1.1.0
Release:   0
Url:       https://github.com/warwick-one-metre/eumetsatd
Summary:   EUMETSAT client for the Warwick La Palma telescopes
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python36, python36-Pyro4, python36-warwick-observatory-common

%description
Part of the observatory software for the Warwick La Palma telescopes.

eumetsat is a commandline utility that queries the EUMETSAT IR opacity daemon.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}/etc/bash_completion.d
%{__install} %{_sourcedir}/eumetsat %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/completion/eumetsat %{buildroot}/etc/bash_completion.d/eumetsat

%files
%defattr(0755,root,root,-)
%{_bindir}/eumetsat
/etc/bash_completion.d/eumetsat

%changelog
