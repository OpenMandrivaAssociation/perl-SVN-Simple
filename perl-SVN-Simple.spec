%define upstream_name    SVN-Simple
%define upstream_version 0.28

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Simple interface to subversion's editor interface
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/C/CL/CLKAO/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl-SVN
#needed for testing
BuildRequires:  subversion

BuildArch:  noarch

%description
SVN::Simple::Edit wraps the subversion delta editor with 
a perl friendly interface and then you could easily 
drive it for describing changes to a tree.

A common usage is to wrap the commit editor, so you could make 
commits to a subversion repository easily.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc CHANGES README 
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.280.0-2mdv2011.0
+ Revision: 654293
- rebuild for updated spec-helper

* Tue Dec 08 2009 Jérôme Quelin <jquelin@mandriva.org> 0.280.0-1mdv2011.0
+ Revision: 474764
- update to 0.28

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.27-8mdv2009.0
+ Revision: 258408
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.27-7mdv2009.0
+ Revision: 246484
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.27-5mdv2008.1
+ Revision: 171031
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Aug 22 2007 Thierry Vignaud <tv@mandriva.org> 0.27-4mdv2008.0
+ Revision: 69026
+ rebuild (emptylog)

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 0.27-3mdv2008.0
+ Revision: 67735
- fix build (was broken due to half-removed changelog by repsys)
- rebuild


* Fri Jul 14 2006 Olivier Thauvin <nanardon@mandriva.org>
+2006-07-14 20:41:45 (41232)
- mkrel && rebuild

* Fri Jul 14 2006 Olivier Thauvin <nanardon@mandriva.org>
+2006-07-14 20:39:47 (41231)
Import perl-SVN-Simple

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

