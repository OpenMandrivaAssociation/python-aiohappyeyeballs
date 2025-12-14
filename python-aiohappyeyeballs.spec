%define module aiohappyeyeballs

Name:		python-aiohappyeyeballs
Version:	2.6.1
Release:	2
Summary:	Happy Eyeballs for asyncio
URL:		https://pypi.org/project/aiohappyeyeballs/
License:	PSF-2.0
Group:		Development/Python
Source0:	https://files.pythonhosted.org/packages/source/a/aiohappyeyeballs/%{module}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch

BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(cython)
BuildRequires:	python%{pyver}dist(poetry-core)
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(pytest-asyncio)
BuildRequires:	python%{pyver}dist(pytest-cov)

%description
Happy Eyeballs for asyncio

%check
pytest -v tests/

%files
%{python_sitelib}/%{module}/
%{python_sitelib}/%{module}-%{version}.dist-info/
%license LICENSE
%doc README.md
