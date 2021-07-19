import yaml
import pathlib
import sys
import logging
from shutil import disk_usage

from format import format, fg, style

PLOT_MAX_SIZE = 109000000000

config_text = pathlib.Path('config.yaml').read_text()
config = yaml.load(config_text, Loader=yaml.FullLoader)
logging.basicConfig(filename='debug.log', encoding='utf-8', level=logging.INFO)
dry = '--dry' in sys.argv

print('madmax-chia-plotter-manager')
print(f'{config=}')
print(f'{dry=}')
print()


def plot(madmax_kwargs, *, dry):
    args = (x for key, value in madmax_kwargs.items()
            for x in (f'--{key}', str(value)))
    command = f'$ ./chia_plot.exe {" ".join(args)}'
    print(format(command, fg=fg.black))
    if not dry:
        pass


for dir in config['madmax']['finaldir']:
    # print(f'Trying to plot to {dir}')
    plot_num_approx = disk_usage(dir).free // PLOT_MAX_SIZE
    plot_num_curr = 1
    print(format(
        f'Approximately enough space for {plot_num_approx} plots in {dir}.', fg=fg.green))
    while True:
        if disk_usage(dir).free < PLOT_MAX_SIZE or (dry and plot_num_curr > plot_num_approx):
            print(
                format(f'Not enough space left in {dir} for more plots.', fg=fg.yellow))
            break
        print(f'Plotting {plot_num_curr} of {plot_num_approx} in {dir}.')
        plot(dict(config['madmax'], finaldir=dir), dry=dry)
        plot_num_curr += 1

print()
print('Done with all directories.')
print('Quitting.')
