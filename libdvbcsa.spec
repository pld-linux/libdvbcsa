Summary:	A free implementation of the DVB/CSA
Summary(pl.UTF-8):	Wolnodostępna implementacja DVB/CSA
Name:		libdvbcsa
Version:	1.1.0
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://download.videolan.org/pub/videolan/libdvbcsa/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	478ab1ca56ca58d2667da6ce22f74e39
URL:		http://www.videolan.org/developers/libdvbcsa.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libdvbcsa is a free implementation of the DVB Common Scrambling
Algorithm - DVB/CSA - with encryption and decryption capabilities.

%description -l pl.UTF-8
libdvbcsa to wolnodostępna implementacja algorytmu DVB/CSA (DVB
Common Scrambling Algorithm - ogólnego algorytmu kodowania DVB)
wraz z możliwością szyfrowania i odszyfrowywania.

%package devel
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{name} library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki %{name}.

%package static
Summary:	Static %{name} library
Summary(pl.UTF-8):	Statyczna biblioteka %{name}
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static %{name} library.

%description static -l pl.UTF-8
Statyczna biblioteka %{name}.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# library has no dependencies (except for libc)
%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/%{name}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/%{name}.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}.so
%{_includedir}/dvbcsa

%files static
%defattr(644,root,root,755)
%{_libdir}/%{name}.a
