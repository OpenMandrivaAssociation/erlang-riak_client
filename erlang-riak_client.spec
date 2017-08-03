%global realname riak_client
%global upstream basho
# Technically, we're noarch; but erlang whose directories we install into is not.
%global debug_package %{nil}


Name:		erlang-%{realname}
Version:	2.1.1
Release:	1
Summary:	Erlang client for Riak
Group:		Development/Erlang
License:	ASL 2.0
URL:		https://github.com/%{upstream}/riak-erlang-client
Source0:	https://github.com/%{upstream}/riak-erlang-client/archive/%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-rak_client-0001-Ensure-auto_reconnect-if-first-connect-fails.patch
Patch2:		erlang-rak_client-0002-Send-a-timeout-in-the-protobuf-message-only-if-it-is.patch
Patch3:		erlang-rak_client-0003-Fixes-for-OTP-18.patch
Patch4:		erlang-rak_client-0004-Relax-requirement-for-riak_pb.patch
Patch5:		erlang-rak_client-0005-Use-proper-version-in-app-file.patch
BuildRequires:	erlang-riak_pb
BuildRequires:	erlang-rebar
Provides:	riak-erlang-client%{?_isa} = %{version}-%{release}


%description
Erlang client for Riak.


%prep
%setup -q -n riak-erlang-client-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1


%build
%{rebar_compile}


%install
mkdir -p %{buildroot}%{_erllibdir}/%{realname}-%{version}/{ebin,include}
install -m 644 ebin/riakc.app ebin/riakc*.beam %{buildroot}%{_erllibdir}/%{realname}-%{version}/ebin
install -m 644 include/riakc.hrl %{buildroot}%{_libdir}/erlang/lib/%{realname}-%{version}/include


%files
%license LICENSE
%doc README.md docs/pb-client.txt
%{_libdir}/erlang/lib/%{realname}-%{version}/


%changelog
* Sat May 07 2016 neoclust <neoclust> 2.1.1-1.mga6
+ Revision: 1010443
- imported package erlang-riak_client

