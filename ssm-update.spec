%define debug_package %{nil}

%global provider        github
%global provider_tld	com
%global project         shatteredsilicon
%global repo            ssm-update
%global provider_prefix	%{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path	%{provider_prefix}

Name:		%{repo}
Version:	%{_version}
Release:	1%{?dist}
Summary:	Tool for updating packages and OS configuration for SSM Server

License:	AGPLv3
URL:		https://%{provider_prefix}
Source0:	%{name}-%{version}.tar.gz

Requires:	(PyYAML or python3-pyyaml)


%description
%{summary}


%prep
%setup -q -n %{name}


%build


%install
install -d %{buildroot}%{_bindir}
cp -pav ./bin/* %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/%{name}
cp -pav ./ansible %{buildroot}%{_datadir}/%{name}
cp -pav ./helpers %{buildroot}%{_datadir}/%{name}


%files
%license LICENSE
%doc README.md
%{_bindir}/*
%{_datadir}/%{name}


%changelog
* Fri Jun 30 2017 Mykola Marzhan <mykola.marzhan@percona.com> - 1.1.6-1
- move repository from Percona-Lab to percona organization

* Mon Feb 13 2017 Mykola Marzhan <mykola.marzhan@percona.com> - 1.1.0-2
- add ansible dir to %{_datadir}/%{name}

* Tue Feb  7 2017 Mykola Marzhan <mykola.marzhan@percona.com> - 1.1.0-1
- init version
