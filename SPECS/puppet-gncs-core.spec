Name:           puppet
Version:        0.1
Release:        1%{?dist}
Summary:        This contains httpd,tomcat6,ntp and ssh manifests for PUPPET
BuildArch:      noarch

Group:		Develpment/Tools
License:        GPL
URL:            http://localhost//
Source0:        puppet-gncs-core.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-buildroot


%description
This contains httpd,tomcat6,ntp and ssh manifests for PUPPET. 
Created by Mr. Shakti Singh and Mr. Prem Patel

%prep
%setup -q

%install
mkdir -p "$RPM_BUILD_ROOT/opt/puppet-0.1/"
cp -R * "$RPM_BUILD_ROOT/opt/puppet-0.1/"

%files
/opt/

%clean
rm -rf $RPM_BUILD_ROOT

%post
chown -R root:root /opt/puppet-0.1/
chmod -R 775 /opt/puppet-0.1/






