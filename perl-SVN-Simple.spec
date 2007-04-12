%define realname   SVN-Simple

Name:		perl-%{realname}
Version:        0.27
Release:        %mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
Summary:        This module is a simple interface to subversion's editor interface
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


* Thu Feb 24 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.27-1mdk
- 0.27

* Sat Feb 05 2005 Sylvie Terjan <erinmargault@mandrake.org> 0.26-2mdk
- rebuild for new perl

* Fri Nov 12 2004 Michael Scherer <misc@mandrake.org> 0.26-1mdk
- New release 0.26

* Sat Jun 05 2004 Michael Scherer <misc@mandrake.org> 0.25-2mdk 
- BuildRequires

* Fri Apr 02 2004 Michael Scherer <misc@mandrake.org> 0.25-1mdk 
- First MandrakeSoft Package
