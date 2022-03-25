#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Python 2 module to get image size from PNG/JPEG/JPEG2000/GIF file
Summary(pl.UTF-8):	Moduł Pythona 2 do pobierania rozmiaru obrazu z pliku PNG/JPEG/JPEG2000/GIF
Name:		python-imagesize
Version:	1.3.0
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/imagesize/
Source0:	https://files.pythonhosted.org/packages/source/i/imagesize/imagesize-%{version}.tar.gz
# Source0-md5:	27da6cc27370c69834723012f2eb203a
Patch0:		%{name}-py2.patch
URL:		https://pypi.org/project/imagesize/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules >= 1:2.7
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
Requires:	python3-modules >= 1:3.4

%description -n python3-imagesize
This module analyzes JPEG/JPEG2000/PNG/GIF image header and returns
image size.

%description -n python3-imagesize -l pl.UTF-8
Ten moduł analizuje nagłówek pliku JPEG/JPEG2000/PNG/GIF i zwraca
rozmiary obrazka.

%prep
%setup -q -n imagesize-%{version}
%patch0 -p1

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m unittest discover -s test
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m unittest discover -s test
%endif
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
%doc LICENSE.rst README.rst
%{py_sitescriptdir}/imagesize.py[co]
%{py_sitescriptdir}/imagesize-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-imagesize
%defattr(644,root,root,755)
%doc LICENSE.rst README.rst
%{py3_sitescriptdir}/imagesize.py
%{py3_sitescriptdir}/__pycache__/imagesize.cpython-*.py[co]
%{py3_sitescriptdir}/imagesize-%{version}-py*.egg-info
%endif
