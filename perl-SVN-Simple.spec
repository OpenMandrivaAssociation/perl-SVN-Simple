%define realname   SVN-Simple

Name:		perl-%{realname}
Version:        0.27
Release:        %mkrel 5
License:	GPL or Artistic
Group:		Development/Perl
Summary:        Simple interface to subversion's editor interface
Source0:        http://search.cpan.org/CPAN/authors/id/C/CL/CLKAO/%{realname}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{realname}/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel perl-SVN
#needed for testing
BuildRequires:  subversion
BuildArch:      noarch
%description
SVN::Simple::Edit wraps the subversion delta editor with 
a perl friendly interface and then you could easily 
drive it for describing changes to a tree.

A common usage is to wrap the commit editor, so you could make 
commits to a subversion repository easily.

%prep
%setup -q -n %{realname}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

make test

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

