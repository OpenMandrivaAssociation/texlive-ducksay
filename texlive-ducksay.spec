%global tl_name ducksay
%global tl_revision 76911

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.8
Release:	%{tl_revision}.1
Summary:	Draw ASCII art of animals saying a specified message
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ducksay
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ducksay.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ducksay.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ducksay.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package draws ASCII art of animals saying a specified message. The
following macros are available: \ducksay \duckthink \DefaultAnimal
\AddAnimal \DucksayOptions Multi-line messages are now fully supported.
The package comes with two versions, choosable with the version key.

