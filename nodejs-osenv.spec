%define		pkg	osenv
Summary:	Recursively mkdir, like "mkdir -p"
Name:		nodejs-%{pkg}
Version:	0.0.3
Release:	1
License:	MIT
Group:		Development/Libraries
URL:		https://github.com/isaacs/osenv
Source0:	http://registry.npmjs.org/osenv/-/%{pkg}-%{version}.tgz
# Source0-md5:	f42ac372960369633871ab3550cb43fb
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Recursively mkdir, like "mkdir -p".

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
