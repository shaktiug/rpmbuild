Name:           sample
Version:        1
Release:        1%{?dist}
Summary:        HI this is only a example for build rpms
BuildArch:      noarch

Group:		Develpment/Tools
License:        GPL
URL:            http://localhost
Source0:        /root/rpmbuild/SOURCES/sample-1.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


%description
This is a test script base rpm

%prep
%setup -q

%install
mkdir -p "$RPM_BUILD_ROOT/opt"
cp -R * "$RPM_BUILD_ROOT/opt"

%files
/opt/

%clean
rm -rf $RPM_BUILD_ROOT

%post
chown -R shakti:shakti /opt/hello.sh
chmod -R 775 /opt/






