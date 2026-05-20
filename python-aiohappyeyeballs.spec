%define module aiohappyeyeballs
%bcond tests 1

Name:		python-aiohappyeyeballs
Version:	2.7.0
Release:	1
Summary:	Happy Eyeballs for asyncio
License:	PSF-2.0
Group:		Development/Python
URL:		https://github.com/aio-libs/aiohappyeyeballs
Source0:	%{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(cython)
BuildRequires:	python%{pyver}dist(poetry-core)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with tests}
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(pytest-asyncio)
%endif

%description
Happy Eyeballs for asyncio

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}"
# disable coverage tests
sed -i -e 's/addopts = "-v -Wdefault --cov=aiohappyeyeballs --cov-report=term-missing:skip-covered"/addopts = "-v -Wdefault"/g' pyproject.toml
rm -rf tests/conftest.py
# run pytest
pytest -v
%endif

%files
%doc README.md
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
