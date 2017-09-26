# SDR3 Ingest Pipeline / DataDevops SDR3 Work Cycle

*(proposal being written for possible start later this fall?)*

There are three converging areas of need in this proposal. One is having a devOps / dataOps work cycle to continue to build out analysis and work around data API-forward architecture for DLSS, setting up & documenting server-less infrastructure leveraging AWS, and consolidating analysis on the current state and desired shifts of our existing infrastructure in terms of operations, data systems, and software/codebases. The second area is to pull together and push forward analysis of SDR3 requirements outside of the Hydrox demo, then matching that with design and at least one major example of a portion of SDR architecture and infrastructure migrated to a data-forward, API-reliant and cloud-based codebase. The third is the currently on hold reset of the Google Books accessioning pipeline, which requires a full rewrite of its current ingest and accessioning processes into SDR. Due to its size (over 2 million digital books) and backlog status, the Google books accessioning pipeline is an ideal candidate for a test of purpose and design of the first two work areas.

## Goals:

- kick start SDR3 work by
  - being a parallel effort to Hydrox, which needs this work to understand interfaces between current & future SDR to Hydrox
  - begin to define the requirements & business cases for SDR3 planning & work
  - offer more details & options to the emerging chimera reboot (digital library review) and data architecture meeting(s)
- generate and share understanding on our current systems (including ability to work with components for a phased replacement plan)
  - interview infrastructure practitioners on current pain points on current infrastructure (a "SDR2" retrospective)
  - compile list of lessons learned
  - reverse engineer specs and requirement lists for current digital library system needs (based on interviews and Current State work)
- explore a data oriented, event driven architecture to process some data object that we currently accession via the SDR ‘pipeline’
  - build a Google books ingest pipeline to vet the said approach
  - generate a set of conceptual diagrams and documentation of concerns approached
  - generate a wireframe of a strategic plan for migration to said approach

## User Stories / Business Value(s):

- (being written)

## Informed by Current Work:

- Current State
- Data Pipeline Proof of Concept

## Informs Future Work:

- SDR3 & API Infrastructure Shift
- Activity & Data Tracking & Analytics

## Proposed Timeframe:

2 months?

## Proposed Team:

- Mark Matienzo PO ?
- Erin Fahy Team Lead / DevOps
- Christina Harlow DataOps
- Chris Beer?
- Ben Albritton as a key stakeholder to check in with
- Infra Devs representation?
