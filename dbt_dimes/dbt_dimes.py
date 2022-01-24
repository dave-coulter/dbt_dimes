# -*- coding: utf-8 -*-
"""
Functions to assist creating dbt models
______________________________________________________________________________
"""
from pathlib import Path


def stg_model(table_name: str,
              table_cols: list,
              source: str,
              save_path: Path):
    '''
    Takes a source table name and columns and creates a basic staging model

    Parameters
    ----------
    table_name : str
        Name of the source table you want to stage
    table_cols : list
        List of the table's column names you want to include in the model
    source : str
        Name of the source system the table is from. Should match the source yml file in dbt
    export_path : Path
        Where you want the *.sql text file exported out to

    Returns
    -------
    None.

    Example:
        stg_model('rmrv_publication',
                  ['col_1', 'col_2', 'col_3'],
                  'researchmaster',
                  Path(r'C:/Users/e39298/RMIT University/dbt_models'))
    '''

    table_cols = [col.lower() for col in table_cols]
    fields = ',\n        '.join(table_cols)

    model = f'''with source as (

    select
        {fields}
    from {{{{ source('{source}', '{table_name}') }}}}

)

select * from source
'''

    with open(save_path / (f'stg_{source}__' + table_name + '.sql'), 'w') as file:
        file.write(model)


def create_src_yaml(source_name: str,
                    database: str,
                    schema: str,
                    table_list: list,
                    save_path: Path):
    '''
    Takes list of source tables and generates a yaml config file for them

    Parameters
    ----------
    source_name : str
        Name of data source. Used by dbt as reference.
    database : str
        Database where source tables are in data warehouse.
    schema : str
        Schema where source tables are in data warehouse.
    table_list : list
        List of tables to add to schema.
    export_path: Path
        Where do you want to yaml file to save to.


    Returns
    -------
    None.

    '''
    
    yaml = f'''version: 2

sources:
  - name: {source_name}
    database: {database}
    schema: {schema}
    tables:
      - name: ''' + '\n      - name: '.join(table_list)

    with open(save_path / (f'src_{source_name}' '.yml'), 'w') as file:
        file.write(yaml)
