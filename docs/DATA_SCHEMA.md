# Data Schema Reference

## Input Data Schema

| Field        | Type   | Description                                   |
|--------------|--------|-----------------------------------------------|
| user_id     | String | Unique identifier for the user                |
| income       | Float  | User's total income for the tax year         |
| deductions   | Float  | Total deductions applicable to the user       |
| tax_credits  | Float  | Tax credits available to the user             |

## Output Data Schema

| Field              | Type   | Description                               |
|--------------------|--------|-------------------------------------------|
| user_id           | String | Unique identifier for the user            |
| calculated_tax    | Float  | Amount of tax calculated based on inputs  |
| net_income        | Float  | Net income after tax deductions            |
| status            | String | Status of the tax calculation operation    |