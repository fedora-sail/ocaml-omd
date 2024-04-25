Name:           ocaml-omd
Version:        1.3.2
Release:        %autorelease
Summary:        extensible Markdown library and tool in "pure OCaml"

License:        ISC
URL:            https://github.com/ocaml/omd
Source0:        https://github.com/ocaml/omd/archive/%{version}/omd-%{version}.tar.gz

BuildRequires:  coq
BuildRequires:  ocaml >= 4.08.1
BuildRequires:  ocaml-dune >= 2.7
BuildRequires:  ocaml-uutf-devel
BuildRequires:  ocaml-uucp-devel
BuildRequires:  ocaml-uunf-devel
BuildRequires:  ocaml-dune-build-info-devel
BuildRequires:  ocaml-ppx-expect-devel
BuildRequires:  ocaml-time-now-devel

%description
Omd is an OCaml library designed to parse, manipulate, and print Markdown into different formats. In addition to the library, a command-line tool omd is included to easily convert markdown into HTML.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
 
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n omd-%{version} -p1

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc README.md CHANGES.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
