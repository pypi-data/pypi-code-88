import argparse

from bigquery_validator import BigQueryValidator

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--function', type=str, help='Function to be called', required=True)
    parser.add_argument('-p', '--param', type=str, help='Parameter for function', required=True)
    args = parser.parse_args()
    function = args.function
    param = args.param

    bigquery_validator = BigQueryValidator()
    if function == 'render_templated_query':
        bigquery_validator.render_templated_query('select date("{{ params.date }}") as date')
    elif function == 'dry_run_query':
        bigquery_validator.dry_run_query('select true')
    elif function == 'validate_query':
        print('vw')
        bigquery_validator.validate_query('select true')
    elif function == 'validate_query_from_file':
        bigquery_validator.validate_query('./valid_query.sql')
    else:
        raise ValueError('Invalid argument passed for function')
