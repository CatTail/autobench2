import click


@click.command()
# autobench2 command line options
@click.option('--debug', is_flag=True, default=False, help='Enable debug logging')
@click.option('--warmup', required=True, help='Duration of warm-up')
@click.option('--low_rate', required=True, type=int, help='The initial rate')
@click.option('--high_rate', required=True, type=int, help='The final rate')
@click.option('--rate_step', required=True, type=int, help='The step to increase from low rate to high rate')
@click.option('--file', default='report.json', help='Report file location')
# wrk2 command line options
@click.option('-c', '--connections', required=True, type=int, help='Connections to keep open')
@click.option('-d', '--duration', required=True, help='Duration of test')
@click.option('-t', '--threads', required=True, type=int, help='Number of threads to use')
@click.option('-s', '--script', help='Load Lua script fil')
@click.option('-H', '--header', help='Add header to request')
@click.option('-L', '--latency', is_flag=True, default=False, help='Print latency statistics')
@click.option('-U', '--u_latency', is_flag=True, default=False, help='Print uncorrected latency statistics')
@click.option('--timeout', type=int, help='Record a timeout if a response is not received within this amount of time.')
@click.option('-B', '--batch_latency', is_flag=True, default=False,
              help='Measure latency of whole batches of pipelined ops (as opposed to each op)')
@click.version_option()
def cli(debug, **args):
    if debug:
        click.echo("get command line options {}".format(args))
    click.echo('Hello World!')
