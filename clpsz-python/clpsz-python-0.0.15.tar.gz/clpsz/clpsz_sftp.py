import pysftp
import click


@click.command()
@click.option('-h', '--host', 'host', help='sftp server address, domain or ip')
@click.option('-P', '--port', 'port', type=int, default=22, help='sftp server port')
@click.option('-u', '--user', 'user', help='sftp server login user')
@click.option('-p', '--password', 'password', help='sftp server login password')
@click.argument('src', nargs=1)
@click.argument('dst', nargs=1)
def main(host, port, user, password, src, dst):
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    with pysftp.Connection(host=host, port=port, username=user, password=password, cnopts=cnopts) as sftp:
        sftp.put(src, dst)


if __name__ == '__main__':
    main()
