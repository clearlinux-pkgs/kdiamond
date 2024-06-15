#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v12
# autospec commit: fbcebd0
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kdiamond
Version  : 24.05.1
Release  : 73
URL      : https://download.kde.org/stable/release-service/24.05.1/src/kdiamond-24.05.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.05.1/src/kdiamond-24.05.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.05.1/src/kdiamond-24.05.1.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GFDL-1.2 GPL-2.0
Requires: kdiamond-bin = %{version}-%{release}
Requires: kdiamond-data = %{version}-%{release}
Requires: kdiamond-license = %{version}-%{release}
Requires: kdiamond-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kcrash-dev
BuildRequires : kdbusaddons-dev
BuildRequires : ki18n-dev
BuildRequires : knotifications-dev
BuildRequires : knotifyconfig-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package bin
Summary: bin components for the kdiamond package.
Group: Binaries
Requires: kdiamond-data = %{version}-%{release}
Requires: kdiamond-license = %{version}-%{release}

%description bin
bin components for the kdiamond package.


%package data
Summary: data components for the kdiamond package.
Group: Data

%description data
data components for the kdiamond package.


%package doc
Summary: doc components for the kdiamond package.
Group: Documentation

%description doc
doc components for the kdiamond package.


%package license
Summary: license components for the kdiamond package.
Group: Default

%description license
license components for the kdiamond package.


%package locales
Summary: locales components for the kdiamond package.
Group: Default

%description locales
locales components for the kdiamond package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n kdiamond-24.05.1
cd %{_builddir}/kdiamond-24.05.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1718416954
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1718416954
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdiamond
cp %{_builddir}/kdiamond-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kdiamond/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/kdiamond-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kdiamond/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kdiamond-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kdiamond/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/kdiamond-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/kdiamond/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/kdiamond-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kdiamond/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kdiamond
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kdiamond
/usr/bin/kdiamond

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kdiamond.desktop
/usr/share/icons/hicolor/128x128/apps/kdiamond.png
/usr/share/icons/hicolor/16x16/apps/kdiamond.png
/usr/share/icons/hicolor/22x22/apps/kdiamond.png
/usr/share/icons/hicolor/32x32/apps/kdiamond.png
/usr/share/icons/hicolor/48x48/apps/kdiamond.png
/usr/share/icons/hicolor/64x64/apps/kdiamond.png
/usr/share/kdiamond/kdiamond.kcfg
/usr/share/kdiamond/themes/default.desktop
/usr/share/kdiamond/themes/diamonds.desktop
/usr/share/kdiamond/themes/diamonds.png
/usr/share/kdiamond/themes/diamonds.svgz
/usr/share/kdiamond/themes/egyptian.svgz
/usr/share/kdiamond/themes/egyptian_preview.png
/usr/share/kdiamond/themes/funny_zoo.desktop
/usr/share/kdiamond/themes/funny_zoo.png
/usr/share/kdiamond/themes/funny_zoo.svgz
/usr/share/knotifications6/kdiamond.notifyrc
/usr/share/knsrcfiles/kdiamond.knsrc
/usr/share/metainfo/org.kde.kdiamond.appdata.xml
/usr/share/sounds/KDiamond-Stone-Drop.ogg
/usr/share/sounds/KDiamond-Stone-Swap.ogg
/usr/share/sounds/KDiamond-Stone-Touch.ogg

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kdiamond/index.cache.bz2
/usr/share/doc/HTML/ca/kdiamond/index.docbook
/usr/share/doc/HTML/de/kdiamond/index.cache.bz2
/usr/share/doc/HTML/de/kdiamond/index.docbook
/usr/share/doc/HTML/en/kdiamond/gameboard.png
/usr/share/doc/HTML/en/kdiamond/index.cache.bz2
/usr/share/doc/HTML/en/kdiamond/index.docbook
/usr/share/doc/HTML/es/kdiamond/index.cache.bz2
/usr/share/doc/HTML/es/kdiamond/index.docbook
/usr/share/doc/HTML/et/kdiamond/index.cache.bz2
/usr/share/doc/HTML/et/kdiamond/index.docbook
/usr/share/doc/HTML/fr/kdiamond/index.cache.bz2
/usr/share/doc/HTML/fr/kdiamond/index.docbook
/usr/share/doc/HTML/it/kdiamond/index.cache.bz2
/usr/share/doc/HTML/it/kdiamond/index.docbook
/usr/share/doc/HTML/lt/kdiamond/index.cache.bz2
/usr/share/doc/HTML/lt/kdiamond/index.docbook
/usr/share/doc/HTML/nl/kdiamond/index.cache.bz2
/usr/share/doc/HTML/nl/kdiamond/index.docbook
/usr/share/doc/HTML/pl/kdiamond/index.cache.bz2
/usr/share/doc/HTML/pl/kdiamond/index.docbook
/usr/share/doc/HTML/pt/kdiamond/index.cache.bz2
/usr/share/doc/HTML/pt/kdiamond/index.docbook
/usr/share/doc/HTML/pt_BR/kdiamond/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kdiamond/index.docbook
/usr/share/doc/HTML/sv/kdiamond/index.cache.bz2
/usr/share/doc/HTML/sv/kdiamond/index.docbook
/usr/share/doc/HTML/uk/kdiamond/gameboard.png
/usr/share/doc/HTML/uk/kdiamond/index.cache.bz2
/usr/share/doc/HTML/uk/kdiamond/index.docbook

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdiamond/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/kdiamond/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/kdiamond/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/kdiamond/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kdiamond/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c

%files locales -f kdiamond.lang
%defattr(-,root,root,-)

