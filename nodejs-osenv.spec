%define		pkg	osenv
Summary:	Look up environment settings specific to different operating systems
Name:		nodejs-%{pkg}
Version:	0.1.0
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	http://registry.npmjs.org/osenv/-/%{pkg}-%{version}.tgz
# Source0-md5:	91aa897b4cd6d64aa19d6c4ee4ede70a
URL:		https://github.com/isaacs/osenv
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Look up environment settings specific to different operating systems.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -pr *.js package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{nodejs_libdir}/%{pkg}
