# dbt_dimes

Assists building staging models and config yaml.

```python
import dbt_dimes

stg_model('my_table', 
         ['col_1', 'col_2', 'col_3'],
          'datasource',
          'C:/Users/me/models')

create_src_yaml('datasource', 
                'database', 
                'schema',
                [table_1, table_2],
                'C:/Users/Me/models')
```

Suggested usage is to create a dictionary of table names and columns as keys and values, then use functions to create staged tables in a for loop. Staged models will be output with standard dbt naming convention, i.e. **stg__datasource_tablename.sql**.