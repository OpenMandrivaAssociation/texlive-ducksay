Name:		texlive-ducksay
Version:	64655
Release:	1
Summary:	Draw ASCII art of animals saying a specified message
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ducksay
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ducksay.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ducksay.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ducksay.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package draws ASCII art of animals saying a specified
message. The following macros are available: \ducksay
\duckthink \DefaultAnimal \AddAnimal \DucksayOptions Multi-line
messages are now fully supported. The package comes with two
versions, choosable with the version key.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/ducksay
%{_texmfdistdir}/tex/latex/ducksay
%doc %{_texmfdistdir}/doc/latex/ducksay

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
