import re
import requests
import gzip


def fetch_packages_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return gzip.decompress(response.content).decode('utf-8')
    else:
        raise Exception(f"Failed to fetch Packages file. Status code: {response.status_code}")


def extract_version_from_packages(packages_content, package_name):
    packages = packages_content.split('\n\n')
    for package in packages:
        if f'Package: {package_name}' in package:
            version_line = [line for line in package.split('\n') if line.startswith('Version:')]
            if version_line:
                return version_line[0].split(': ')[1]
    raise Exception(f"Failed to extract version for {package_name} from Packages file.")


def update_spec_file(spec_file_path, version):
    with open(spec_file_path, 'r') as spec_file:
        spec_content = spec_file.read()

    updated_spec_content = re.sub(
        r'%global pkgver \d+\.\d+\.\d+',
        f'%global pkgver {version}',
        spec_content
    )

    with open(spec_file_path, 'w') as spec_file:
        spec_file.write(updated_spec_content)

    print(f"Spec file updated to version {version}")


def main():
    packages_url = "https://deb.termius.com/dists/squeeze/main/binary-amd64/Packages.gz"
    spec_file_path = "../termius-app.spec"
    package_name = "termius-app"

    try:
        packages_content = fetch_packages_content(packages_url)
        version = extract_version_from_packages(packages_content, package_name)
        print(f"The version of {package_name} is: {version}")
        update_spec_file(spec_file_path, version)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
