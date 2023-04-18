Name:           tinyxml
Version:        2.6.2
Release:        23
Summary:        C++ XML parser
License:        zlib
URL:            http://www.grinninglizard.com/tinyxml/
Source0:        http://downloads.sourceforge.net/tinyxml/tinyxml_2_6_2.tar.gz
Patch0001:      CVE-2021-42260.patch
BuildRequires:  gcc-c++

%description
TinyXML parses an XML document, and builds from that a Document
Object Model (DOM) that can be read, modified, and saved.
XML is a very structured and convenient format. All those random file
formats created to store application data can all be replaced with XML.
One parser for everything.

%package        devel
Summary:        Development files for tinyxml
Requires:       %{name} = %{version}-%{release}

%description    devel
The devel package contains development files for tinyxml.
It provides header files and libraries for tinyxml.

%prep
%autosetup -p1 -n tinyxml
touch tinyxml.h

%build
for i in tinyxml.cpp tinystr.cpp tinyxmlerror.cpp tinyxmlparser.cpp; do
  ${CXX} $RPM_OPT_FLAGS -fPIC -o $i.o -c $i
done
${CXX} $RPM_LD_FLAGS -shared -o lib%{name}.so.0.%{version} \
   -Wl,-soname,lib%{name}.so.0 *.cpp.o


%install
install -d $RPM_BUILD_ROOT%{_libdir}
cp lib%{name}.so.0.%{version} $RPM_BUILD_ROOT%{_libdir}/
chmod 755 $RPM_BUILD_ROOT%{_libdir}/libtinyxml.so.0.%{version}
ln -s libtinyxml.so.0.%{version} $RPM_BUILD_ROOT%{_libdir}/libtinyxml.so
ln -s libtinyxml.so.0.%{version} $RPM_BUILD_ROOT%{_libdir}/libtinyxml.so.0

install -d $RPM_BUILD_ROOT%{_includedir}
cp tinyxml.h $RPM_BUILD_ROOT%{_includedir}/
chmod 644 $RPM_BUILD_ROOT%{_includedir}/tinyxml.h

mkdir -p %{buildroot}%{_libdir}/pkgconfig

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%doc changes.txt readme.txt
%{_libdir}/*.so.*

%files devel
%doc docs/*
%{_includedir}/*
%{_libdir}/*.so

%changelog
* Tue Apr 18 2023 Xiaoya Huang <huangxiaoya@iscas.ac.cn> - 2.6.2-23
- Support specify CC

* Thu Jan 27 2022 yaoxin <yaoxin30@huawei.com> - 2.6.2-22
- Change the patch name to CVE-2021-42260.patch.

* Mon Nov  1 2021 Zhiyi Weng <zhiyi@iscas.ac.cn> - 2.6.2-21
- Fix CVE-2021-42260

* Tue Oct 26 2021 chenchen <chen_aka_jan@163.com> - 2.6.2-20
- change the spec file name to be the same as the repo name

* Tue Feb 18 2020 Senlin Xia <xiasenlin1@huawei.com> - 2.6.2-19
- Package init
