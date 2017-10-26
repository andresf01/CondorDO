# CondorDO

This script generate automatically a set of condor files to code a list of videos grouped by resolution. 

## Requirements

 - Python3+

## Run

For running this script is necessary have next information

 - Number of presets
 - Docker image name
 - Script name
 - Path to script
 - Videos resolution
 - Name of condor files

### Docker images availables

 - `hm` for use andresf01/hm-4891 image
 - `turing` for use andresf01/tg image
 - `vp9` for use andresf01/vpx image

To change images please refer to `loadImg` function.

### Script name

If you have a set of three scripts as `hmbwl0.sh`,`hmbwl1.sh` and `hmbwl2.sh` the script name is `hmbwl`. So the **number of presets** is **three**. All scripts must finish in `.sh`

### Path to script

If scritp is located in `/home/andresf01/script.sh` then path must be `/home/andresf01/`

### Videos resolution

Pick a resolution to access all videos of that set. Check video list in `VIDEOS.MD`

 - `480` 
 - `720`
 - `1080`

This only apply to Universidad del Valle's cluster, if you need set new paths check lists `l480`, `l720` and `l1080`.

### Name of condor files

This set `name`in the list of generated files like `name1.condor`, `name2.condor`, ..., `nameN.condor`

## Example

`python3 genCondor.py 3 hm hmrt /home/andres/scripts/ 1080 hm1080rt`