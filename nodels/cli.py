import click


@click.group()
def cli():
    """
    Gather information about Kubernetes Nodes and Cloud Provider Compute
    Instances.

    For tracking changes over time and helping to ensure no surprise
    infrastructure bills!
    """


@cli.command()
def nodes():
    """ Get information on Kubernetes nodes """
    click.echo("Get Nodes!")


@cli.command()
@click.option("--region", default=None, help="Limit to a single region")
def instances(region):
    """ Get all instances from Cloud account """
    click.echo("Get Instances!")
    click.echo(f"Region: {region}")


@cli.command()
def report_nodes():
    """ Gather and report on Kubernetes nodes """
    click.echo("Report Nodes!")


@cli.command()
def report_instances():
    """ Gather and report on Cloud instances in account """
    click.echo("Report Instances!")


if __name__ == "__main__":
    cli(auto_envvar_prefix="NODELS")
