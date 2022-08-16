%global debug_package %{nil}

Name:           ocaml-xcp-idl
Version:        1.96.4
Release:        1%{?dist}
Summary:        Common interface definitions for XCP services
License:        LGPL
URL:            https://github.com/xapi-project/xcp-idl

Source0: https://code.citrite.net/rest/archive/latest/projects/XSU/repos/xcp-idl/archive?at=v1.96.4&format=tar.gz&prefix=ocaml-xcp-idl-1.96.4#/xcp-idl-1.96.4.tar.gz


Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XSU/repos/xcp-idl/archive?at=v1.96.4&format=tar.gz&prefix=ocaml-xcp-idl-1.96.4#/xcp-idl-1.96.4.tar.gz) = e9d1357cece33b37847392ce44a11ee736413546

BuildRequires:  xs-opam-repo
BuildRequires:  message-switch-devel

%global _use_internal_dependency_generator 0
%global __requires_exclude *caml*

%description
Common interface definitions for XCP services.

%package        devel
Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XSU/repos/xcp-idl/archive?at=v1.96.4&format=tar.gz&prefix=ocaml-xcp-idl-1.96.4#/xcp-idl-1.96.4.tar.gz) = e9d1357cece33b37847392ce44a11ee736413546
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       message-switch-devel%{?_isa}
Requires:       xs-opam-repo

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%global ocaml_libdir %{_opamroot}/ocaml-system/lib
%global build_ocaml_libdir %{buildroot}%{ocaml_libdir}

%prep
%autosetup -p1

%build
make %{?coverage:runtime-coverage}

%check
make test

%install
DESTDIR=${RPM_BUILD_ROOT} %{__make} install

# this is to make opam happy
mkdir -p %{build_ocaml_libdir}/xapi-idl
touch %{build_ocaml_libdir}/xapi-idl/opam.config

%files
%doc MAINTAINERS
%doc %{ocaml_libdir}/../doc/xapi-idl/CHANGES
%doc %{ocaml_libdir}/../doc/xapi-idl/LICENSE
%doc %{ocaml_libdir}/../doc/xapi-idl/README.md
%{ocaml_libdir}/xapi-idl
%{ocaml_libdir}/stublibs/*.so
%exclude %{ocaml_libdir}/xapi-idl/*.a
%exclude %{ocaml_libdir}/xapi-idl/*.cmx
%exclude %{ocaml_libdir}/xapi-idl/*.cmxa
%exclude %{ocaml_libdir}/xapi-idl/*.cmxs
%exclude %{ocaml_libdir}/xapi-idl/*.mli
%exclude %{ocaml_libdir}/xapi-idl/*.cmt
%exclude %{ocaml_libdir}/xapi-idl/*.cmti
%exclude %{ocaml_libdir}/../doc/xapi-idl
%exclude %{ocaml_libdir}/xcp/*
%exclude %{ocaml_libdir}/../doc/xcp

%files devel
%{ocaml_libdir}/xapi-idl/*.a
%{ocaml_libdir}/xapi-idl/*.cmx
%{ocaml_libdir}/xapi-idl/*.cmxa
%{ocaml_libdir}/xapi-idl/*.cmxs
%{ocaml_libdir}/xapi-idl/*.mli

%changelog
* Tue May 17 2022 Christian Lindig <christian.lindig@citrix.com> - 1.96.4-1
- CA-363633: Always take the generation-id directly from xapi
- CA-361220: xenopsd: introduce TASK.destroy_on_finish
- Remove CPUID levelling v1 compat code
- Add featureset to xenopsd VM state

* Mon Sep 27 2021 Pau Ruiz Safont <pau.safont@citrix.com> - 1.96.2-2
- Bump package after xs-opam update

* Mon Aug 23 2021 Pau Ruiz Safont <pau.safont@citrix.com> - 1.96.2-1
- CP-38064: compatibility with rpclib 7

* Tue Jul 13 2021 Edwin Török <edvin.torok@citrix.com> - 1.96.1-2
- bump packages after xs-opam update

* Thu Feb 11 2021 Ben Anson <ben.anson@citrix.com> - 1.96.1-1
- CP-35026 optionally include client info in logs
- CA-347560: Add VM.import_metadata_async

* Fri May 29 2020 Christian Lindig <christian.lindig@citrix.com> - 1.96.0-1
- maintenance: formatting fixes
- maintenance: fix (deprecation) warnings
- maintenance: drop unused Scheduler code
- CA-338201: use a more efficient way of splitting a map
- Optimization: store handles in the map
- Optimization: do not build intermediate list
- CA-338201: use mtime
- CA-337546: use a single persistent pipe per scheduler, avoid using
	pipes in Delay.wait
- CA-337546: add mtime to opam file

* Tue May 19 2020 Christian Lindig <christian.lindig@citrix.com> - 1.95.0-1
- maintenance: remove ambiguity of doc comment
- maintenance: Tweak comments
- Maintenance: add ocamlformat configuration
- maintenance: update dune to 2.0
- format: format using ocamlformat 0.14
- maintenance: reformat comments with stars in them

* Tue Apr 14 2020 Christian Lindig <christian.lindig@citrix.com> - 1.94.0-1
- add Sriov.enable_action_result Manual_successful, for manual sr-iov/vf
	configuration support
- Revert "add Sriov.enable_action_result Manual_successful, for manual
	sr-iov/vf configuration support"

* Mon Mar 23 2020 Christian Lindig <christian.lindig@citrix.com> - 1.93.0-1
- Remove bisect_ppx instrumentation
- CA-337000 escape non-printable characters in log msgs

* Thu Mar 12 2020 Christian Lindig <christian.lindig@citrix.com> - 1.92.0-1
- CP-33058 create a centralized cipher string

* Mon Mar 02 2020 Christian Lindig <christian.lindig@citrix.com> - 1.91.0-1
- Improve reliability of scheduler tests
- CA-334912: Allow DMC in PV Shim

* Tue Jan 28 2020 Christian Lindig <christian.lindig@citrix.com> - 1.89.0-1
- REQ-627 CA-333495 add PCI.dequarantine

* Mon Jan 06 2020 Christian Lindig <christian.lindig@citrix.com> - 1.88.0-1
- maintenance: replace references to pervasives module
- ci: use configuration from xs-opam
- CA-328130 add speed to Vusb record

* Mon Dec 09 2019 Christian Lindig <christian.lindig@citrix.com> - 1.87.0-1
- maintenance: use ocamldoc's tags
- maintenance: fix unintended bad markup in the docs

* Mon Nov 18 2019 Christian Lindig <christian.lindig@citrix.com> - 1.86.0-1
- CP-32446: Introduce Xen.features_pv_host and Xen.features_hvm_host

* Mon Oct 14 2019 Christian Lindig <christian.lindig@citrix.com> - 1.85.0-1
- Merge REQ-627 SR-IOV support for NVidia GPUs

* Tue Oct 01 2019 Christian Lindig <christian.lindig@citrix.com> - 1.84.0-1
- Merge changes for Xen 4.13

* Thu Sep 26 2019 Igor Druzhinin <igor.druzhinin@citrix.com> - 1.83.0-1
- CA-327265: Modify shim_mib formula for Xen 4.13

* Tue Sep 24 2019 Christian Lindig <christian.lindig@citrix.com> - 1.82.0-1
- CA-326244: Debug: Remove unnecessary facility mutex
- CA-326244: Debug: Remove unused get_all_debug_keys and its mutex
- CA-326244: don't take thread local table lock during logging
- CA-326244: do not include host name in log format
- CA-326244: Leave hostname empty for now instead of removing its entry
- Reduce Debug interface
- Move tests to alcotest

* Wed Sep 18 2019 Christian Lindig <christian.lindig@citrix.com> - 1.81.0-1
- CA-326244: Store debug levels in Set ref and do not take lock during logging

* Mon Sep 09 2019 Christian Lindig <christian.lindig@citrix.com> - 1.80.0-1
- CA-325843: Modify pv-shim (Xen 4.12) memory requirements

* Fri Aug 23 2019 Edwin Török <edvin.torok@citrix.com> - 1.79.0-2
- bump packages after xs-opam update

* Thu Aug 15 2019 Christian Lindig <christian.lindig@citrix.com> - 1.79.0-1
- CA-322204: enable critical logging
- Fix PCI function address formatting .%02x -> .%x
- maintenance: Replace \r (DOS) by \n (Unix) line endings
- maintenance: do not depend on bisect_ppx
- maintenance: ounit and alcotest are test-only deps

* Wed Aug 07 2019 Christian Lindig <christian.lindig@citrix.com> - 1.78.0-1
- Simplify Makefile
- Update storage_test so that it builds with dune build @all
- Build storage_test always so it does not bitrot

* Fri Aug 02 2019 Christian Lindig <christian.lindig@citrix.com> - 1.77.0-1
- CP-31450: Add domid to Datapath.attach

* Wed Jul 10 2019 Christian Lindig <christian.lindig@citrix.com> - 1.76.0-1
- Avoid deprecated Re.get_all_ofs
- Silence preprocess warnings

* Tue Jun 25 2019 Christian Lindig <christian.lindig@citrix.com> - 1.75.0-1
- CA-321983: use defaults or options for new nvidia vgpu fields

* Thu Jun 06 2019 Christian Lindig <christian.lindig@citrix.com> - 1.74.0-1
- Simplify Travis setup

* Wed Jun 05 2019 Christian Lindig <christian.lindig@citrix.com> - 1.73.0-1
- REQ-720: CP-31058: Update nvidia type.
- CP-31160: Add 'config_file' back to IDL.
- CP-31122: Add uuid in interface between Xapi and Xenopsd.
- CP-31124: Add uuid in interface between Xapi and Gpumon.
- CP-31321: Support extra_args for vGPU configuration

* Wed May 08 2019 Christian Lindig <christian.lindig@citrix.com> - 1.72.0-1
- Fix creation of default Vif.t

* Tue Jan 29 2019 Christian Lindig <christian.lindig@citrix.com> - 1.71.0-1
- CP-30508: Add iommu capability to Host information
- Add whether host supports hvm to Host information

* Wed Jan 23 2019 Christian Lindig <christian.lindig@citrix.com> - 1.70.0-1
- Prepare for Dune 1.6

* Tue Jan 22 2019 Christian Lindig <christian.lindig@citrix.com> - 1.69.0-1
- CA-307829: XSI-216 Add active state to VGPU
- CA-272180: allow reporting of suspend ack failures
- CA-272180: allow reporting of suspend timeouts
- maintenance: whitespace

* Fri Jan 11 2019 Christian Lindig <christian.lindig@citrix.com> - 1.68.0-1
- Deprecated package rrd in favour of xapi-rrd. (#261)

* Tue Dec 18 2018 Christian Lindig <christian.lindig@citrix.com> - 1.67.0-1
- CP-29967: sandboxing support for varstored
- CP-29967: add tests for varstore interfaces
- CA-302981: Add a timeout to varstored-guard RPC calls
- CP-30032: add path to varstore.privileged.destroy
- add missing tests for cluster and v6 interfaces
- Travis: use OCaml 4.07

* Tue Dec 04 2018 Christian Lindig <christian.lindig@citrix.com> - 1.66.0-1
- Reference xapi-inventory instead of xcp-inventory; the latter is being
  deprecated. (#256)

* Wed Nov 28 2018 Konstantina Chremmou <konstantina.chremmou@citrix.com> - 1.65.0-2
- xcp deprecated in favour of xapi-idl

* Tue Nov 27 2018 Christian Lindig <christian.lindig@citrix.com> - 1.65.0-1
- Register printer for Xmlm errors
- .travis.yml: use debian-9 instead of debian-testing

* Fri Nov 16 2018 Christian Lindig <christian.lindig@citrix.com> - 1.64.0-1
- Switch to new ocaml-rpc interface
- Switch xen/jbuild to updated way to specify ppxs

* Thu Nov 01 2018 Christian Lindig <christian.lindig@citrix.com> - 1.63.0-1
- Update opam files for Opam 2

* Thu Oct 11 2018 Rob Hoes <rob.hoes@citrix.com> - 1.62.0-1
- CP-28301, CP-28659, CP-28662: add firmware type and NVRAM parameter for xenopsd

* Tue Oct 09 2018 Christian Lindig <christian.lindig@citrix.com> - 1.61.0-1
- Fix unit test after introduction of cancellable field
- Travis: test the xcp package not the dummy package

* Thu Oct 04 2018 Christian Lindig <christian.lindig@citrix.com> - 1.60.0-1
- network_interface: add Bridge_does_not_exist error

* Mon Oct 01 2018 Christian Lindig <christian.lindig@citrix.com> - 1.59.0-1
- storage_interface: add implementations_of_backend helper from xapi
- network_interface: add Interface_does_not_exist error

* Wed Sep 26 2018 Christian Lindig <christian.lindig@citrix.com> - 1.58.0-1
- CA-290696: Add field cancellable for task

* Mon Sep 24 2018 Christian Lindig <christian.lindig@citrix.com> - 1.57.0-1
- CP-27110: PPX the storage interface

* Mon Sep 17 2018 Christian Lindig <christian.lindig@citrix.com> - 1.56.0-1
- Use Dune, update opam files
- Fix clerical error of xenops exception - report correct module

* Wed Sep 05 2018 Christian Lindig <christian.lindig@citrix.com> - 1.55.0-1
- jbuild: remove ppx_deriving_rpc from libraries
- Fix unit tests: add missing functions
- Convert xenops interface from camlp4 to new ppx style
- Fix Travis: Use DISTRO=debian-testing to work around curl error

* Tue Aug 21 2018 Christian Lindig <christian.lindig@citrix.com> - 1.54.0-1
- Task/Updates: Remove dependence on camlp4 style interfaces
- Remove calls to ocamlfind from within jbuild files

* Mon Aug 13 2018 Christian Lindig <christian.lindig@citrix.com> - 1.53.0-1
- CP-29027: cluster_interface: Add startup_finished to diagnostics

* Thu Jul 05 2018 Christian Lindig <christian.lindig@citrix.com> - 1.52.0-1
- CA-292641: Collect log messages from libs using Logs
- CA-292641: debug: use private buffer for logs formatter

* Fri Jun 29 2018 Christian Lindig <christian.lindig@citrix.com> - 1.51.0-1
- Fix build with rpclib 5.8.0

* Thu Jun 28 2018 Christian Lindig <christian.lindig@citrix.com> - 1.50.0-1
- CP-28132: Remove domain_uuid from attach result
- Add new attach interface from SMAPIv3
- Mark old VDI.attach as deprecated in docstring
- storage_interface: Add helper to parse NBD uri
- storage_interface: Add test for parse_nbd_uri helper
- Fix build with rpclib 5.8.0

* Tue Jun 05 2018 Christian Lindig <christian.lindig@citrix.com> - 1.49.0-1
- CP-28365: do not lose the exception text in log_and_ignore_exn

* Tue May 29 2018 Christian Lindig <christian.lindig@citrix.com> - 1.48.0-1
- xcp: update and simplify interface using fd-send-recv >= 2.0.0
- posix_channel: make it even clearer that the token is a throwaway buffer
- lib/channel_helper: Lwt_unix requires bytes
- lib/channel_helper: use bytes for the io_vector
- move the standalone tool channel_helper to misc

* Thu May 24 2018 Christian Lindig <christian.lindig@citrix.com> - 1.47.0-1
- CA-289145: Close socket if error occurs when connecting
- xcp-idl: port to safe-strings
- network: make safe-string compliant
- lib/cohttp_posix_io: avoid bytes where possible
- lib/xcp_service: be more conservative with unsafe_of_string

* Fri May 18 2018 Christian Lindig <christian.lindig@citrix.com> - 1.46.0-1
- Fix compilation of vdi_automaton_test

* Mon May 14 2018 Christian Lindig <christian.lindig@citrix.com> - 1.45.0-1
- vdi_automaton: extract test into a runnable test
- xcp.opam, {storage,xen}/jbuild: use the new rpc 5.0.0 and rpclib-legacy

* Thu May 10 2018 Christian Lindig <christian.lindig@citrix.com> - 1.44.0-1
- CP-26583: Derive RPC type for auxiliary types
- CP-26583: Port Rrd client to PPX
- CP-26583: Add Rrdd debugging CLI
- CP-26583: Rrd: Build debug CLI, remove Camlp4 dependency
- CP-26583: Port Rrdd interface to use PPX-based RPCs
- CP-26583: Update docstrings, client gen and error type
- CP-26583: Add protocol-string conversion helpers, add protocol error,
            update docstrings
- CP-26583: Update Rrd interface formatting and docstrings
- CP-26583: Don't discard internal errors
- CP-26583: Remove old rrd_idl_test and move test data to be ppx friendly
- CP-26583: Generalize idl tests over marshaller
- CP-26583: Add (failing) test of rrd interface
- CP-26583: Fix things until the RRD tests pass.
- CP-26583: Update RRD interface doc strings
- CP-26583: Register Rrdd PPX error printer, minor changes
- rrd_interface: fix type used in printer

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

