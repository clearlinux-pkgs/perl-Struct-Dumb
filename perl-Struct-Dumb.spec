#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Struct-Dumb
Version  : 0.12
Release  : 24
URL      : https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Struct-Dumb-0.12.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Struct-Dumb-0.12.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libs/libstruct-dumb-perl/libstruct-dumb-perl_0.09-1.debian.tar.xz
Summary  : 'make simple lightweight record-like structures'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Struct-Dumb-license = %{version}-%{release}
Requires: perl-Struct-Dumb-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Test::Fatal)

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
Requires: perl-Struct-Dumb = %{version}-%{release}

%description dev
dev components for the perl-Struct-Dumb package.


%package license
Summary: license components for the perl-Struct-Dumb package.
Group: Default

%description license
license components for the perl-Struct-Dumb package.


%package perl
Summary: perl components for the perl-Struct-Dumb package.
Group: Default
Requires: perl-Struct-Dumb = %{version}-%{release}

%description perl
perl components for the perl-Struct-Dumb package.


%prep
%setup -q -n Struct-Dumb-0.12
cd %{_builddir}
tar xf %{_sourcedir}/libstruct-dumb-perl_0.09-1.debian.tar.xz
cd %{_builddir}/Struct-Dumb-0.12
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Struct-Dumb-0.12/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Struct-Dumb
cp %{_builddir}/Struct-Dumb-0.12/LICENSE %{buildroot}/usr/share/package-licenses/perl-Struct-Dumb/7e88e362b09da4b18d7e611c14945b5734383496
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Struct::Dumb.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Struct-Dumb/7e88e362b09da4b18d7e611c14945b5734383496

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
