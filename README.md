# E-Commerce Customer Insights

A comprehensive analytics and recommendation engine for e-commerce platforms that extracts customer insights from transactional data, computes business metrics, and powers product recommendations through graph-based analysis.

## Features

- **Data Ingestion**: Extract customer, product, and order data from MySQL
- **Customer Analytics**: 
  - Compute Customer Lifetime Value (CLV) by user
  - Calculate category-level revenue analysis
  - Determine product affinity scores
- **Product Recommendations**: Generate co-purchase recommendations based on transaction patterns
- **Graph Database Integration**: Store and query relationships using Neo4j
- **Power BI Export**: Export computed metrics for business intelligence visualization
- **Extensible Pipeline**: Modular ETL pipeline for easy enhancement and maintenance

## Prerequisites

- Python 3.7+
- MySQL Server (local or remote)
- Neo4j Database (local or remote)
- pip or conda for dependency management

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd ecommerce-customer-insights
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

**Dependencies**:
- `mysql-connector-python` - MySQL database connectivity
- `neo4j` - Neo4j graph database driver
- `pandas` - Data manipulation and analysis
- `numpy` - Numerical computing
- `pyyaml` - Configuration file parsing
- `python-dotenv` - Environment variable management

### 3. Set Up MySQL Database

```bash
# Run the setup script to create database and tables
mysql -u root -p < db/mysql/setup_mysql.sql

# (Optional) Load sample data for testing
mysql -u root -p ecommerce_db < db/mysql/seed_sample_data.sql
```

### 4. Set Up Neo4j Database

Connect to your Neo4j instance and run the constraint and schema setup scripts:

```bash
# Load constraints and relationship definitions
# See db/neo4j/cypher/ for available scripts
```

### 5. Configure Application

Edit `config/config.yaml` with your database credentials and settings:

```yaml
mysql:
  host: localhost          # MySQL server hostname
  port: 3306               # MySQL server port
  user: root               # Database username
  password: Jasmine@123    # Database password
  database: ecommerce_db   # Database name

neo4j:
  uri: bolt://localhost:7687  # Neo4j connection URI
  user: neo4j                 # Neo4j username
  password: Jasmine@123       # Neo4j password

pipeline:
  export_dir: data/exports           # Output directory for exports
  min_copurchase_count: 2            # Minimum co-purchases for recommendations
  recommendation_limit: 10           # Max recommendations per product
```

## Usage

### Using the CLI Interface (Recommended)

The project provides a modular CLI for flexible pipeline execution:

```bash
# Run all pipeline stages
python -m src.cli run_all

# Or run individual stages
python -m src.cli ingest         # Extract data from MySQL
python -m src.cli analyze        # Compute metrics (category revenue, CLV, affinity scores)
python -m src.cli graph          # Load data into Neo4j
python -m src.cli export         # Export metrics to CSV files
```

Each command loads the necessary data and executes its stage of the pipeline.

### Using the Orchestration Script (Legacy)

For automated execution of the complete pipeline:

```bash
python -m src.main
```

This executes the complete data pipeline:
1. **Data Extraction**: Fetches users, products, and orders from MySQL
2. **Analytics Computation**:
   - Category revenue breakdown
   - Customer lifetime value (CLV) per user
   - Product affinity scores
   - Co-purchase pairs for recommendations
3. **Data Export**: Exports metrics to `data/exports/` for Power BI integration
4. **Graph Storage**: Upserts relationships to Neo4j for relationship queries

### Run Local Validation Checks

```bash
bash scripts/run_local_checks.sh
```

### Run ETL with Custom Parameters

```bash
bash scripts/run_etl.sh
```

## Project Structure

```
ecommerce-customer-insights/
├── README.md                      # Project documentation
├── requirements.txt               # Python dependencies
├── config/
│   └── config.yaml               # Application configuration
├── data/
│   └── exports/                  # Computed metrics exports
├── db/
│   ├── mysql/
│   │   ├── setup_mysql.sql       # MySQL schema creation
│   │   └── seed_sample_data.sql  # Sample data for testing
│   └── neo4j/
│       ├── notes.md              # Neo4j implementation notes
│       └── cypher/
│           ├── constraints.cypher    # Graph constraints
│           └── recommendations.cypher # Recommendation queries
├── scripts/
│   ├── run_etl.sh                # Execute full pipeline
│   └── run_local_checks.sh       # Validation checks
├── src/
│   ├── main.py                   # Pipeline orchestration (legacy)
│   ├── cli.py                    # CLI interface with subcommands
│   ├── config.py                 # Configuration loading
│   ├── mysql_ingest.py           # MySQL data extraction
│   ├── analytics.py              # Metric computations
│   ├── recommendations.py        # Co-purchase logic
│   ├── neo4j_graph.py            # Graph database operations
│   ├── export_powerbi.py         # Export functionality
│   ├── graph_queries.py          # Graph query utilities
│   ├── validation.py             # Data validation functions
│   └── pipeline/                 # Modular pipeline components
│       ├── __init__.py
│       ├── ingest.py             # Data ingestion module
│       ├── analyze.py            # Analytics computation module
│       ├── graph.py              # Graph operations module
│       └── export.py             # Export module
└── tests/                        # Test suite
    ├── test_cli.py               # CLI tests
    ├── test_graph_queries.py     # Graph query tests
    └── test_validation.py        # Validation tests
```

## Core Modules

### `cli.py`
Command-line interface for modular pipeline execution:
- `run_ingest` - Execute data ingestion from MySQL
- `run_graph` - Load data into Neo4j graph database
- `run_analyze` - Compute analytics metrics
- `run_export` - Export results to CSV files
- Supports subcommands: `ingest`, `graph`, `analyze`, `export`, `run_all`

### Pipeline Modules

#### `pipeline/ingest.py`
Data ingestion from MySQL:
- `run_ingest()` - Main ingestion orchestrator returning (users_df, products_df, orders_df)
- Wraps functions from `mysql_ingest.py`

#### `pipeline/analyze.py`
Analytics computation:
- `run_analyze()` - Computes all metrics returning (category_df, clv_df, affinity_df)
- Calls analytics and recommendation functions

#### `pipeline/graph.py`
Graph database operations:
- `run_graph()` - Upsert data to Neo4j graph
- Wraps Neo4j connection and graph operations

#### `pipeline/export.py`
Data export functionality:
- `run_export()` - Export all computed metrics to CSV files
- Wraps export_powerbi functions

### Core Library Modules

### `mysql_ingest.py`
Handles MySQL connectivity and data extraction:
- `connect_mysql()` - Establish database connection
- `fetch_users_df()` - Extract user records
- `fetch_products_df()` - Extract product catalog
- `fetch_orders_df()` - Extract order and order item details

### `analytics.py`
Computes business metrics:
- `compute_category_revenue()` - Revenue breakdown by product category
- `compute_clv_by_user()` - Customer lifetime value per user
- `compute_product_affinity_score()` - Normalized affinity scores for product pairs

### `recommendations.py`
Generates product recommendations:
- `build_copurchase_pairs()` - Identify products frequently bought together
- `top_recommendations_for_product()` - Retrieve top N recommendations for a product

### `neo4j_graph.py`
Graph database operations:
- `connect_neo4j()` - Establish Neo4j connection
- `upsert_graph()` - Create/update graph relationships for users, products, and orders

### `export_powerbi.py`
Export analytics results:
- `export_all()` - Export all computed metrics to CSV files for Power BI

### `graph_queries.py`
Graph query utilities:
- Functions for querying relationship data from Neo4j

### `validation.py`
Data validation functions:
- Quality checks and data integrity validation

## Database Schema

### MySQL Tables

**users**
- `user_id` (INT, Primary Key)
- `email` (VARCHAR, Unique)
- `full_name` (VARCHAR)
- `created_at` (TIMESTAMP)

**products**
- `product_id` (INT, Primary Key)
- `sku` (VARCHAR, Unique)
- `name` (VARCHAR)
- `category` (VARCHAR)
- `price` (DECIMAL)
- `created_at` (TIMESTAMP)

**orders**
- `order_id` (INT, Primary Key)
- `user_id` (INT, Foreign Key)
- `order_date` (TIMESTAMP)
- `status` (VARCHAR)

**order_items**
- `order_item_id` (INT, Primary Key)
- `order_id` (INT, Foreign Key)
- `product_id` (INT, Foreign Key)
- `quantity` (INT)
- `unit_price` (DECIMAL)

## Data Flow

```
MySQL (Raw Data)
    ↓
Data Extraction (mysql_ingest.py)
    ↓
Analytics Computations (analytics.py)
    ├→ Category Revenue
    ├→ Customer Lifetime Value
    └→ Product Affinity Scores
    ↓
Recommendations Engine (recommendations.py)
    ↓
Export & Graph Storage
    ├→ Power BI Export (export_powerbi.py)
    └→ Neo4j Graph (neo4j_graph.py)
```

## Configuration Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `mysql.host` | MySQL server hostname | localhost |
| `mysql.port` | MySQL server port | 3306 |
| `neo4j.uri` | Neo4j connection URI | bolt://localhost:7687 |
| `pipeline.export_dir` | Output directory for exports | data/exports |
| `pipeline.min_copurchase_count` | Minimum co-purchases for recommendations | 2 |
| `pipeline.recommendation_limit` | Maximum recommendations per product | 10 |

## Testing

Run the test suite:

```bash
pytest tests/
```

For specific test files:

```bash
pytest tests/test_analytics.py
pytest tests/test_recommendations.py
pytest tests/test_export.py
```

## Troubleshooting

### MySQL Connection Failed
- Verify MySQL server is running: `mysql -u root -p`
- Check credentials in `config/config.yaml`
- Ensure database `ecommerce_db` exists

### Neo4j Connection Failed
- Verify Neo4j service is running
- Check connection URI and credentials
- Ensure Neo4j is accessible on the configured port

### Missing Data
- Verify seed data was loaded: `mysql -u root -p ecommerce_db < db/mysql/seed_sample_data.sql`
- Check that MySQL tables are populated with records

## Performance Considerations

- **Large Datasets**: For datasets >100K orders, consider batch processing and indexing strategies
- **Recommendation Computation**: Co-purchase analysis is quadratic; optimize for large product catalogs
- **Graph Storage**: Consider partitioning Neo4j data for scalability
- **Export Size**: CSV exports may be large; implement incremental export strategies

## Environment Variables

Create a `.env` file for sensitive configuration (not tracked in version control):

```
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_HOST=localhost
NEO4J_USER=neo4j
NEO4J_PASSWORD=your_password
```

Load with `python-dotenv`:

```python
from dotenv import load_dotenv
load_dotenv()
```

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes with clear messages
4. Push to the branch and open a Pull Request

## Contact & Support

For questions or issues, please open an issue in the repository.

---

**Last Updated**: 2026-09-01
