Name:      observatory-eumetsat-server
Version:   2.0.1
Release:   0
Url:       https://github.com/warwick-one-metre/eumetsatd
Summary:   Estimates the IR opacity from the Eumetsat image published by sat24.com
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3, python3-Pyro4, python3-numpy, python3-requests,
Requires:  python3-pillow, python3-warwick-observatory-common
Requires:  observatory-log-client, %{?systemd_requires}

%description
Part of the observatory software for the Warwick La Palma telescopes.

Creates IR and dust maps for the web dashboard and estimates the IR
opacity from EUMETSAT images for other services via Pyro.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}

%{__install} %{_sourcedir}/eumetsatd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/eumetsatd.service %{buildroot}%{_unitdir}

%post
%systemd_post eumetsatd.service

%preun
%systemd_preun eumetsatd.service

%postun
%systemd_postun_with_restart eumetsatd.service

%files
%defattr(0755,root,root,-)
%{_bindir}/eumetsatd
%defattr(0644,root,root,-)
%{_unitdir}/eumetsatd.service

%changelog
