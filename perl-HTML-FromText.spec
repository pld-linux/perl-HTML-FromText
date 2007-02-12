#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	HTML
%define		pnam	FromText
Summary:	HTML::FromText Perl module - convert plain text to HTML
Summary(pl.UTF-8):   Moduł Perla HTML::FromText - konwersja czystego tekstu do HTML
Name:		perl-HTML-FromText
Version:	2.05
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fb8ae4ab0cae0b57101f78b046b3927b
%if %{with tests}
BuildRequires:	perl-Email-Find >= 0.09
BuildRequires:	perl-Exporter-Lite >= 0.01
BuildRequires:	perl-HTML-Parser >= 3.26
BuildRequires:	perl(HTML::Entities) >= 1.26
# Scalar::Util in perl-modules 5.8.0 is too old
BuildRequires:	perl-Scalar-List-Utils >= 1.12
BuildRequires:	perl(Scalar::Util) >= 1.12
BuildRequires:	perl(Text::Tabs) >= 98.1128
BuildRequires:	perl-Test-Pod >= 0.95
BuildRequires:	perl-Test-Simple >= 0.47
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::FromText converts text to HTML.

%description -l pl.UTF-8
HTML::FromText konwertuje tekst do formatu HTML.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/text2html
%{perl_vendorlib}/HTML/FromText.pm
%{_mandir}/man1/*
%{_mandir}/man3/*
