Summary:	FTP File System 
Summary(pl):	FTP File System 
Name:		ftpfs
Version:	0.2.2
Release:	1
License:	GPL
Group:		Base/Kernel
Group(de):	Grundsätzlich/Kern
Group(pl):	Podstawowe/J±dro
Source0:	http://ftp1.sourceforge.net/ftpfs/%{name}-%{version}-k2.4.tar.gz
BuildRequires:	kernel-headers >= 2.4
BuildRequires:	awk
BuildRequires:	tar
Prereq:		/sbin/depmod
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FTP File System is a Linux kernel module, enhancing the VFS with FTP
volume mounting capabilities. That is, you can "mount" FTP shared
directories in your very personal file system and take advantage of
local files ops.

%description -l pl
FTP File System

%prep

%setup  -q -n ftpfs-0.2.2-k2.4

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

tar czf docs.tar.gz docs

KERNEL_VERSION=`awk 'BEGIN {FS="\""} /^#define UTS_RELEASE/ { print $2}' < %{_includedir}/linux/version.h`
install -D ftpfs.o $RPM_BUILD_ROOT/lib/modules/$KERNEL_VERSION/fs/ftpfs.o

%post
/sbin/depmod -a
	
%postun
/sbin/depmod -a
	
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/lib/modules/*/*/*
%doc docs.tar.gz
