import click

from .cloud.instances import Instances
from .kube import Nodes

API_URL = "https://api.revsys.com"


@click.group()
@click.pass_context
@click.option(
    "--api-url",
    default=API_URL,
    envvar="NODELS_API_URL",
    help="Base API URL for reporting",
)
def cli(ctx, api_url):
    """
    Gather information about Kubernetes Nodes and Cloud Provider Compute
    Instances.

    For tracking changes over time and helping to ensure no surprise
    infrastructure bills!
    """
    ctx.ensure_object(dict)
    ctx.obj["API_URL"] = api_url


@cli.command()
def nodes():
    """ Get information on Kubernetes nodes """
    click.echo("Get Nodes!")
    n = Nodes()
    n.gather()
    print(n.json(pretty=True))


@cli.command()
@click.option(
    "--region", default=None, envvar="NODELS_REGION", help="Limit to a single region"
)
def instances(region):
    """ Get all instances from Cloud account """
    click.echo("Get Instances!")
    i = Instances(region=region)
    i.gather()
    print(i.json(pretty=True))


@cli.command()
@click.pass_context
@click.option("-q / --quiet", is_flag=True)
def report_nodes(ctx, quiet):
    """ Gather and report on Kubernetes nodes """
    click.echo("Report Nodes!")
    n = Nodes()
    n.gather()
    result = n.report(url=ctx.obj["API_URL"])

    if not quiet:
        print(n.json(pretty=True))


@cli.command()
@click.pass_context
@click.option(
    "--region", default=None, envvar="NODELS_REGION", help="Limit to a single region"
)
@click.option("-q / --quiet", is_flag=True)
def report_instances(ctx, region, quiet):
    """ Gather and report on Cloud instances in account """
    click.echo("Report Instances!")
    i = Instances(region=region)
    i.gather()
    result = i.report(url=ctx.obj["API_URL"])

    if not quiet:
        print(i.json(pretty=True))


if __name__ == "__main__":
    cli(obj={})
