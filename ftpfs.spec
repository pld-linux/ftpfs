# TODO: UP/SMP modules
#
# Conditional build:
%bcond_without 	dist_kernel	# without kernel from distribution
#
%define		smpstr		%{?with_smp:-smp}
%define		smp		%{?with_smp:1}%{!?with_smp:0}
Summary:	FTP File System
Summary(pl):	System plików FTP
Name:		ftpfs
Version:	0.6.2
Release:	1
License:	GPL
Group:		Base/Kernel
Source0:	http://dl.sourceforge.net/ftpfs/%{name}-%{version}-k2.4.tar.gz
# Source0-md5:	5e160de7f7237cdb27e5bc6f234e8c14
Patch0:		%{name}-opt.patch
%{?with_dist_kernel:BuildRequires:	kernel-headers >= 2.4}
BuildRequires:	rpmbuild(macros) >= 1.118
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FTP File System is a Linux kernel module, enhancing the VFS with FTP
volume mounting capabilities. That is, you can "mount" FTP shared
directories in your very personal file system and take advantage of
local files ops.

%description -l pl
System plików FTP jest modu³em j±dra rozszerzaj±cym VFS o mo¿liwo¶æ
montowania wolumenów FTP. Oznacza to, ¿e mo¿esz podmontowaæ katalogi
FTP do swojego systemu plików i korzystaæ z nich jak z plików
lokalnych.

%package -n kernel%{smpstr}-net-ftpfs
Summary:	FTP File System - kernel module
Summary(pl):	System plików FTP - modu³ j±dra
Release:	%{release}@%{_kernel_ver_str}
Group:		Base/Kernel
Requires(post,postun):	/sbin/depmod
Obsoletes:	ftpfs
Provides:	ftpfs = %{version}

%description -n kernel%{smpstr}-net-ftpfs
FTP File System is a Linux kernel module, enhancing the VFS with FTP
volume mounting capabilities. That is, you can "mount" FTP shared
directories in your very personal file system and take advantage of
local files ops. This package contains ftpfs kernel module.

%description -n kernel%{smpstr}-net-ftpfs -l pl
System plików FTP jest modu³em j±dra rozszerzaj±cym VFS o mo¿liwo¶æ
montowania wolumenów FTP. Oznacza to, ¿e mo¿esz podmontowaæ katalogi
FTP do swojego systemu plików i korzystaæ z nich jak z plików
lokalnych. Ten pakiet zawiera modu³ j±dra do ftpfs.

%package -n ftpmount
Summary:	FTP File System mounting utility
Summary(pl):	Narzêdzie do montowania systemów plików FTP
Group:		Applications/System
Requires:	ftpfs = %{version}

%description -n ftpmount
FTP File System mounting utility.

%description -n ftpmount -l pl
Narzêdzie do montowania systemów plików FTP.

%prep
%setup -q -n ftpfs-%{version}-k2.4
%patch -p1

%build
%{__make} OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -D ftpfs/ftpfs.o $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}/misc/ftpfs.o
install -D ftpmount/ftpmount $RPM_BUILD_ROOT%{_sbindir}/ftpmount

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n kernel%{smpstr}-net-ftpfs
%depmod %{_kernel_ver}

%postun -n kernel%{smpstr}-net-ftpfs
%depmod %{_kernel_ver}

%files -n kernel%{smpstr}-net-ftpfs
%defattr(644,root,root,755)
%doc docs CHANGELOG TODO
/lib/modules/*/*/*

%files -n ftpmount
%defattr(644,root,root,755)
%doc ftpmount/README
%attr(755,root,root) %{_sbindir}/ftpmount
