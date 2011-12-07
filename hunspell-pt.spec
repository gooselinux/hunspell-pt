Name: hunspell-pt
Summary: Portuguese hunspell dictionaries
%define upstreamid 20090702
Version: 0.%{upstreamid}
Release: 4%{?dist}
Source0: http://natura.di.uminho.pt/download/sources/Dictionaries/hunspell/hunspell-pt_PT-20090309.tar.gz
Source1: http://www.broffice.org/files/pt_BR-2009-07-02AOC.zip
Group: Applications/Text
URL: http://www.broffice.org/verortografico/baixar
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
# pt_BR dicts are under LGPLv2+, pt_PT under GPLv2+ or LGPLv2+ or MPL
License: LGPLv2+ and (GPLv2+ or LGPLv2+ or MPL)
BuildArch: noarch

Requires: hunspell

%description
Portuguese hunspell dictionaries.

%prep
%setup -q -n hunspell-pt_PT-20090309
unzip -q -o %{SOURCE1}
for i in README_pt_BR.TXT README_pt_PT.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-1 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_pt_BR.TXT README_pt_PT.txt COPYING
%{_datadir}/myspell/*

%changelog
* Fri Jun 11 2010 Caolán McNamara <caolanm@redhat.com> - 0.20090702-4
- Resolves: rhbz#602193 clarify licence

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20090702-3.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090702-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090702-2
- tidy spec

* Fri Jul 03 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090702-1
- latest pt_BR version

* Thu Apr 30 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090330-1
- latest pt_BR version

* Tue Mar 10 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090309-1
- latest pt_PT version

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20081113-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 23 2008 Caolan McNamara <caolanm@redhat.com> - 0.20081113-1
- latest pt_PT version

* Tue Jul 08 2008 Caolan McNamara <caolanm@redhat.com> - 0.20080707-1
- latest pt_BR version

* Mon Jul 07 2008 Caolan McNamara <caolanm@redhat.com> - 0.20080705-1
- latest pt_PT version

* Tue Jun 10 2008 Caolan McNamara <caolanm@redhat.com> - 0.20080610-1
- latest version

* Fri Mar 21 2008 Caolan McNamara <caolanm@redhat.com> - 0.20080320-1
- latest version

* Thu Feb 21 2008 Caolan McNamara <caolanm@redhat.com> - 0.20080221-1
- latest version

* Fri Feb 15 2008 Caolan McNamara <caolanm@redhat.com> - 0.20080210-1
- latest version

* Fri Dec 14 2007 Caolan McNamara <caolanm@redhat.com> - 0.20071212-1
- latest version

* Sat Nov 11 2007 Caolan McNamara <caolanm@redhat.com> - 0.20071106-1
- latest version

* Mon Nov 05 2007 Caolan McNamara <caolanm@redhat.com> - 0.20071101-1
- latest version

* Fri Oct 05 2007 Caolan McNamara <caolanm@redhat.com> - 0.20071003-1
- next version

* Tue Oct 02 2007 Caolan McNamara <caolanm@redhat.com> - 0.20071001-1
- next version

* Tue Aug 28 2007 Caolan McNamara <caolanm@redhat.com> - 0.20070823-2
- source file audit shows that pt_BR-2007-04-11.zip silently changed
  content, updating to match

* Thu Aug 23 2007 Caolan McNamara <caolanm@redhat.com> - 0.20070823-1
- latest version

* Fri Aug 03 2007 Caolan McNamara <caolanm@redhat.com> - 0.20070709-2
- clarify licences

* Wed Jul 18 2007 Caolan McNamara <caolanm@redhat.com> - 0.20070709-1
- latest pt_PT version

* Sun May 06 2007 Caolan McNamara <caolanm@redhat.com> - 0.20070411-1
- latest versions

* Wed Feb 14 2007 Caolan McNamara <caolanm@redhat.com> - 0.20061026-2
- disambiguate readmes

* Thu Dec 07 2006 Caolan McNamara <caolanm@redhat.com> - 0.20061026-1
- initial version
