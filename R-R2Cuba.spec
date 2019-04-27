#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-R2Cuba
Version  : 1.1.0
Release  : 17
URL      : https://cran.r-project.org/src/contrib/Archive/R2Cuba/R2Cuba_1.1-0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/Archive/R2Cuba/R2Cuba_1.1-0.tar.gz
Summary  : Multidimensional Numerical Integration
Group    : Development/Tools
License  : GPL-3.0
Requires: R-R2Cuba-lib = %{version}-%{release}
BuildRequires : R-mvtnorm
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-R2Cuba package.
Group: Libraries

%description lib
lib components for the R-R2Cuba package.


%prep
%setup -q -c -n R2Cuba

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552794451

%install
export SOURCE_DATE_EPOCH=1552794451
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library R2Cuba
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library R2Cuba
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library R2Cuba
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  R2Cuba || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/R2Cuba/DESCRIPTION
/usr/lib64/R/library/R2Cuba/INDEX
/usr/lib64/R/library/R2Cuba/Meta/Rd.rds
/usr/lib64/R/library/R2Cuba/Meta/demo.rds
/usr/lib64/R/library/R2Cuba/Meta/features.rds
/usr/lib64/R/library/R2Cuba/Meta/hsearch.rds
/usr/lib64/R/library/R2Cuba/Meta/links.rds
/usr/lib64/R/library/R2Cuba/Meta/nsInfo.rds
/usr/lib64/R/library/R2Cuba/Meta/package.rds
/usr/lib64/R/library/R2Cuba/NAMESPACE
/usr/lib64/R/library/R2Cuba/NEWS
/usr/lib64/R/library/R2Cuba/R/R2Cuba
/usr/lib64/R/library/R2Cuba/R/R2Cuba.rdb
/usr/lib64/R/library/R2Cuba/R/R2Cuba.rdx
/usr/lib64/R/library/R2Cuba/demo/GenzSuite.R
/usr/lib64/R/library/R2Cuba/help/AnIndex
/usr/lib64/R/library/R2Cuba/help/R2Cuba.rdb
/usr/lib64/R/library/R2Cuba/help/R2Cuba.rdx
/usr/lib64/R/library/R2Cuba/help/aliases.rds
/usr/lib64/R/library/R2Cuba/help/paths.rds
/usr/lib64/R/library/R2Cuba/html/00Index.html
/usr/lib64/R/library/R2Cuba/html/R.css
/usr/lib64/R/library/R2Cuba/tests/Gtilde2.R
/usr/lib64/R/library/R2Cuba/tests/Gtilde2.Rout.save
/usr/lib64/R/library/R2Cuba/tests/MWE.R
/usr/lib64/R/library/R2Cuba/tests/MWE.Rout.save
/usr/lib64/R/library/R2Cuba/tests/cuhre.R
/usr/lib64/R/library/R2Cuba/tests/cuhre.Rout.save
/usr/lib64/R/library/R2Cuba/tests/divonne.R
/usr/lib64/R/library/R2Cuba/tests/divonne.Rout.save
/usr/lib64/R/library/R2Cuba/tests/peak.R
/usr/lib64/R/library/R2Cuba/tests/peak.Rout.save
/usr/lib64/R/library/R2Cuba/tests/suave.R
/usr/lib64/R/library/R2Cuba/tests/suave.Rout.save
/usr/lib64/R/library/R2Cuba/tests/vegas.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/R2Cuba/libs/R2Cuba.so
/usr/lib64/R/library/R2Cuba/libs/R2Cuba.so.avx2
/usr/lib64/R/library/R2Cuba/libs/R2Cuba.so.avx512
