import psutil # aqui o disk_usage() da tambem a porcentagem usada ao contrario do shutil

def check_disk_usage (path): # Vai dar as informações do disco usado
    disk_info = psutil.disk_usage(path) # (total = , used = , free = , percent = )
    free_disk_percent = 100 - disk_info.percent
    return free_disk_percent > 20 # Tem no minimo 20% livre?

def check_cpu_usage():
    cpu_percent = psutil.cpu_percent(1)
    return cpu_percent < 75 # usando mais de 75%?

if not check_disk_usage("D:\\") or not check_cpu_usage():
    print("Error : Free Disk: {:.1f}% || CPU: {}%".format(100-psutil.disk_usage("C:\\").percent,psutil.cpu_percent(1)))
else:
    print("OK")