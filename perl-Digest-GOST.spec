#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Digest
%define		pnam	GOST
Summary:	Digest::GOST - Perl interface to the GOST R 34.11-94 digest algorithm
Summary(pl.UTF-8):	Digest::GOST - implementacja algorytmu skrótu GOST R 34.11-94
Name:		perl-Digest-GOST
Version:	0.06
Release:	10
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Digest/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d91904e56300d08956ea5f1e174863f3
URL:		https://metacpan.org/release/Digest-GOST
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Test-Simple >= 0.82
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Digest::GOST module provides an interface to the GOST R 34.11-94
message digest algorithm. This interface follows the conventions set
forth by the Digest module. To use the CryptoPro parameters, use
Digest::GOST::CryptoPro.

%description -l pl.UTF-8
Moduł Digest::GOST implementuje algorytm skrótu GOST R 34.11-94.
Interfejs programistyczny jest zgodny z konwencją przyjętą przez
moduł Digest. W przypadku wykorzystywania parametrów CryptoPro
należy użyć modułu Digest::GOST::CryptoPro.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%{perl_vendorarch}/Digest/GOST.pm
%{perl_vendorarch}/Digest/GOST
%dir %{perl_vendorarch}/auto/Digest/GOST
%attr(755,root,root) %{perl_vendorarch}/auto/Digest/GOST/GOST.so
%{_mandir}/man3/Digest::GOST.3pm*
%{_mandir}/man3/Digest::GOST::CryptoPro.3pm*
