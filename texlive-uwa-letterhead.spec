Name:		texlive-uwa-letterhead
Version:	64491
Release:	2
Summary:	The letterhead of the University of Western Australia
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/uwa-letterhead
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uwa-letterhead.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uwa-letterhead.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uwa-letterhead.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package generates the letterhead of the University of
Western Australia. It requires the UWA logo in PDF format,
which is available in SVG format at
https://static-listing.weboffice.uwa.edu.au/visualid/core-rebra
nd/img/uwacrest/, and uses the Arial and UWA Slab fonts by
default. The package works with XeLaTeX and LuaLaTeX.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/uwa-letterhead
%{_texmfdistdir}/tex/latex/uwa-letterhead
%doc %{_texmfdistdir}/doc/latex/uwa-letterhead

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
