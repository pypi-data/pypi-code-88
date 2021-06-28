import json
from pathlib import Path
from typing import Dict, List

import typer
from alteia.core.errors import ResponseError
from tabulate import tabulate

from alteia_cli import utils
from alteia_cli.sdk import alteia_sdk

app = typer.Typer()


@app.command(name='create')
def create(
        filepath: Path = typer.Option(
        ...,   # '...' in typer.Option() makes the option required
        exists=True,
        readable=True,
        help='Path of the Credential JSON file'),
        company: str = typer.Option(default=None, help='Company identifier')):
    """ Create a new credential entry """

    sdk = alteia_sdk()
    credentials_list = json.load(open(filepath))
    if not isinstance(credentials_list, list):
        credentials_list = [credentials_list]
    for cred in credentials_list:
        if not company and not cred.get('company', None):
            typer.secho(
                '✖ Cannot create a credential entry with the name {!r}. '
                'You have to define a company'.format(
                    cred.get('name')),
                fg=typer.colors.RED
            )
            raise typer.Exit(2)
        elif company and not cred.get('company', None):
            cred['company'] = company

        found_cred = sdk.credentials.search(
            filter={
                'name': {'$eq': cred.get('name')},
                'company': {'$eq': cred.get('company')},
            },
            return_total=True
        )
        if found_cred.total >= 1:
            typer.secho(
                '✖ Cannot create a credential entry with the name {!r}. '
                'One already exists on {}'.format(
                    cred.get('name'), sdk._connection._base_url
                ),
                fg=typer.colors.RED
            )
            raise typer.Exit(2)

        try:
            created_cred = sdk.credentials.create(
                name=cred['name'],
                credentials=cred['credentials'],
                company=cred['company']
            )
            typer.secho('✓ Credentials created successfully', fg=typer.colors.GREEN)
            return created_cred
        except Exception as ex:
            print('Impossible to save {} with error {}'.format(cred['name'], ex))
            raise typer.Exit(code=1)


@app.command(name='list')
def list_credentials(
        company: str = typer.Option(default=None, help='Company identifier'),
):
    """ List the existing credentials """
    sdk = alteia_sdk()
    list_filter = {}
    if company:
        list_filter = {"company": {"$eq": company}}
    with utils.spinner():
        credentials = sdk.credentials.search(filter=list_filter)
    if len(credentials) > 0:
        table: Dict[str, List[str]] = {
            'Credentials name': [],
            'Company': [],
            'Company shortname': [],
            'Registry': [],
        }
        for credential in credentials:
            table['Credentials name'].append(utils.green_bold(credential.name))
            table['Registry'].append(
                utils.green_bold(credential.credentials['registry'])
            )

            company_desc = utils.describe_company(sdk, credential.company)
            if company_desc:
                company_name = company_desc.name
                short_name = getattr(company_desc, 'short_name', '')
            else:
                company_name = credential.company
                short_name = ''

            table['Company'].append(utils.green_bold(company_name))
            table['Company shortname'].append(utils.green_bold(short_name))

        print(tabulate(
            table,
            headers='keys',
            tablefmt='pretty',
            colalign=['left'])
        )
    else:
        typer.secho(
            'No credentials founds', fg=typer.colors.YELLOW)
    print()


@app.command(name='delete')
def delete_credentials(
        name: str = typer.Argument(...)):
    """ Delete a credential entry by its name"""
    sdk = alteia_sdk()
    found_cred = sdk.credentials.search(
        filter={
            'name': {'$eq': name},
        },
        return_total=True
    )
    if found_cred.total < 1:
        typer.secho(
            '✖ Credential {!r} not found on {!r}'.format(
                name, sdk._connection._base_url
            ),
            fg=typer.colors.RED
        )
        raise typer.Exit(2)

    try:
        sdk.credentials.delete(
            found_cred.results[0].id,
            company=found_cred.results[0].company
        )
    except ResponseError as e:
        typer.secho(
            '✖ Cannot delete the credentials {!r}'.format(name),
            fg=typer.colors.RED
        )
        typer.secho('details: {}'.format(str(e)), fg=typer.colors.RED)
        raise typer.Exit(2)

    typer.secho(
        '✓ Credentials {!r} deleted successfully'.format(name),
        fg=typer.colors.GREEN
    )


if __name__ == "__main__":
    app()
