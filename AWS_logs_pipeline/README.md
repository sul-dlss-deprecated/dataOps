# Operationalizing AWS / Building Logs Aggregation Data Pipeline Project

*September-October 2017*

## Team

- Erin, DevOps
- Christina, DataOps

## Vision & Goals

From devOps: Test streaming architecture
- Kinesis or Kafka: handle data pipelines from producers to consumers
- AWS Services & Terraform builds
- Support log shipping as an example of this to further inform
- What things are hitting infrastructure services

From dataOps:
- Ability to write more any data pipeline(s)
- Testing how to monitor data state

Proof of Concept: Logs shipping (of what interfaces? To what interfaces? What reports are key here and require what transforms)
- Lining up next “pipelines”
  - Lyberservices
  - Preservation Core Logs to PREMIS Events
  - Object State Dashboard
- Other analyses to do on logs / other dashboards to output etc.

## Open Questions to Answer

- AWS proprietary toolkit versus other services?
  - i.e. kinesis, lamba vs kafka, …?
  - EMR vs Spark
- Ease or value of writing data pipelines in this framework?
  - Where to manage transforms? Retrieval? Output? Etc.
- Data retention concerns on Elasticsearch side
- Monitoring of logging from kinesis
- Having good insight into the activity of the streams & transforms
- Expense of running this & comparing to what we have

## MVP for Logs Aggregation Pilot

Reports / questions to ask of logs:
- Who queries what services? (How to define who here?)
- How often, broken down across querying agents or given timeframes?
- What queries? What frequency of queries?
- What queries are issued by the agent?

See [our issue on what services' logs to target for this MVP](https://github.com/sul-dlss/dataOps/issues/5).

See [this write-up on logs aggregation pipeline proof of concept overlap with the SDR Preservation Core Catalog work cycle.](https://docs.google.com/document/d/1Gxi73V2TfZviOIc6yr4cEpcUWN55Jowcgu93VxoxrIY/edit)

## Resources

Migrated to the [DataOps wiki](https://github.com/sul-dlss/dataOps/wiki)


## Plan

See the [DataOps Issues with tag 'logs proof of concept'](https://github.com/sul-dlss/dataOps/issues?q=is%3Aissue+label%3A%22logs+proof+of+concept%22).
