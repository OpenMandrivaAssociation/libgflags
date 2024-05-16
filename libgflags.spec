Name: libgflags
Version: 2.2.2
Release: 1
Source0: https://github.com/gflags/gflags/archive/refs/tags/v%{version}.tar.gz
Summary: C++ library for command line flags processing
URL: https://github.com/gflags/gflags
License: BSD-3-Clause
Group: System/Libraries
BuildSystem: cmake

%description
The gflags package contains a C++ library that implements commandline flags
processing. It includes built-in support for standard types such as string
and the ability to define flags in the source file in which they are used.

%install -a
%libpackages

rm -rf %{buildroot}$(realpath ~)/.cmake

%files
%{_bindir}/gflags_completions.sh
