#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-cu2qu
Version  : 1.6.7.post1
Release  : 1
URL      : https://files.pythonhosted.org/packages/d9/98/139592d4e7fbfe61dfa64dd1fb2a5b2f0a119d8ea3abdf42d46edcddf48d/cu2qu-1.6.7.post1.zip
Source0  : https://files.pythonhosted.org/packages/d9/98/139592d4e7fbfe61dfa64dd1fb2a5b2f0a119d8ea3abdf42d46edcddf48d/cu2qu-1.6.7.post1.zip
Summary  : Cubic-to-quadratic bezier curve conversion
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-cu2qu-bin = %{version}-%{release}
Requires: pypi-cu2qu-license = %{version}-%{release}
Requires: pypi-cu2qu-python = %{version}-%{release}
Requires: pypi-cu2qu-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pypi(cython)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(wheel)
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
cu2qu
=====
This library provides functions which take in UFO objects (Defcon Fonts
or Robofab RFonts) and converts any cubic curves to quadratic. The most
useful function is probably ``fonts_to_quadratic``.

%package bin
Summary: bin components for the pypi-cu2qu package.
Group: Binaries
Requires: pypi-cu2qu-license = %{version}-%{release}

%description bin
bin components for the pypi-cu2qu package.


%package license
Summary: license components for the pypi-cu2qu package.
Group: Default

%description license
license components for the pypi-cu2qu package.


%package python
Summary: python components for the pypi-cu2qu package.
Group: Default
Requires: pypi-cu2qu-python3 = %{version}-%{release}

%description python
python components for the pypi-cu2qu package.


%package python3
Summary: python3 components for the pypi-cu2qu package.
Group: Default
Requires: python3-core
Provides: pypi(cu2qu)
Requires: pypi(fonttools)

%description python3
python3 components for the pypi-cu2qu package.


%prep
%setup -q -n cu2qu-1.6.7.post1
cd %{_builddir}/cu2qu-1.6.7.post1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640195777
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-cu2qu
cp %{_builddir}/cu2qu-1.6.7.post1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-cu2qu/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cu2qu

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-cu2qu/7df059597099bb7dcf25d2a9aedfaf4465f72d8d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
