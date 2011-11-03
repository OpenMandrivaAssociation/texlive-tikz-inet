# revision 15878
# category Package
# catalog-ctan /graphics/pgf/contrib/tikz-inet
# catalog-date 2008-08-24 14:43:48 +0200
# catalog-license lppl
# catalog-version 0.1
Name:		texlive-tikz-inet
Version:	0.1
Release:	1
Summary:	Draw interaction nets with TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/tikz-inet
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-inet.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-inet.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package extends TikZ with macros to draw interaction nets.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tikz-inet/tikz-inet.sty
%doc %{_texmfdistdir}/doc/latex/tikz-inet/README
%doc %{_texmfdistdir}/doc/latex/tikz-inet/tikz-inet-doc.pdf
%doc %{_texmfdistdir}/doc/latex/tikz-inet/tikz-inet-doc.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
