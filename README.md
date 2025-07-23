# termius-rpm

Unofficial port of [Termius](https://termius.com/) for [Fedora](https://fedoraproject.org/).

## Building instructions
1. Clone the repo, and cd into the directory
```bash
git clone https://github.com/Wallvon/termius-rpm
cd termius-rpm
```

2. Install the build dependencies
```bash
sudo dnf install -y rpmdevtools rpm-build rpm-devel rpmlint bsdtar libXScrnSaver libappindicator-gtk3
```

3. Set up development build tree, download Termius deb to it and build the package.
```bash
rpmdev-setuptree
spectool -g -R termius-app.spec
rpmbuild --target x86_64 -bb termius-app.spec
```

4. Install the package. It may be called something else depending on your distribution.
```bash
sudo rpm -i ~/rpmbuild/RPMS/x86_64/termius-app-8.6.0-1.fc39.x86_64.rpm
```

## Why is this not on Fedora Copr?
I will not be distributing this on [Fedora Copr](https://copr.fedorainfracloud.org/) or other similar sites because I do not have permission to do so.

I contacted Termius Support on November 15, 2023 and got the following reply back on December 5, 2023:
```
Hi Robert,

Thank you for reaching out to clarify. We are looking into it. We will do it ourselves shortly.

Best regards,
[REDACTED]
The Termius Team
```

So they might be releasing a native RPM package in the near future.