import click


@click.command()
@click.argument('number', type=int, nargs=1)
def main(number):
	binary_str = "{0:b}".format(number)
	binary_str = binary_str[::-1]
	for i, c in enumerate(binary_str):
		print '{:02d}: {:s}'.format(i, c)


if __name__ == '__main__':
	main()
