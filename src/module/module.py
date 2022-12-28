"""
This file implements module's main logic.
Data outputting should happen here.

Edit this file to implement your module.
"""

import requests
from logging import getLogger
from .params import PARAMS

log = getLogger("module")

def module_main(received_data: any) -> str:
    """
    Send received data to the next module by implementing module's main logic.
    Function description should not be modified.

    Args:
        received_data (any): Data received by module and validated.

    Returns:
        str: Error message if error occurred, otherwise None.

    """

    log.debug("Outputting ...")

    try:
        if type(received_data) == dict:
            return insert_data(received_data)
        else:
            for data in received_data:
                resp_error = insert_data(data)
                if resp_error:
                    return resp_error
            return None

    except Exception as e:
        return f"Exception in the module business logic: {e}"

def insert_data(data):
    # build columns artefact
    columns = ""
    for c in PARAMS['COLUMNS']:
        columns += f"{c},"
    columns = "(" + columns[:-1] + ")"

    # build values
    values = ""
    for label in PARAMS['LABELS']:
        if type(data[label]) == str:
            values += f"\'{data[label]}\',"
        else:
            values += f"{data[label]},"
    values = "(" + values[:-1] + ")"

    # build SQL Query
    SQL = f"INSERT INTO {PARAMS['TABLE_NAME']} {columns} VALUES {values}"
    log.debug(f'SQL: {SQL}')
    query_params = {'query': SQL}

    try:
        log.debug("Writing data...")
        requests.get(PARAMS['QUEST_URL'] + '/exec', params=query_params)

        return None

    except requests.exceptions.RequestException as e:
        return f'Error when inserting to QuestDB: {e}'
