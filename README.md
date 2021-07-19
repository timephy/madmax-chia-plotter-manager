# madmax-chia-plotter-manager
A plotting manager to fill all given drives with the madmax chia plotter.

## How to Use

### Clone repo

```bash
git clone https://github.com/timephy/madmax-chia-plotter-manager
cd madmax-chia-plotter-manager
```

### Install madmax plotter

https://github.com/madMAx43v3r/chia-plotter

Download the executable on Windows or build from source on macOS and Linux. See ["Install" section](https://github.com/madMAx43v3r/chia-plotter#Install) of the madmax `README.md`.

<!-- ### Install python3.9

Install python from the python website [download section](https://www.python.org/downloads).
On macOS you can also install python via [Homebrew](https://brew.sh).

Search the web for guidance if necessary. -->

### Edit `config.yaml`

```yaml
# Path to the plotter executable
# Windows: ../madMAx43v3r_chia-plotter_win_v<VERSION>/chia_plot.exe
# macOS: ../chia-plotter/build/chia_plot
# Linux: ../chia-plotter/build/chia_plot
plotter_path: ../madMAx43v3r_chia-plotter_win_v0.1.1/chia_plot.exe
madmax:
  # Temporary Drive
  # Windows: "A:\"
  # macOS: "/Volumes/A"
  # Linux: "/mnt/A"
  tmpdir: A:\
  # Temporary Drive 2 (ideally a ramdisk, as by madmax docs)
  # Windows: "R:\"
  # macOS: "/Volumes/R"
  # Linux: "/mnt/R"
  tmpdir2: R:\
  # Destination Directories (array), these will be filled with plots until their drive is full
  # Windows: [X:\, Y:\, Z:\]
  # macOS: [/Volumes/X, /Volumes/Y, /Volumes/Z]
  # Linux: [/mnt/X, /mnt/Y, /mnt/Z]
  finaldir: [X:\, Y:\, Z:\]
  # Thread Count
  threads: 14
  # Pool Key
  poolkey: <POOL>
  # Farmer Key
  farmerkey: <FARMER>
```

### Start script

```bash
python3.9 .
```