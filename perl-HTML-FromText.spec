%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	FromText
Summary:	HTML::FromText perl module
Summary(pl):	Modu³ perla HTML::FromText
Name:		perl-HTML-FromText
Version:	1.005
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::FromText converts text to HTML.

%description -l pl
HTML::FromText konwertuje tekst do formatu HTML.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%{perl_sitelib}/HTML/FromText.pm
%{_mandir}/man3/*
