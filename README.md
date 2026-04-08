# ERP Data Platform

## Overview

This project represents the design of a centralized ERP data platform built for a manufacturing company with five distinct business divisions. The platform unified operational, financial, and reporting data into one system, enabling management to track saldo in, saldo out, dashboards, KPI metrics, and performance statistics across the organization.

## Documentation

* [Architecture Details](./architecture.md)
* [Business Rules](./business-rules.md)
* [ERP Workflows](./workflows.md)

* ## Architecture Diagram

[ERP Architecture](./images/erp-architecture-diagram.png)


## Business Context

This ERP platform was designed for a manufacturing company operating across five distinct business divisions:

- Door and frame manufacturing
- Heating radiator manufacturing
- Sanitary ware and plumbing product manufacturing
- Kitchen furniture manufacturing
- Window manufacturing

The system centralized financial, operational, and reporting data from all five divisions into one unified platform. This allowed leadership to monitor business performance, accounting flows, saldo in, saldo out, KPI metrics, and operational statistics in a single program.

## My Contributions

- Designed and developed a centralized ERP data platform for five manufacturing business divisions
- Built a unified data model to consolidate operational and financial records across all business units
- Developed reporting structures for saldo in / saldo out analysis and management visibility
- Enabled centralized dashboards, statistics, and cross-division performance monitoring
- Designed role-based access logic for different organizational levels
- Implemented KPI-related reporting functionality for employee and department performance tracking
- Developed complex financial reporting, transaction control logic, and approval workflows for enterprise-grade ERP operations

 ## Access Control & KPI Management

The ERP platform included role-based access controls and KPI monitoring functionality to support organizational hierarchy and secure data visibility.

### Access Management
- Executive-level users such as directors, founders, and shareholders had access to consolidated financial dashboards including saldo in / saldo out across all business divisions
- Department managers and operational staff had restricted access based on role and department
- Sensitive financial and strategic reporting was limited to authorized leadership roles only

### KPI Functionality
- Employee and department performance metrics were tracked within the system
- KPI dashboards enabled management to evaluate operational effectiveness
- Performance indicators were segmented by department and business unit

  ## Advanced Financial & Control Features

The ERP platform included enterprise-grade financial controls and operational safeguards designed for complex business workflows.

### Key Capabilities
- Audit logs for tracking historical changes and user activity
- Permission controls by transaction type and operational role
- Multi-level transaction validation and approval workflows
- Internal transfer processing between business units or accounts
- Accounting and finance reporting for operational and management visibility

## Objectives

- Design a centralized ERP platform for multi-division manufacturing operations
- Consolidate operational and financial data into one system
- Enable secure role-based access across organizational levels
- Support KPI tracking, accounting visibility, and executive reporting
- Provide reliable reporting and analytics across all business units

## System Architecture

The platform consists of the following logical layers:

1. **Business Units**
   - Five manufacturing divisions generating operational and financial data

2. **Central ERP Data Layer**
   - Unified storage for transactional, accounting, and reporting data

3. **Processing Layer**
   - Validation, transformation, reporting, and control logic

4. **Access & Reporting Layer**
   - Dashboards, KPI views, saldo in / saldo out reporting, and role-based visibility

## Key Components

### Business Units
- Doors & Frames Manufacturing
- Heating Radiators Manufacturing
- Sanitary Ware & Plumbing Products
- Kitchen Furniture Manufacturing
- Window Manufacturing

### Reporting & Visibility
- Consolidated dashboards
- Saldo in / saldo out reporting
- Cross-division business statistics
- KPI-based performance tracking

### Access Control
- Role-based permissions
- Restricted reporting access by position
- Transaction-level control rules

### Financial Control
- Audit logs
- Internal transfers
- Multi-level transaction validation
- Accounting-oriented reporting

## Technologies Used

### Core Technical Expertise
- SQL
- Azure SQL Database
- PL/SQL Developer
- Data Modeling
- Database Normalization
- Database Architecture

### ERP & Financial Logic
- Financial Workflow Automation
- Accounting Logic
- KPI Management
- Enterprise Reporting Architecture
- Operational Control Logic

### Security & Controls
- Role-Based Access Control (RBAC)
- Audit Logging
- Transaction Validation
- Internal Transfer Controls
- Multi-Level Approval Workflows

### Reporting & Analytics
- Power BI
- KPI Reporting
- Management Dashboard Design

### Platform / Collaboration Exposure
- Java / C#
- ASP.NET / Node.js
- React / JavaScript / Bootstrap
- Azure Data Factory / Azure Synapse
- API Integrations

## Design Approach

This project focuses on system design, business logic, reporting architecture, and enterprise-grade operational controls. It reflects real-world experience building a centralized ERP platform for a complex manufacturing business with multiple divisions, layered permissions, KPI monitoring, and advanced financial workflows.

## Note

Due to NDA restrictions, this repository does not include production code. Instead, it focuses on architecture, business logic, data modeling, reporting structure, and system design.


