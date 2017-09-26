# Operationalizing AWS / Building Logs Aggregation Data APIs & Flow Project

*September-October 2017*

## Team

- Erin, DevOps
- Christina, DataOps

## Vision & Goals

From devOps: Operationalize AWS
- AWS Services & Terraform builds
- What things are hitting infrastructure services
- More details lined up in the SprintOps docs and eventually in the DevOps / Ops Terraform repo

From dataOps:
- Kinesis or Kafka: handle data from producers to consumers leveraging APIs
- Testing how to monitor data state
- Support log shipping as an example of this to further inform implementation of AWS and data API design concerns
- Project: Logs shipping
  - Lining up & implementing log data flows, APIs, reporting / analytic interfaces within AWS
  - Other analyses to do on logs / other dashboards to output etc.

## DataOps-focused Open Questions to Answer

- AWS proprietary toolkit versus other services?
  - i.e. kinesis, lamba vs kafka, …?
  - EMR vs Spark
- Ease or value of writing data APIs & transforms in this framework?
  - Where to manage transforms? Mappings? Producers? Consumers? etc.
- Data retention concerns on Elasticsearch side
- Monitoring of logging from Kinesis
- Having good insight into the activity of the streams & transforms
- Expense of running this & comparing to what we have

## MVP for Logs Aggregation

Reports / questions to ask of logs:
- Who queries what services? (How to define who here?)
- How often, broken down across querying agents or given timeframes?
- What queries? What frequency of queries?
- What queries are issued by the agent?

See [our issue on what services' logs to target for this MVP](https://github.com/sul-dlss/dataOps/issues/5).

See [this write-up on logs aggregation data mechanism overlap with the SDR Preservation Core Catalog work cycle.](https://docs.google.com/document/d/1Gxi73V2TfZviOIc6yr4cEpcUWN55Jowcgu93VxoxrIY/edit)

## DataOps & AWS Resources

Migrated to the [DataOps wiki](https://github.com/sul-dlss/dataOps/wiki)


## DataOps Work Plan

See the [DataOps Issues with tag 'logs aggregation'](https://github.com/sul-dlss/dataOps/labels/logs%20aggregation).
