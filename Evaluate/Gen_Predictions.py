import os
from ops.os_operation import mkdir

def Gen_Predictions(all_map_path,save_path):
    code_path = os.path.join(os.getcwd(), 'source')
    code_path = os.path.join(code_path, 'hpx_unet_190116.py')
    network_path = os.path.join(os.getcwd(), 'network')
    network_path = os.path.join(network_path, 'hpx_190116')
    listfiles = os.listdir(all_map_path)
    for item in listfiles:
        tmp_output_path = os.path.join(save_path, item[:-4])
        mkdir(tmp_output_path)
        tmp_map_path = os.path.join(all_map_path, item)
        run_cmd = "python3 " + code_path + " -n " + network_path + " -d map-predict " + tmp_map_path + " -o " + tmp_output_path
        os.system(run_cmd)