# Spotify End-To-End Data Pipeline

This project demonstrates how to build an end-to-end data pipeline for Spotify streaming data, implemented in 4 different ways using various AWS and data engineering tools.

| Version | Tools & Tech Stack |
|---------|--------------------|
| 1 | Lambda → S3 → Athena |
| 2 | Lambda → S3 → Glue → Athena |
| 3 | Apache Airflow |
| 4 | Airflow → Spark → Snowflake |

Each version is organized in its own folder with instructions.

## Project Goal

- Ingest Spotify data.
- Store raw data on S3.
- Process data.
- Load data to Athena or Snowflake for analytics.

Explore each version to learn different ways to design and orchestrate modern data pipelines.
