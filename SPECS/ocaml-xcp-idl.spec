%global debug_package %{nil}

Name:           ocaml-xcp-idl
Version:        1.43.0
Release:        2%{?dist}
Summary:        Common interface definitions for XCP services
License:        LGPL
URL:            https://github.com/xapi-project/xcp-idl
Source0:        https://code.citrite.net/rest/archive/latest/projects/XSU/repos/xcp-idl/archive?at=v%{version}&format=tar.gz&prefix=xcp-idl-%{version}#/xcp-idl-%{version}.tar.gz
Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XSU/repos/xcp-idl/archive?at=v1.43.0&format=tar.gz&prefix=xcp-idl-1.43.0#/xcp-idl-1.43.0.tar.gz) = b062924ccc99713e9836e5c9b33b30734febce85
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  xs-opam-repo
BuildRequires:  message-switch-devel

%global _use_internal_dependency_generator 0
%global __requires_exclude *caml*

%description
Common interface definitions for XCP services.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       message-switch-devel%{?_isa}
Requires:       xs-opam-repo

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%global ocaml_libdir /usr/lib/opamroot/system/lib
%global build_ocaml_libdir %{buildroot}%{ocaml_libdir}

%prep
%autosetup -p1 -n xcp-idl-%{version}

%build
make %{?coverage:runtime-coverage}

%install
export OCAMLFIND_LDCONF=ignore
export OCAMLFIND_DESTDIR=%{build_ocaml_libdir}
mkdir -p $OCAMLFIND_DESTDIR
DESTDIR=${RPM_BUILD_ROOT} %{__make} install

# this is to make opam happy
mkdir -p %{build_ocaml_libdir}/xapi-idl
touch %{build_ocaml_libdir}/xapi-idl/opam.config

%files
%doc MAINTAINERS
%doc %{ocaml_libdir}/../doc/xapi-idl/CHANGES
%doc %{ocaml_libdir}/../doc/xapi-idl/LICENSE 
%doc %{ocaml_libdir}/../doc/xapi-idl/README.md
%{ocaml_libdir}/xcp
%{ocaml_libdir}/stublibs/*.so
%exclude %{ocaml_libdir}/xcp/*.a
%exclude %{ocaml_libdir}/xcp/*.cmx
%exclude %{ocaml_libdir}/xcp/*.cmxa
%exclude %{ocaml_libdir}/xcp/*.cmxs
%exclude %{ocaml_libdir}/xcp/*.mli
%exclude %{ocaml_libdir}/xcp/*.cmt
%exclude %{ocaml_libdir}/xcp/*.cmti
%exclude %{ocaml_libdir}/../doc/xcp

%files devel
%{ocaml_libdir}/xcp/*.a
%{ocaml_libdir}/xcp/*.cmx
%{ocaml_libdir}/xcp/*.cmxa
%{ocaml_libdir}/xcp/*.cmxs
%{ocaml_libdir}/xcp/*.mli
%{ocaml_libdir}/xapi-idl

%changelog
* Wed Apr 04 2018 Marcello Seri <marcello.seri@citrix.com> - 1.43.0-2
- Update SPEC file to get rid of rpmbuild warnings

* Wed Apr 04 2018 Christian Lindig <christian.lindig@citrix.com> - 1.43.0-1
- CP-26340: SR.probe changes
- Make probe return value match the one in SMAPIv3
- Add SR UUID to sr_info
- remove unused type declaration

* Tue Apr 03 2018 Christian Lindig <christian.lindig@citrix.com> - 1.42.0-1
- Fix and add CLIs: memory, network, gpumon, v6

* Thu Mar 22 2018 Marcello Seri <marcello.seri@citrix.com> - 1.41.0-1
- CP-25798:  Factoring out PCI address to common lib
- CP-25798: Add interface of SRIOV support
- CP-26333 Add interface Network.Interface.get_pci_bus_path
- Differentiate the sriov_result into three kinds.
- CP-25794: Add new network backend type for network SR-IOV
- Port sriov interface to ppx

* Wed Mar 21 2018 Christian Lindig <christian.lindig@citrix.com> - 1.40.0-1
- Add tests: network interface,  gpumon interface, memory interface
- Add alcotest dependency to opam, explicit test deps in travis.yml
- Fix warning (Re_str -> Re.Str)

* Fri Mar 09 2018 Christian Lindig <christian.lindig@citrix.com> - 1.39.0-1
- CA-285213 add error logging for Memory_interface
- CA-285213 add error logging for Network_interface
- CA-285213 add error logging for V6_interface
- CA-285213 add error logging for Gpumon_interface
- network_interface: extend the abstract type declaration for 
  compatibility with rpc 3.2.0
- xcp_service: Re_emacs -> Re.Emacs to get rid of deprecation warnings
- cluster_interface: update to the new idl error functor

* Mon Mar 05 2018 Christian Lindig <christian.lindig@citrix.com> - 1.38.0-1
- Test the RRD interface

* Wed Feb 28 2018 Christian Lindig <christian.lindig@citrix.com> - 1.37.0-1
- Add PVinPVH build_info type + a domain_type field in Vm.state
- Add memory.ml from xen-api/xenopsd/squeezed
- Update memory model for PV-in-PVH
- CP-26352 Port xcp-idl/network interface from Camlp4 to PPX

* Thu Feb 22 2018 Christian Lindig <christian.lindig@citrix.com> - 1.36.0-1
- CA-283754: ppxified interfaces, do not discard internal errors (#204)
- Remove redundant (|>) definition

* Mon Feb 19 2018 Christian Lindig <christian.lindig@citrix.com> - 1.35.0-1
- Strip whitespace, update deprecated String.{lowercase -> lowercase_ascii}

* Fri Feb 09 2018 Christian Lindig <christian.lindig@citrix.com> - 1.34.0-1
- Return updated device_config in SMAPIv2 SR.create call
- Remove duplicate default_vdi_info
- CP-24350: expose sharable flag to SMAPIv3 backends
- CA-272163: Introduce new exception when snapshot is called in the wrong place

* Wed Feb 07 2018 Christian Lindig <christian.lindig@citrix.com> - 1.33.0-1
- CP-26717: Port Gpumon interface from Camlp4 to PPX-based RPC scheme

* Fri Feb 02 2018 Christian Lindig <christian.lindig@citrix.com> - 1.32.0-1
- Refactor jbuilder test target
- Remove outdated INSTALL instructions, add CLI tool info to README
- coverage: be less smart
- Remove unused Camlp4 rewriter from clusterd jbuild
- Remove unused ppx_sexp_conv dependency from clusterd
- .coverage: bisects names are not unique
- Don't run cluster CLI during runtest
- Runtest now builds all CLI tools
- CA-281880 - travis: use coverage.sh from xapi-travis-scripts

* Wed Jan 31 2018 Christian Lindig <christian.lindig@citrix.com> - 1.31.0-1
- Use Lwt.bind instead of Lwt_unix.Versioned.bind_2
- Update opam dependencies for cmdliner and lwt
- Add clustering interface (#195)

* Fri Jan 26 2018 Christian Lindig <christian.lindig@citrix.com> - 1.30.0-1
- CP-26098: Port v6d interface from Camlp4 to PPX (#186)

* Wed Jan 24 2018 Christian Lindig <christian.lindig@citrix.com> - 1.29.0-1
- Makefile: do not use --dev in the release build
- Makefile: be explicit about the default goal

* Fri Jan 19 2018 Christian Lindig <christian.lindig@citrix.com> - 1.28.0-1
- CP-26471: Renamed library after porting it to jbuilder.
- coverage: fix compiler warning on unused variable

* Mon Jan 08 2018 Christian Lindig <christian.lindig@citrix.com> - 1.27.0-1
- The changes below provide support for vGPU migration
- CP-24185 add gpumon_if.get_pgpu_vgpu_compatibility
- CP-24185 add docstring for get_pgpu_vgpu_compatibility
- CP-24185 export get_vgpu_metadata from gpumon

* Mon Dec 18 2017 Christian Lindig <christian.lindig@citrix.com> - 1.26.0-1
- Storage_interface: add missing dependency in jbuild file
- Network_interface: remove unused functions

* Tue Dec 12 2017 Christian Lindig <christian.lindig@citrix.com> - 1.25.0-1
- updates_test: do not rely on json as a string but compare the Rpc structure

* Tue Dec 05 2017 Christian Lindig <christian.lindig@citrix.com> - 1.24.0-1
- CP-22945: runtime coverage dumping support for Xcp_service (#179)

* Wed Nov 01 2017 Rob Hoes <rob.hoes@citrix.com> - 1.23.0-1
- Add gpumon interface

* Tue Oct 24 2017 Rob Hoes <rob.hoes@citrix.com> - 1.22.0-1
- CP-24549: Add vusb to xenops_interface

* Fri Oct 13 2017 Rob Hoes <rob.hoes@citrix.com> - 1.21.0-1
- Rename VDI.export_changed_blocks to VDI.list_changed_blocks
- Add cbt_enabled parameter to vdi_info

* Thu Oct 12 2017 Rob Hoes <rob.hoes@citrix.com> - 1.20.0-1
- Port to jbuilder

* Tue Oct  3 2017 Edwin Török <edvin.torok@citrix.com> - 1.19.0-2
- CP-24962: convert to jbuilder

* Fri Sep 22 2017 Rob Hoes <rob.hoes@citrix.com> - 1.19.0-1
- CP-23093: Add igmp_snooping field for bridge
- Update compiler in travis file
- Travis: switch to docker env

* Fri Aug 11 2017 Rob Hoes <rob.hoes@citrix.com> - 1.18.0-1
- Add VDI.data_destroy call
- Add VDI.export_changed_blocks call

* Mon Jul 24 2017 Rob Hoes <rob.hoes@citrix.com> - 1.17.0-1
- Move memory interface to using ppx-based RPCs
- Add a memory CLI
- CA-259579: Introduce ballooning timeout before migration

* Mon Jul 03 2017 Rob Hoes <rob.hoes@citrix.com> - 1.16.0-1
- Add VDI.enable_cbt call
- Add VDI.disable_cbt call
- Add enable/disable CBT calls to Storage_skeleton

* Fri Jun 16 2017 Jon Ludlam <jonathan.ludlam@citrix.com> - 1.15.0-1
- Sync opam file with xs-opam

* Fri May 12 2017 Rob Hoes <rob.hoes@citrix.com> - 1.14.0-1
- Travis fixes
- README: add colorful icons
- Add updates, scheduler and task_server with unit tests and docs
- Prefer 'try find ... with _ ->' over 'if mem then find else ...'
- Update storage_interface to the new task signature
- Remove the global scheduler

* Thu Mar 16 2017 Rob Hoes <rob.hoes@citrix.com> - 1.13.0-1
- CP-20431: MxGPU in Xenops_interface.Vgpu

* Mon Mar 13 2017 Marcello Seri <marcello.seri@citrix.com> - 1.12.0-2
- Update OCaml dependencies and build/install script after xs-opam-repo split

* Mon Dec 12 2016 Gabor Igloi <gabor.igloi@citrix.com> - 1.10.0-1
- Fix OCaml compiler warnings
- Remove outdated INSTALL file; add INSTALL.md with generic build instructions

* Thu Oct 13 2016 Jon Ludlam <jonathan.ludlam@citrix.com> - 1.5.0-1
- New version - adds v6 interface

* Wed Sep 14 2016 Euan Harris <euan.harris@citrix.com> - 1.4.0-1
- Add force option to VM.start
- Add device information in VIF.state

* Wed Aug 17 2016 Christian Lindig <christian.lindig@citrix.com> - 1.3.0-1
- Update to 1.3.0; the interface to xenopsd changed

* Mon Jul 25 2016 Jon Ludlam <jonathan.ludlam@citrix.com> - 1.2.0-1
- Update to 1.2.0

* Mon Jul 4 2016 Euan Harris <euan.harris@citrix.com> - 1.1.0-1
- Update to 1.1.0

* Thu Apr 21 2016 Euan Harris <euan.harris@citrix.com> - 1.0.0-1
- Update to 1.0.0

* Wed Sep 9 2015 David Scott <dave.scott@citrix.com> - 0.14.0-1
- Update to 0.14.0

* Fri Aug 14 2015 David Scott <dave.scott@citrix.com> - 0.13.0-1
- Update to 0.13.0

* Fri Apr 24 2015 David Scott <dave.scott@citrix.com> - 0.11.1-1
- Update to 0.11.1
- Update to message-switch.0.11.0 API

* Sat Apr  4 2015 David Scott <dave.scott@citrix.com> - 0.10.0-1
- Update to 0.10.0

* Fri Apr  3 2015 David Scott <dave.scott@citrix.com> - 0.9.21-2
- Update to cohttp.0.15.2

* Wed Jan 21 2015 David Scott <dave.scott@citrix.com> - 0.9.21-1
- Update to 0.9.21

* Tue Oct 14 2014 David Scott <dave.scott@citrix.com> - 0.9.20-1
- Update to 0.9.20

* Wed Aug 20 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.9.18-1
- Update to 0.9.18

* Fri Jun 06 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.9.17-1
- Update to 0.9.17

* Mon Jun 02 2014 Euan Harris <euan.harris@citrix.com> - 0.9.16-2
- Split files correctly between base and devel packages

* Fri May  9 2014 David Scott <dave.scott@citrix.com> - 0.9.16-1
- Update to 0.9.16, with RRD fixes

* Fri Apr 25 2014 David Scott <dave.scott@eu.citrix.com> - 0.9.15-1
- Update to 0.9.15, now with vGPU and SR.probe

* Thu Sep 26 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.14-1
- Support searching for executables on the XCP_PATH as well as the PATH

* Wed Sep 25 2013 David Scott <dave.scott@eu.citrix.com>
- Logging, channel passing and interface updates

* Wed Sep 04 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.12-1
- Allow domain 0 memory policy to be queried

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

