Name:      observatory-eumetsat-server
Version:   20220722
Release:   0
Url:       https://github.com/warwick-one-metre/eumetsatd
Summary:   Estimates the IR opacity from the Eumetsat images
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3 python3-Pyro4 python3-numpy python3-requests
Requires:  python3-pillow python3-warwick-observatory-common

%description

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}

%{__install} %{_sourcedir}/eumetsatd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/eumetsatd.service %{buildroot}%{_unitdir}

%files
%defattr(0755,root,root,-)
%{_bindir}/eumetsatd
%defattr(0644,root,root,-)
%{_unitdir}/eumetsatd.service

%changelog
