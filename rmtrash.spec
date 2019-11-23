%define version %{getenv:RMTRASH_VERS}
Name:           rmtrash
Version:        %{version}
Release:        1
Summary:        rmtrash and rmdirtrash

License:        GPL-3.0
URL:            https://github.com/sandrospadaro/rmtrash
Source0:        rmtrash-%{version}.tar.gz
BuildArch:      noarch

Requires: trash-cli

%description
Put files (and directories) in trash using the `trash-put` command in a way that is, otherwise as `trash-put` itself, compatible to GNUs `rm` and `rmdir`

%prep
%setup -q
#%autosetup


%build
#%configure
#%make_build


%install
install -d $RPM_BUILD_ROOT/usr/local/bin
install -m 0755 rmtrash-%{version}/rmtrash $RPM_BUILD_ROOT/usr/local/bin/rmtrash
install -m 0755 rmtrash-%{version}/rmdirtrash $RPM_BUILD_ROOT/usr/local/bin/rmdirtrash
#%make_install

%post

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/usr/local/bin/rmtrash
/usr/local/bin/rmdirtrash
#%license add-license-file-here
#%doc add-docs-here



%changelog
* Sat Nov 23 2019 Sandro Spadaro <sandro.spadaro@gmail.com>
- 
