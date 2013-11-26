%define		packname	affyio

Summary:	Tools for parsing Affymetrix data files
Name:		R-%{packname}
Version:	1.30.0
Release:	1
License:	LGPL v2+
Group:		Applications/Engineering
Source0:	http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	5a26b715296921b05ab788e6af2a3e09
Patch0:		no-zlibbioc.patch
URL:		http://bioconductor.org/packages/release/bioc/html/affyio.html
BuildRequires:	R
BuildRequires:	texlive-latex
BuildRequires:	zlib-devel
Requires:	R
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Routines for parsing Affymetrix data files based upon file format
information. Primary focus is on accessing the CEL and CDF file
formats.

%prep
%setup -q -c -n %{packname}
%patch0 -p0

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

R CMD INSTALL %{packname} -l $RPM_BUILD_ROOT%{_libdir}/R/library

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/LICENSE
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/R/
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/libs
