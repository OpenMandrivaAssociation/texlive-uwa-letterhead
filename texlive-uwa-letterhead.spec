%global tl_name uwa-letterhead
%global tl_revision 78431

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.1
Release:	%{tl_revision}.1
Summary:	The letterhead of the University of Western Australia
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/unicodetex/latex/uwa-letterhead
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uwa-letterhead.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uwa-letterhead.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uwa-letterhead.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package generates the letterhead of the University of Western
Australia. It requires the UWA logo in PDF format, which is available in
SVG format at https://static-listing.weboffice.uwa.edu.au/visualid/core-
rebra nd/img/uwacrest/, and uses the Arial and UWA Slab fonts by
default. The package works with XeLaTeX and LuaLaTeX.

