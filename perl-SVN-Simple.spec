%define upstream_name    SVN-Simple
%define upstream_version 0.28

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Simple interface to subversion's editor interface
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://search.cpan.org/CPAN/authors/id/C/CL/CLKAO/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl-SVN
#needed for testing
BuildRequires:  subversion

BuildArch:  noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
SVN::Simple::Edit wraps the subversion delta editor with 
a perl friendly interface and then you could easily 
drive it for describing changes to a tree.

A common usage is to wrap the commit editor, so you could make 
commits to a subversion repository easily.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGES README 
%{perl_vendorlib}/*
%{_mandir}/man3/*
