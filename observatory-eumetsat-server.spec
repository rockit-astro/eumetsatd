Name:      observatory-eumetsat-server
Version:   1.2.2
Release:   0
Url:       https://github.com/warwick-one-metre/eumetsatd
Summary:   Estimates the IR opacity from the Eumetsat image published by sat24.com
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3, python3-Pyro4, python3-numpy, python3-scipy, python3-pytesseract
Requires:  python3-pillow, python3-warwick-observatory-common
Requires:  tesseract, observatory-log-client, %{?systemd_requires}

%description
Part of the observatory software for the Warwick La Palma telescopes.

Estimates the IR opacity from the Eumetsat image published by sat24.com and
makes the latest measurement available for other services via Pyro.

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
