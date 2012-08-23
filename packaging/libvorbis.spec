Name:       libvorbis
Summary:    The Vorbis General Audio Compression Codec
Version:    1.3.2
Release:    2
Group:      System/Libraries
License:    BSD
URL:        http://www.xiph.org/
Source0:    http://downloads.xiph.org/releases/vorbis/%{name}-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(ogg)

%description
Description: %{summary}

%package devel
Summary:    Development tools for Vorbis applications
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Description: %{summary}

%prep
%setup -q -n %{name}-%{version}

%build

%configure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install
rm -rf $RPM_BUILD_ROOT%{_docdir}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_libdir}/libvorbis.so.*
%{_libdir}/libvorbisfile.so.*
%{_libdir}/libvorbisenc.so.*

%files devel
%{_includedir}/vorbis
%{_libdir}/libvorbis.so
%{_libdir}/libvorbisfile.so
%{_libdir}/libvorbisenc.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/vorbis.m4

