# API-Forward SDR3 Analysis & Implementation Work Cycle

*(proposal being written for possible start later this fall / early this winter)*

There are a few converging areas of need in this proposal:

- having a devOps & dataOps work cycle to continue to build out:
  - analysis and implementations of select components into a data API-forward architecture for DLSS,
  - getting production-ready / operationalizing our AWS usage, and
  - consolidating analysis on the current state and desired shifts of our existing infrastructure around SDR.
- pulling together and push forward analysis of future SDR system requirements outside of the Hydrox demo, then matching that with design and at least one major example of a component of the SDR data architecture and infrastructure migrated to a data-forward, API-reliant and cloud-based codebase.

## Goals:

- kick start "SDR3" work (outside of Hydrox) by
  - being a parallel effort to Hydrox, which needs this work to understand interfaces between current & future SDR to Hydrox
  - begin to define the requirements & business cases for components of SDR and their future form
  - offer more details & options to the emerging Chimera reboot (digital library review) and data architecture meeting(s)
- generate and share understanding on our current systems (including ability to work with components for a phased replacement plan)
  - interview infrastructure practitioners on current pain points on current infrastructure (a "SDR2" retrospective)
  - compile list of lessons learned
  - reverse engineer specs and requirement lists for current digital library system needs (based on interviews and Current State work)
- explore a data oriented, event driven architecture to process some identified component of SDR ready / supportive of an early shift
  - generate a set of conceptual diagrams and documentation of concerns approached (including data API specification guidelines)
  - generate a wireframe of a strategic plan for migration to data APIs and SDR3 components in a AWS deployment environment

## User Stories / Business Value(s):

- As an engineer, I would like to know what services (current or ideal) the Hydrox implementation can leverage OR what services are needed and are not present in the current architecture.
- As a SDR services manager, I would like to have list of requirements and related work around SDR components to be able to plan future work around SDR services such as (but not limited to):
  - faster/more transparent/advanced user-driven object accessioning ;
  - more flexible support for metadata & repository object model extensions ;
  - easier delivery of SDR repository objects to downstream, user-facing services like Spotlight ;
  - etc.
- As an accessioning manager, I would like to have a more coordinated set of accessioning into SDR components tools and workflows for adding new types of, new sources of, or large (in either discrete set number or single object file size) objects.
- As an operations engineer, I would like to gather requirements on operations-related needs when moving identified SDR components to a server-less infrastructure or cloud-based architecture.

## Informed by Current Work:

- [Current State](https://github.com/sul-dlss/sdr_current_state)
- [Operationalizing AWS / Logs Data Aggregation](https://github.com/sul-dlss/dataOps/tree/master/AWS_logs)

## Informs Future or Parallel Work:

- SDR3 & API Infrastructure Shift
- Hydrox <=> SDR Interfaces & Connections

## Proposed Timeframe:

2 months

## Proposed Team:

- Mark Matienzo, PO (proposed)
- Erin Fahy, Team Lead / DevOps
- Christina Harlow, DataOps
- Chris Beer, engineer (proposed)
- Ben Albritton, key stakeholder
- An engineer or two to represent the Infrastructure team (Justin?)
