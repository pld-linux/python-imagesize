#
# Conditional build:
%bcond_with	tests	# test target [test images are missing]
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Python 2 module to get image size from PNG/JPEG/JPEG2000/GIF file
Summary(pl.UTF-8):	Moduł Pythona 2 do pobierania rozmiaru obrazu z pliku PNG/JPEG/JPEG2000/GIF
Name:		python-imagesize
Version:	0.7.1
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/simple/imagesize/
Source0:	https://pypi.python.org/packages/53/72/6c6f1e787d9cab2cc733cf042f125abec07209a58308831c9f292504e826/imagesize-%{version}.tar.gz
# Source0-md5:	976148283286a6ba5f69b0f81aef8052
URL:		https://pypi.python.org/pypi/imagesize
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module analyzes JPEG/JPEG2000/PNG/GIF image header and returns
image size.

%description -l pl.UTF-8
Ten moduł analizuje nagłówek pliku JPEG/JPEG2000/PNG/GIF i zwraca
rozmiary obrazka.

%package -n python3-imagesize
Summary:	Python 3 module to get image size from PNG/JPEG/JPEG2000/GIF file
Summary(pl.UTF-8):	Moduł Pythona 3 do pobierania rozmiaru obrazu z pliku PNG/JPEG/JPEG2000/GIF
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-imagesize
This module analyzes JPEG/JPEG2000/PNG/GIF image header and returns
image size.

%description -n python3-imagesize -l pl.UTF-8
Ten moduł analizuje nagłówek pliku JPEG/JPEG2000/PNG/GIF i zwraca
rozmiary obrazka.

%prep
%setup -q -n imagesize-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/imagesize
%{py_sitescriptdir}/imagesize-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-imagesize
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/imagesize
%{py3_sitescriptdir}/imagesize-%{version}-py*.egg-info
%endif
