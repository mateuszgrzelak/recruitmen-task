import click


@click.command()
@click.option('--load-to-db', '-ltdb', 'ltdb', is_flag=True)
@click.option('--percentage', '-p', 'p', type=click.Choice(['male', 'female'], case_sensitive=False))
@click.option('--average-age', '-aa', 'aa', type=click.Choice(['male', 'female', 'generally'], case_sensitive=False))
@click.option('--most-common-cities', '-mcc', 'mcc')
@click.option('--most-common-pass', '-mcp', 'mcp')
@click.option('--users-born-between-dates', '-ubbd', 'ubbd', nargs=2)
@click.option('--most-secure-pass', '-msp', 'msp', is_flag=True)
def hello(ltdb, p, aa, mcc, mcp, ubbd, msp):
    if ltdb:
        print("load to database")
    if p is not None:
        print("percentage")
    if aa is not None:
        print("average age")
    if mcc is not None:
        print("most common cities")
    if mcp is not None:
        print("most common pass")
    if len(ubbd) == 2:
        print("users born between dates")
    if msp:
        print("most secure pass")


if __name__ == '__main__':
    hello()