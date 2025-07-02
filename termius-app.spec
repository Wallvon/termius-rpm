%global pkgname termius-app
%global pkgver 9.25.1

Summary: Desktop SSH Client
Name: %{pkgname}
Version: %{pkgver}
Release: 1%{?dist}
License: custom
URL: https://termius.com/
Source: https://termius.com/download/linux/Termius.deb
BuildRequires: bsdtar, gtk3, libnotify, nss, libXScrnSaver, libXtst, xdg-utils, at-spi2-core, libuuid, libsecret, libappindicator-gtk3
ExclusiveArch: x86_64

%description
Desktop SSH Client

#-- PREP, BUILD & INSTALL -----------------------------------------------------#
%prep
bsdtar -x -f %{_sourcedir}/Termius.deb -C %{_builddir}

%build
# No build is needed for binary packages

%install
mkdir -p %{buildroot}/opt/Termius

# Extract contents from data.tar.xz
tar -xJf %{_builddir}/data.tar.xz -C %{buildroot}

# Correct permissions for chrome-sandbox
chmod 4755 %{buildroot}/opt/Termius/chrome-sandbox

#-- FILES ---------------------------------------------------------------------#
%files
/opt/Termius/
%{_datadir}/applications/%{pkgname}.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/doc/%{pkgname}/
/etc/cron.daily/termius-app

#-- CHANGELOG -----------------------------------------------------------------#
%changelog