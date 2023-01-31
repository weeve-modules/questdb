# QuestDB

|                |                                       |
| -------------- | ------------------------------------- |
| Name           | QuestDB                           |
| Version        | v1.0.0                                |
| DockerHub | [weevenetwork/questdb](https://hub.docker.com/r/weevenetwork/questdb) |
| Authors        | Jakub Grzelak                   |

- [QuestDB](#questdb)
  - [Description](#description)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Set by the weeve Agent on the edge-node](#set-by-the-weeve-agent-on-the-edge-node)
  - [Dependencies](#dependencies)
  - [Input](#input)
  - [Output](#output)

## Description

This module uses [REST API](https://questdb.io/docs/reference/api/rest/) to write data into your QuestDB table.

## Environment Variables

### Module Specific

The following module configurations can be provided in a data service designer section on weeve platform:

| Name                 | Environment Variables     | type     | Description                                              |
| -------------------- | ------------------------- | -------- | -------------------------------------------------------- |
| QuestDB URL    | QUEST_URL         | string   | URL to your QuestDB. It should be either host or if port is provided then host:port.            |
| Table Name    | TABLE_NAME         | string   | Table to write data to.            |
| Database Columns    | COLUMNS         | string   | List of comma (,) separated database columns headers to write to.           |
| Data Labels    | LABELS         | string   | List of comma (,) separated labels in passed data. Order of labels must match the order of provided corresponding columns.           |

### Set by the weeve Agent on the edge-node

Other features required for establishing the inter-container communication between modules in a data service are set by weeve agent.

| Environment Variables | type   | Description                                    |
| --------------------- | ------ | ---------------------------------------------- |
| MODULE_NAME           | string | Name of the module                             |
| MODULE_TYPE           | string | Type of the module (Input, Processing, Output)  |
| INGRESS_HOST          | string | Host to which data will be received            |
| INGRESS_PORT          | string | Port to which data will be received            |

## Dependencies

```txt
bottle
requests
```

## Input

Input to this module is:

* JSON body single object, example:

```json
{
    "label-1": 12,
    "label-2": "speed"
}
```

* array of JSON body objects, example:

```json
[
    {
        "label-1": 12,
        "label-2": "speed"
    },
    {
        "label-1": 15,
        "label-2": "volume"
    }
]
```

## Output

Output of this module is data inserted to the selected QuestDB table.
