%include	/usr/lib/rpm/macros.perl
Summary:	HTML-FromText perl module
Summary(pl):	Modu³ perla HTML-FromText
Name:		perl-HTML-FromText
Version:	1.005
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTML/HTML-FromText-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML-FromText converts text to HTML.

%description -l pl
HTML-FromText konwertuje tekst do formatu HTML.

%prep
%setup -q -n HTML-FromText-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/HTML/FromText.pm
%{_mandir}/man3/*
