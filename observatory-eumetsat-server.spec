Name:      observatory-eumetsat-server
Version:   1.0.0
Release:   0
Url:       https://github.com/warwick-one-metre/eumetsatd
Summary:   Estimates the IR opacity from the Eumetsat image published by sat24.com
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python34, python34-Pyro4, python34-numpy, python34-scipy, python34-pytesseract, tesseract, python34-warwick-observatory-common, observatory-log-client, %{?systemd_requires}

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
