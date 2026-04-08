# ERP Data Platform

## Overview
This project represents the design and architecture of a scalable ERP (Enterprise Resource Planning) data platform. The system supports core business operations including finance, inventory, sales, and reporting.

The goal is to demonstrate how to design a production-ready data system using modern data engineering principles.

## Objectives
- Design a normalized database schema for ERP operations
- Build scalable ETL pipelines for data processing
- Enable reliable reporting and analytics
- Ensure data consistency across multiple business domains

## System Architecture
The platform consists of the following layers:

1. **Source Systems**
   - Transactional ERP modules (Finance, Inventory, Sales)

2. **Data Storage**
   - Azure SQL Database
   - Normalized schema for operational data

3. **ETL Layer**
   - Data extraction, transformation, and loading
   - Batch processing pipelines

4. **Analytics Layer**
   - Reporting-ready datasets
   - Aggregations for business intelligence

## Key Components

### ERP Modules
- Finance (accounts, transactions, payments)
- Inventory (products, stock, movements)
- Sales (orders, customers, invoices)

### Data Modeling
- Fully normalized schema for operational efficiency
- Designed relationships between business entities
- Ensured data integrity and consistency

### ETL Pipelines
- Data ingestion from operational systems
- Transformation logic for reporting
- Scheduled batch processing

## Technologies Used
- SQL
- Python
- Azure SQL Database
- ETL Pipelines

## Design Approach
This project focuses on system design and architecture rather than implementation details. It reflects real-world experience building ERP data systems under production constraints.

## Note
Due to NDA restrictions, this repository does not include production code. Instead, it focuses on architecture, data modeling, and system design.
