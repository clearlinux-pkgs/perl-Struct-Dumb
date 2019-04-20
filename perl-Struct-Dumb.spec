#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Struct-Dumb
Version  : 0.09
Release  : 9
URL      : https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Struct-Dumb-0.09.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Struct-Dumb-0.09.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libs/libstruct-dumb-perl/libstruct-dumb-perl_0.09-1.debian.tar.xz
Summary  : 'make simple lightweight record-like structures'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Struct-Dumb-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Try::Tiny)

%description
NAME
Struct::Dumb - make simple lightweight record-like structures
SYNOPSIS
use Struct::Dumb;

struct Point => [qw( x y )];

my $point = Point(10, 20);

printf "Point is at (%d, %d)\n", $point->x, $point->y;

$point->y = 30;
printf "Point is now at (%d, %d)\n", $point->x, $point->y;

%package dev
Summary: dev components for the perl-Struct-Dumb package.
Group: Development
Provides: perl-Struct-Dumb-devel = %{version}-%{release}

%description dev
dev components for the perl-Struct-Dumb package.


%package license
Summary: license components for the perl-Struct-Dumb package.
Group: Default

%description license
license components for the perl-Struct-Dumb package.


%prep
%setup -q -n Struct-Dumb-0.09
cd ..
%setup -q -T -D -n Struct-Dumb-0.09 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Struct-Dumb-0.09/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Struct-Dumb
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Struct-Dumb/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/Struct/Dumb.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Struct::Dumb.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Struct-Dumb/LICENSE
