# Spanner dialect for SQLAlchemy

Spanner dialect for SQLAlchemy represents an interface API designed to make it possible to control Cloud Spanner databases with SQLAlchemy API. The dialect is built on top of [the Spanner DB API](https://github.com/googleapis/python-spanner/tree/master/google/cloud/spanner_dbapi), which is designed in accordance with [PEP-249](https://www.python.org/dev/peps/pep-0249/).

**NOTE: This project is still in DEVELOPMENT. It may make breaking changes without prior notice and should not yet be used for production purposes.**  

- [Cloud Spanner product documentation](https://cloud.google.com/spanner/docs)
- [SQLAlchemy product documentation](https://www.sqlalchemy.org/)

Quick Start
-----------

In order to use this package, you first need to go through the following steps:

1. [Select or create a Cloud Platform project.](https://console.cloud.google.com/project)
2. [Enable billing for your project.](https://cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project)
3. [Enable the Google Cloud Spanner API.](https://cloud.google.com/spanner)
4. [Setup Authentication.](https://googleapis.dev/python/google-api-core/latest/auth.html)

Installation
-----------

To install an in-development version of the package, clone its Git-repository:
```
git clone https://github.com/cloudspannerecosystem/python-spanner-sqlalchemy.git
```
Next install the package from the package `setup.py` file:
```
python setup.py install
```
During setup the dialect will be registered with entry points.

Example Usage
-----------
**Simple SELECT**
```python
from sqlalchemy import MetaData, Table, create_engine, select

engine = create_engine(
    "spanner:///projects/project-id/instances/instance-id/databases/database-id"
)

table = Table("table-id", MetaData(bind=engine), autoload=True)
for row in select(["*"], from_obj=table).execute().fetchall():
    print(row)
```

**Create a table**
```python
from sqlalchemy import (
    Column,
    Integer,
    MetaData,
    String,
    Table,
    create_engine,
)

engine = create_engine(
    "spanner:///projects/appdev-soda-spanner-staging/instances/sqlalchemy-dialect-test/databases/compliance-test"
)
metadata = MetaData()

user = Table(
    "users",
    metadata,
    Column("user_id", Integer, primary_key=True),
    Column("user_name", String(16), nullable=False),
)

metadata.create_all(engine)
```
Features and limitations
-----------
**Unique constraints**  
Cloud Spanner doesn't support direct UNIQUE constraints creation. In order to achieve column values uniqueness UNIQUE indexes should be used.

Instead of direct UNIQUE constraint creation:
```python
Table(
    'table',
    metadata,
    Column('col1', Integer),
    UniqueConstraint('col1', name='uix_1')
)
```
Create a UNIQUE index:
```python
Table(
    'table',
    metadata,
    Column('col1', Integer),
    Index("uix_1", "col1", unique=True),
)
```
**Autocommit mode**  
Spanner dialect supports both "autocommit" and "manual commit" modes. To set/change the current mode isolation levels can be used: `SERIALIZABLE` and `AUTOCOMMIT`.

**DDL and transactions**  
DDL statements are executed outside the regular transactions mechanism, which means DDL statements will not be rolled back on normal transaction rollback.

**Dropping a table**  
Cloud Spanner, by default, doesn't drop tables, which has secondary indexes and/or foreign key constraints. In Spanner dialect for SQLAlchemy, however, this restriction is omitted - if a table you are trying to delete has indexes/foreign keys, they will be dropped automatically right before dropping the table.

**Other limitations**  
- WITH RECURSIVE statement is not supported.
- Named schemas are not supported.
- Temporary tables are not supported, real tables are used instead.
- Numeric type dimensions (scale and precision) are constant. See the [docs](https://cloud.google.com/spanner/docs/data-types#numeric_types).
