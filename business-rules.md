# Business Rules

## Finance
- Each transaction must be linked to an account
- Transactions must be balanced (debit = credit)
- Payments must reference invoices

## Inventory
- Stock levels cannot be negative
- Each product must have a unique identifier
- Inventory movements must be tracked

## Sales
- Each order must be linked to a customer
- Orders must contain at least one product
- Invoices are generated per completed order

## Data Integrity
- Foreign key constraints enforced
- No duplicate primary records
- Consistent timestamps for all records
