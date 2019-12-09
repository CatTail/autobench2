import json
import shutil
import subprocess
import sys

import click


@click.command()
@click.argument('url')
# autobench2 command line options
@click.option('--verbose', is_flag=True, default=False, help='Print verbose messages')
@click.option('--warmup_duration', required=True, help='Duration of warm-up')
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
@click.option('--timeout', type=int, help='Record a timeout if a response is not received within this amount of time.')
@click.version_option()
def cli(url, verbose, warmup_duration, duration, low_rate, high_rate, rate_step, file, **args):
    if shutil.which('wrk') is None:
        sys.exit('wrk2 not installed')

    click.echo('sending warm-up traffic')
    execute_command(verbose, low_rate, warmup_duration, url, args)

    result = {}
    for rate in inclusive_range(low_rate, high_rate, rate_step):
        stdout = execute_command(verbose, rate, duration, url, args)
        result[rate] = stdout

    with open(file, 'w') as f:
        f.write(json.dumps(result))


def execute_command(verbose, rate, duration, url, args):
    command = get_command(rate, duration, url, args)

    if verbose:
        click.echo('executing command: {}'.format(' '.join(command)))

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    click.echo(stdout)
    click.secho(stderr.decode("utf-8"), fg='red', err=True)

    if process.returncode != 0:
        sys.exit(process.returncode)

    return stdout.decode("utf-8")


def get_command(rate, duration, url, args):
    cmd = ['wrk', '--rate', str(rate), '--duration', str(duration), '--latency']
    for key, value in args.items():
        if value is not None:
            # skip flag option value
            if type(value) is not bool:
                cmd.append('--{}'.format(key))
                cmd.append(str(value))
            elif value is True:
                cmd.append('--{}'.format(key))
    cmd.append(url)
    return cmd


def inclusive_range(start, stop, step):
    return list(range(start, stop, step)) + [stop]
