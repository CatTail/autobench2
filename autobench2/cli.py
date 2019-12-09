import click
import shutil
import subprocess
import sys


@click.command()
@click.argument('url')
# autobench2 command line options
@click.option('--verbose', is_flag=True, default=False, help='Print verbose messages')
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
def cli(url, verbose, warmup, low_rate, high_rate, rate_step, file, **args):
    if verbose:
        click.echo('get command line options {}'.format(args))

    if shutil.which('wrk') is None:
        sys.exit('wrk2 not installed')

    cmd = ['wrk']
    for key, value in args.items():
        if value is not None:
            # skip flag option value
            if type(value) is not bool:
                cmd.append('--{}'.format(key))
                cmd.append(str(value))
            elif value is True:
                cmd.append('--{}'.format(key))

    for rate in inclusive_range(low_rate, high_rate, rate_step):
        command = cmd.copy()

        command.append('--rate')
        command.append(str(rate))

        command.append(url)

        if verbose:
            click.echo('executing command: {}'.format(' '.join(command)))

        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        click.echo(stdout)
        click.secho(stderr.decode("utf-8"), fg='red', err=True)


def inclusive_range(start, stop, step):
    return list(range(start, stop, step)) + [stop]
