# TODO:
# - regenerate ac/am
# - desktop and icon
Summary:	Gnome BibTeX editor
Name:		gbib
Version:	0.1.2
Release:	0.9
License:	GPL ??
Group:		X11/Applications
Source0:	ftp://ftp.seul.org/pub/gbib/src/%{name}-%{version}.tar.gz
# Source0-md5:	b90e05dbac8be823ccb06616eaff3d02
#Source1:	%{name}.desktop
URL:		http://gbib.seul.org/
#BuildRequires:	autoconf
#BuildRequires:	automake
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
gBib is a user-friendly Gnome BibTeX database browser and editor. It
provides facilities for merging BibTeX files, managing key conflicts,
and adding bibliographic citations in LyX.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	ROOTDIR=$RPM_BUILD_ROOT

#install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install gbib48.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/gbib.xpm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES INSTALL README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/gbibtex
%{_datadir}/gbibtex/*.rc
%{_datadir}/gbibtex/*.xpm
#%{_desktopdir}/*
%{_pixmapsdir}/*
