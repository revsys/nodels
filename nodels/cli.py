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
@click.option(
    "--api-token", default=None, envvar="NODELS_API_TOKEN", help="Auth token for API"
)
def cli(ctx, api_url, api_token):
    """
    Gather information about Kubernetes Nodes and Cloud Provider Compute
    Instances.

    For tracking changes over time and helping to ensure no surprise
    infrastructure bills!
    """
    ctx.ensure_object(dict)
    ctx.obj["API_URL"] = api_url
    ctx.obj["API_TOKEN"] = api_token


@cli.command()
def nodes(name, id):
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
@click.option("--name", default=None, envvar="NODELS_CLUSTER_NAME", help="Cluster name")
@click.option("--id", default=None, envvar="NODELS_CLUSTER_ID", help="Cluster API ID")
def report_nodes(ctx, q, name, id):
    """ Gather and report on Kubernetes nodes """
    click.echo("Report Nodes!")
    n = Nodes()
    n.gather()
    report = n.report(
        url=ctx.obj["API_URL"], token=ctx.obj["API_TOKEN"], name=name, id=id
    )

    if not q:
        print(report.to_json())


@cli.command()
@click.pass_context
@click.option(
    "--region", default=None, envvar="NODELS_REGION", help="Limit to a single region"
)
@click.option("-q / --quiet", is_flag=True)
@click.option("--name", default=None, envvar="NODELS_ACCOUNT_NAME", help="Cluster name")
@click.option("--id", default=None, envvar="NODELS_ACCOUNT_ID", help="Cluster API ID")
def report_instances(ctx, region, q, name, id):
    """ Gather and report on Cloud instances in account """
    click.echo("Report Instances!")
    i = Instances(region=region)
    i.gather()
    report = i.report(
        url=ctx.obj["API_URL"], token=ctx.obj["API_TOKEN"], name=name, id=id
    )

    if not q:
        print(report.to_json())


if __name__ == "__main__":
    cli(obj={})
