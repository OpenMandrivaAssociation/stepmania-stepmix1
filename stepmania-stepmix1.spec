%define name stepmania-stepmix1
%define version 1
%define release 7

Summary: StepMania StepMix1 song pack
Name: %{name}
Version: %{version}
Release: %{release}
# from http://www.tfbw.com/dancegames/songs/
Source0: http://files.tfbw.com/stepmania/songs/StepMania_all_StepMix1_entries.smzip
License: Creative Commons Attribution/Attribution-ShareAlike 2.5
Group: Games/Arcade
Url: http://www.stepmania.com/wiki/StepMix_1_Contest
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch

%description
This packages contains the songs from the StepMania StepMix1 contest.

%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
install -D -m 644 %{SOURCE0} %{buildroot}%{_gamesdatadir}/StepMania/Packages/StepMix1.smzip

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_gamesdatadir}/StepMania/Packages/StepMix1.smzip




%changelog
* Sun Sep 20 2009 Thierry Vignaud <tvignaud@mandriva.com> 1-6mdv2010.0
+ Revision: 445236
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 1-4mdv2009.0
+ Revision: 261177
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 1-3mdv2009.0
+ Revision: 253548
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1-1mdv2008.1
+ Revision: 136523
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Dec 01 2006 Olivier Blin <oblin@mandriva.com> 1-1mdv2007.1
+ Revision: 89925
- initial StepMania StepMix1 package
- Create stepmania-stepmix1

