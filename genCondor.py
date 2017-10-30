import os as os

l480 = ['akiyo_cif.y4m','bridge_far_cif.y4m','city_4cif.y4m','container_cif.y4m','flower_cif.y4m','grandma_qcif.y4m','husky_cif.y4m','news_cif.y4m','salesman_qcif.y4m','tennis_sif.y4m   ','bowing_cif.y4m','bus_cif.y4m','claire_qcif.y4m','crew_4cif.y4m','football_cif.y4m','harbour_4cif.y4m','ice_4cif.y4m','pamphlet_cif.y4m','sign_irene_cif.y4m','waterfall_cif.y4m','bridge_close_cif.y4m','carphone_qcif.y4m','coastguard_cif.y4m','deadline_cif.y4m','foreman_cif.y4m','highway_cif.y4m','mobile_cif.y4m','paris_cif.y4m','suzie_qcif.y4m'] 
l720 = ['720p50_mobcal_ter','720p50_parkrun_ter','720p50_shields_ter','720p5994_stockholm_ter','FourPeople_1280x720_60','Johnny_1280x720_60','KristenAndSara_1280x720_60','vidyo1_720p_60fps','vidyo3_720p_60fps','vidyo4_720p_6']
l1080 = ['blue_sky_1080p25','crowd_run_1080p50','dinner_1080p30','ducks_take_off_1080p50','factory_1080p30','in_to_tree_1080p50','life_1080p30','old_town_cross_1080p50','park_joy_1080p50','pedestrian_area_1080p25','rush_hour_1080p25','sintel_trailer_2k_1080p24','station2_1080p25','sunflower_1080p25','tractor_1080p25']

imgVp9 = "andresf01/vpx"
imgHm = "andresf01/hm-4891"
imgTg = "andresf01/tg"

# write files
# name : name of file
# content : list of line to write in file
def writeFile(name, content):
    try:
        with open (name, 'w') as f:
            for line in content:
                f.write(line + "\n")
            f.close()
        pass
    except:
        print ("Error writing files")

# cant : number of presets
# img : docker image to use
# scriptName : script name
# location : path to script name
# resolution : resolution to work (480p, 720p, 1080p)
# fileName : file name defined
def condorFile(cant, img, scriptName, location, resolution, fileName):
    string = []
    transfer_core = "transfer_input_files = {}{}$(Process).sh,/cluster/andresf01/sourceVideos/".format(location,scriptName)
    
    string.append("universe = docker")
    string.append("docker_image = {}".format(img))
    string.append("executable = /bin/bash")
    string.append("arguments = {}$(Process).sh".format(scriptName))
    string.append("should_transfer_files = YES")
    string.append("")
    string.append("when_to_transfer_output = ON_EXIT")
    string.append("output = out.$(Process)")
    string.append("error = err.$(Process)")
    string.append("log = log.$(Process)")
    string.append("queue {}".format(cant))
    
    files = addVideos(transfer_core, resolution)
    
    if len(files) > 0:
        for key, value in enumerate(files):
            string[5] = value
            writeFile("{}{}.condor".format(fileName, key), string)
            pass
        pass
    
# add every video path of videos
# transfer_core : common path for every video
# resolution : resolution needed for put specific videos
# return => list of specific line per video
def addVideos(transfer_core, resolution):
    tmpList = []
    results = []
    if resolution == '480':
        tmpList = l480
    elif resolution == '720':
        tmpList = l720
    elif resolution == '1080':
        tmpList = l1080
    else:
        tmpList = None
        
    if tmpList != None:
        for item in tmpList:
            results.append(transfer_core + "{}p/{}.y4m".format(resolution,item))
        pass
    else:
        print ("Resolution is not supported")
        exit()
    
    return results

def loadImg(imgName):
    if (imgName == "hm"):
        return imgHm
    elif (imgName == "vp9"):
        return imgVp9
    elif (imgName == "turing"):
        return imgTg
    else:
        print ("Docker image is not available")
        exit()

def showHelp():
    instruct = ("genCondor: Script to generate condor files \n"
    "====================================================== \n"
    "python3 genCondor.py : shows this help \n"
    "python3 cantity image script-name location resolution file-name \n"
    "*cantity : amount of queues to run (presets) \n"
    "*image : docker image to use \n"
    "*script-name : base name of the script \n"
    "*location : path to the script \n"
    "*resolution : videos resolution [480,720,1080] \n"
    "*file-name : name of condor files to generate")
    print (instruct)

if __name__ == "__main__":
    import sys
    args = sys.argv
    if (len(args) == 7):
        img = loadImg(args[2])
        condorFile(args[1], img, args[3], args[4], args[5], args[6])
    elif (len(args) == 1):
        showHelp()
    else:
        print ("Please check your parameters")
        showHelp()
    