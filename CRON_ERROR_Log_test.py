# Imagine one of your colleagues is struggling with a program that keeps throwing an error. Unfortunately, 
# the program's source code is too complicated to easily find the error there. The good news is that the program outputs
# a log file you can read! Let's write a script to search the log file for the exact error, then output that error into a 
# separate file so you can work out what's wrong.


#!/usr/bin/env python3
import sys
import os
import re


def error_search(log_file):
  error = input("What is the error? ")
  returned_errors = []
  with open(log_file, mode='r',encoding='UTF-8') as file:
    for log in  file.readlines():
      error_patterns = ["error"]
      for i in range(len(error.split(' '))):
        error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
      if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
        returned_errors.append(log)
    file.close()
  return returned_errors

  
def file_output(returned_errors):
  with open(os.path.expanduser('~') + '/data/errors_found.log', 'w') as file: # os.path.expanduser('~') vai retornar o homepath
    for error in returned_errors:
      file.write(error)
    file.close()
if __name__ == "__main__":
  log_file = sys.argv[1]
  returned_errors = error_search(log_file)
  file_output(returned_errors)
  sys.exit(0) # Vai sair do python e o argumento opcional passado determina o estado de terminio ,0 é considerado 
              # "sucessful termination" e qualquer valor diferente é "abnormal termination" pelas shells

# Conteudo do arquivo de log passados no qwikilabs

# July 31 00:06:21 mycomputername kernel[96041]: WARN Failed to start network connection
# July 31 00:09:53 mycomputername updater[46711]: WARN Computer needs to be turned off and on again
# July 31 00:12:36 mycomputername kernel[48462]: INFO Successfully connected
# July 31 00:13:52 mycomputername updater[43530]: ERROR Error running Python2.exe: Segmentation Fault (core dumped)
# July 31 00:16:13 mycomputername NetworkManager[63902]: WARN Failed to start application install
# July 31 00:26:45 mycomputername CRON[83063]: INFO I'm sorry Dave. I'm afraid I can't do that
# July 31 00:27:56 mycomputername cacheclient[75746]: WARN PC Load Letter
# July 31 00:33:31 mycomputername system[25588]: ERROR Out of yellow ink, specifically, even though you want grayscale
# July 31 00:36:55 mycomputername updater[73786]: WARN Packet loss
# July 31 00:37:38 mycomputername dhcpclient[87602]: INFO Googling the answer
# July 31 00:37:48 mycomputername utility[21449]: ERROR The cake is a lie!
# July 31 00:44:50 mycomputername kernel[63793]: ERROR Failed process [13966]
# July 31 00:45:23 mycomputername cacheclient[55644]: ERROR Unable to download more RAM
# July 31 00:51:23 mycomputername cacheclient[85917]: ERROR Failed process [13966]
# July 31 01:06:51 mycomputername cacheclient[47853]: WARN Computer needs to be turned off and on again
# July 31 01:07:17 mycomputername system[78132]: INFO Packets sent successfully
# July 31 01:19:34 mycomputername CRON[94028]: WARN Failed to start network connection
# July 31 01:24:05 mycomputername utility[14905]: INFO Healthy resource usage
# July 31 01:29:04 mycomputername kernel[57436]: INFO Generating Logs
# July 31 01:36:27 mycomputername process[81163]: ERROR Unable to download more RAM
# July 31 01:40:38 mycomputername kernel[35287]: ERROR ID: 10t
# July 31 01:42:02 mycomputername jam_tag=psim[27947]: INFO I'm sorry Dave. I'm afraid I can't do that
# July 31 01:42:28 mycomputername kernel[16004]: WARN Computer needs to be turned off and on again
# July 31 01:45:14 mycomputername cacheclient[28721]: INFO Googling the answer
# July 31 02:01:20 mycomputername NetworkManager[55118]: ERROR Unable to perform package upgrade
# July 31 02:12:54 mycomputername kernel[30641]: WARN Low on memory
# July 31 02:23:37 mycomputername utility[37367]: INFO Starting sync
# July 31 02:25:52 mycomputername system[41921]: WARN Failed to start CPU thread[39016]
# July 31 02:34:37 mycomputername kernel[32280]: INFO Loading...
# July 31 02:36:44 mycomputername NetworkManager[90289]: WARN Failed to start CPU thread[39016]
# July 31 02:39:01 mycomputername CRON[89330]: ERROR Unable to perform package upgrade
# July 31 02:45:39 mycomputername utility[57387]: INFO Access permitted
# July 31 02:58:44 mycomputername process[44707]: WARN Computer needs to be turned off and on again
# July 31 02:59:35 mycomputername system[55024]: WARN Packet loss
# July 31 03:09:30 mycomputername kernel[40705]: ERROR The cake is a lie!
# July 31 03:23:16 mycomputername cacheclient[57185]: INFO Checking process [16121]
# July 31 03:26:56 mycomputername cacheclient[90154]: INFO Healthy resource usage
# July 31 03:28:52 mycomputername CRON[55441]: INFO Loading...
# July 31 03:29:34 mycomputername dhcpclient[69232]: ERROR Unable to download more RAM
# July 31 03:34:41 mycomputername NetworkManager[14120]: ERROR 404 error not found
# July 31 03:36:26 mycomputername dhcpclient[79731]: ERROR The cake is a lie!
# July 31 03:38:24 mycomputername CRON[92141]: INFO Access permitted
# July 31 03:40:00 mycomputername dhcpclient[40114]: INFO Starting sync
# July 31 03:42:45 mycomputername utility[53726]: INFO I'm sorry Dave. I'm afraid I can't do that
# July 31 03:47:07 mycomputername NetworkManager[63805]: WARN Please reboot user
# July 31 04:09:16 mycomputername CRON[52593]: WARN PC Load Letter
# July 31 04:11:32 mycomputername CRON[51253]: ERROR: Failed to start CRON job due to script syntax error. Inform the CRON job owner!
# July 31 04:11:32 mycomputername jam_tag=psim[84082]: ERROR ID: 10t
# July 31 04:12:05 mycomputername utility[63418]: INFO Successfully connected
# July 31 04:14:22 mycomputername utility[53225]: ERROR I am error
# July 31 04:31:00 mycomputername NetworkManager[23060]: ERROR Out of yellow ink, specifically, even though you want grayscale
# July 31 04:36:49 mycomputername dhcpclient[89091]: ERROR Failed process [13966]
# July 31 04:37:34 mycomputername cacheclient[63496]: ERROR Sorting a list
# July 31 04:45:37 mycomputername CRON[78322]: INFO Checking process [16121]
# July 31 04:51:20 mycomputername kernel[66473]: WARN System overheating
# July 31 05:00:28 mycomputername NetworkManager[76363]: ERROR The cake is a lie!
# July 31 05:10:52 mycomputername jam_tag=psim[26712]: ERROR Process failed
# July 31 05:14:16 mycomputername utility[91499]: ERROR Sorting a list
# July 31 05:15:02 mycomputername system[76042]: WARN System overheating
# July 31 05:18:19 mycomputername kernel[59870]: INFO Starting sync
# July 31 05:27:34 mycomputername NetworkManager[67593]: INFO Writing Logs
# July 31 05:32:16 mycomputername process[21939]: ERROR Failed process [13966]
# July 31 05:34:23 mycomputername NetworkManager[96505]: INFO Plenty of disk space left
# July 31 05:36:31 mycomputername utility[15156]: INFO Packets sent successfully
# July 31 05:43:29 mycomputername dhcpclient[35484]: ERROR Encapsulating packets
# July 31 05:44:07 mycomputername cacheclient[97637]: ERROR Operation completed successfully
# July 31 05:58:25 mycomputername process[99181]: ERROR Process failed
# July 31 05:59:27 mycomputername utility[74219]: WARN Failed to start CPU thread[39016]
# July 31 06:20:09 mycomputername jam_tag=psim[34744]: INFO Loading...
# July 31 06:31:02 mycomputername jam_tag=psim[40033]: ERROR Syntax issue
# July 31 06:38:58 mycomputername CRON[31832]: INFO Memory allocated
# July 31 06:38:58 mycomputername updater[10115]: ERROR Unable to perform package upgrade
# July 31 06:43:49 mycomputername jam_tag=psim[59857]: INFO Successfully connected
# July 31 06:46:06 mycomputername CRON[12372]: ERROR Unable to perform package upgrade
# July 31 06:48:38 mycomputername NetworkManager[95699]: WARN Failed to start network connection
# July 31 07:01:16 mycomputername system[39619]: INFO Plenty of disk space left
# July 31 07:08:07 mycomputername jam_tag=psim[39984]: INFO Memory allocated
# July 31 07:08:10 mycomputername cacheclient[17912]: INFO Generating Logs
# July 31 07:10:12 mycomputername process[60665]: INFO Failed to start process[85253]
# July 31 07:11:12 mycomputername dhcpclient[98633]: WARN System overheating
# July 31 07:24:38 mycomputername jam_tag=psim[83107]: ERROR ID: 10t
# July 31 07:34:37 mycomputername process[22428]: INFO Failed to start process[85253]
# July 31 07:34:52 mycomputername updater[42267]: ERROR I am error
# July 31 07:35:27 mycomputername jam_tag=psim[96969]: INFO Loading...
# July 31 07:37:13 mycomputername updater[11461]: ERROR Unable to perform package upgrade
# July 31 07:46:27 mycomputername jam_tag=psim[21363]: INFO Packets sent successfully
# July 31 07:50:05 mycomputername system[68973]: INFO Compiling code
# July 31 08:02:17 mycomputername kernel[84055]: INFO Checking process [16121]
# July 31 08:14:45 mycomputername process[84233]: ERROR Out of ink
# July 31 08:21:11 mycomputername system[78476]: ERROR Error running Python2.exe: Segmentation Fault (core dumped)
# July 31 08:29:59 mycomputername utility[73121]: ERROR I am error
# July 31 08:33:24 mycomputername system[55880]: INFO Defragmenting hard drive
# July 31 08:39:13 mycomputername utility[78233]: ERROR The cake is a lie!
# July 31 08:49:55 mycomputername kernel[88866]: INFO Starting sync
# July 31 08:55:07 mycomputername system[24562]: ERROR Process failed
# July 31 08:56:17 mycomputername jam_tag=psim[67538]: WARN Packet loss
# July 31 09:01:06 mycomputername NetworkManager[89092]: INFO I'm sorry Dave. I'm afraid I can't do that
# July 31 09:26:46 mycomputername utility[53969]: WARN Low on memory
# July 31 09:29:37 mycomputername CRON[89099]: INFO Packets sent successfully
# July 31 09:37:31 mycomputername updater[46513]: ERROR Out of yellow ink, specifically, even though you want grayscale
# July 31 09:45:20 mycomputername utility[95200]: ERROR Out of yellow ink, specifically, even though you want grayscale
# July 31 09:47:30 mycomputername system[61238]: ERROR I am error
# July 31 09:51:01 mycomputername dhcpclient[83799]: WARN Packet loss
# July 31 09:54:04 mycomputername system[18585]: ERROR 404 error not found
# July 31 09:54:06 mycomputername updater[84188]: ERROR 404 error not found
# July 31 09:57:08 mycomputername dhcpclient[26102]: WARN Failed to start application install
# July 31 10:21:57 mycomputername NetworkManager[62856]: WARN Failed to start network connection
# July 31 10:25:03 mycomputername utility[89273]: ERROR lp0 on fire
# July 31 10:26:12 mycomputername utility[23086]: INFO Access permitted
# July 31 10:30:37 mycomputername system[48235]: WARN Please reboot user
# July 31 10:41:32 mycomputername NetworkManager[70251]: ERROR Sorting a list
# July 31 10:53:36 mycomputername system[78903]: ERROR Encapsulating packets
# July 31 10:56:12 mycomputername jam_tag=psim[97572]: WARN Failed to start network connection
# July 31 10:56:29 mycomputername updater[55938]: ERROR Unable to download more RAM
# July 31 10:58:29 mycomputername utility[78692]: INFO Writing Logs
# July 31 11:05:09 mycomputername cacheclient[34385]: WARN System overheating
# July 31 11:14:39 mycomputername process[22102]: WARN System overheating
# July 31 11:18:34 mycomputername process[32468]: ERROR 418: I'm a teapot
# July 31 11:19:56 mycomputername system[15816]: ERROR I am error
# July 31 11:20:11 mycomputername kernel[77339]: ERROR Out of ink
# July 31 11:25:08 mycomputername utility[65264]: INFO Checking process [16121]
# July 31 11:27:52 mycomputername CRON[65812]: ERROR ID: 10t
# July 31 11:43:32 mycomputername CRON[72993]: WARN Failed to start network connection
# July 31 11:50:34 mycomputername CRON[51748]: ERROR ID: 10t
# July 31 12:00:29 mycomputername NetworkManager[96959]: ERROR Operation completed successfully
# July 31 12:04:22 mycomputername updater[51112]: ERROR lp0 on fire
# July 31 12:07:01 mycomputername updater[47209]: ERROR 418: I'm a teapot
# July 31 12:15:19 mycomputername updater[76427]: WARN Low on memory
# July 31 12:21:53 mycomputername system[33216]: WARN PC Load Letter
# July 31 12:42:41 mycomputername system[38483]: ERROR AssertionError 'False' is not 'True'
# July 31 12:47:53 mycomputername dhcpclient[17238]: WARN PC Load Letter
# July 31 12:48:04 mycomputername system[68448]: ERROR lp0 on fire
# July 31 12:54:55 mycomputername updater[93309]: WARN Please send help I am stuck inside the internet
# July 31 13:00:34 mycomputername system[62593]: ERROR Out of yellow ink, specifically, even though you want grayscale
# July 31 13:04:58 mycomputername cacheclient[63249]: INFO Access permitted
# July 31 13:08:06 mycomputername cacheclient[32689]: INFO Loading...
# July 31 13:14:54 mycomputername system[84324]: ERROR 404 error not found
# July 31 13:23:12 mycomputername system[56046]: ERROR Unable to perform package upgrade
# July 31 13:36:17 mycomputername CRON[53567]: ERROR You seriously weren't expecting to find anything useful in here, were you?
# July 31 13:39:39 mycomputername process[94615]: ERROR AssertionError 'False' is not 'True'
# July 31 14:34:36 mycomputername dhcpclient[37575]: ERROR 404 error not found
# July 31 14:44:34 mycomputername kernel[34400]: INFO Successfully connected
# July 31 15:18:00 mycomputername process[56145]: WARN Please send help I am stuck inside the internet
# July 31 15:21:55 mycomputername CRON[38897]: INFO Failed to start process[85253]
# July 31 15:23:54 mycomputername utility[20760]: ERROR lp0 on fire
# July 31 15:45:53 mycomputername jam_tag=psim[18544]: INFO Hello world
# July 31 15:51:37 mycomputername kernel[79314]: WARN Failed to start CPU thread[39016]
# July 31 16:02:05 mycomputername cacheclient[80348]: INFO Starting sync
# July 31 16:07:01 mycomputername process[11843]: ERROR Process failed
# July 31 16:20:37 mycomputername dhcpclient[36371]: ERROR Unable to download more RAM
# July 31 16:24:34 mycomputername updater[83956]: INFO Access permitted
# July 31 16:30:59 mycomputername updater[61327]: INFO Starting sync
# July 31 16:36:57 mycomputername system[27219]: ERROR Process failed
# July 31 16:39:10 mycomputername jam_tag=psim[76787]: INFO Checking process [16121]
# July 31 16:43:19 mycomputername utility[31859]: ERROR Process failed
# July 31 16:45:49 mycomputername process[29993]: WARN Failed to start network connection
# July 31 17:13:27 mycomputername system[77845]: WARN Failed to start CPU thread[39016]
# July 31 17:25:11 mycomputername jam_tag=psim[70693]: ERROR Syntax issue
# July 31 17:55:16 mycomputername jam_tag=psim[58396]: ERROR 404 error not found
# July 31 17:55:32 mycomputername system[56762]: WARN Low on memory
# July 31 18:03:28 mycomputername process[79703]: ERROR lp0 on fire
# July 31 18:04:46 mycomputername updater[79077]: ERROR Operation completed successfully
# July 31 18:51:04 mycomputername cacheclient[83250]: ERROR Sorting a list
# July 31 18:51:46 mycomputername cacheclient[57597]: INFO Access permitted
# July 31 18:56:23 mycomputername kernel[87834]: WARN Failed to start network connection
# July 31 19:04:43 mycomputername kernel[36465]: WARN Packet loss
# July 31 19:24:44 mycomputername cacheclient[47526]: INFO Googling the answer
# July 31 19:44:47 mycomputername system[50340]: ERROR lp0 on fire
# July 31 19:48:46 mycomputername CRON[88206]: ERROR Failed process [13966]
# July 31 19:51:07 mycomputername NetworkManager[38455]: INFO Access permitted
# July 31 19:55:34 mycomputername jam_tag=psim[21289]: INFO Plenty of disk space left
# July 31 19:56:47 mycomputername CRON[61924]: ERROR Out of yellow ink, specifically, even though you want grayscale
# July 31 20:02:26 mycomputername cacheclient[50070]: ERROR Encapsulating packets
# July 31 20:05:36 mycomputername updater[23489]: INFO Healthy resource usage
# July 31 20:21:06 mycomputername utility[67718]: INFO Defragmenting hard drive
# July 31 20:38:05 mycomputername kernel[30846]: ERROR AssertionError 'False' is not 'True'
# July 31 20:42:44 mycomputername CRON[95019]: INFO Access permitted
# July 31 20:48:06 mycomputername kernel[51099]: WARN PC Load Letter
# July 31 20:57:02 mycomputername CRON[23996]: INFO Googling the answer
# July 31 21:05:47 mycomputername utility[67348]: ERROR The cake is a lie!
# July 31 21:06:46 mycomputername kernel[80105]: ERROR lp0 on fire
# July 31 21:26:11 mycomputername process[18312]: WARN Computer needs to be turned off and on again
# July 31 21:28:55 mycomputername jam_tag=psim[89637]: INFO Packets sent successfully
# July 31 21:48:30 mycomputername kernel[33330]: ERROR Syntax issue
# July 31 22:05:31 mycomputername process[37921]: ERROR Process failed
# July 31 22:07:54 mycomputername cacheclient[12017]: ERROR Process failed
# July 31 22:14:37 mycomputername utility[78832]: INFO Healthy resource usage
# July 31 22:22:34 mycomputername updater[78750]: ERROR ID: 10t
# July 31 22:41:00 mycomputername jam_tag=psim[40956]: ERROR The cake is a lie!
# July 31 22:42:51 mycomputername NetworkManager[28895]: INFO I'm sorry Dave. I'm afraid I can't do that
# July 31 23:15:22 mycomputername jam_tag=psim[75013]: ERROR Failed process [13966]
# July 31 23:17:05 mycomputername system[88316]: ERROR 418: I'm a teapot
# July 31 23:20:09 mycomputername system[42918]: ERROR Out of ink
# July 31 23:28:49 mycomputername utility[40452]: INFO Checking process [16121]
# July 31 23:29:25 mycomputername utility[22941]: WARN Failed to start CPU thread[39016]
# July 31 23:30:46 mycomputername process[99294]: WARN Computer needs to be turned off and on again
# July 31 23:35:49 mycomputername dhcpclient[10726]: INFO Googling the answer
# July 31 23:36:29 mycomputername updater[86053]: ERROR AssertionError 'False' is not 'True'
# July 31 23:40:05 mycomputername utility[88068]: INFO Generating Logs
# July 31 23:48:17 mycomputername CRON[28813]: WARN Please send help I am stuck inside the internet
# July 31 23:53:58 mycomputername CRON[59985]: INFO Successfully connected



# Resultado do erro extraido

# July 31 04:11:32 mycomputername CRON[51253]: ERROR: Failed to start CRON job due to script syntax error. Inform the CRON job owner!