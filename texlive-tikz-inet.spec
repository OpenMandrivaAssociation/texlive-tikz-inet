# revision 15878
# category Package
# catalog-ctan /graphics/pgf/contrib/tikz-inet
# catalog-date 2008-08-24 14:43:48 +0200
# catalog-license lppl
# catalog-version 0.1
Name:		texlive-tikz-inet
Version:	0.1
Release:	2
Summary:	Draw interaction nets with TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/tikz-inet
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-inet.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-inet.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
