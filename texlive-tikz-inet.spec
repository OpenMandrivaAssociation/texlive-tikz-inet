Name:		texlive-tikz-inet
Version:	15878
Release:	2
Summary:	Draw interaction nets with TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/tikz-inet
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-inet.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-inet.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package extends TikZ with macros to draw interaction nets.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tikz-inet/tikz-inet.sty
%doc %{_texmfdistdir}/doc/latex/tikz-inet/README
%doc %{_texmfdistdir}/doc/latex/tikz-inet/tikz-inet-doc.pdf
%doc %{_texmfdistdir}/doc/latex/tikz-inet/tikz-inet-doc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
