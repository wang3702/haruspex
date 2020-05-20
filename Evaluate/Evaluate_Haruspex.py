import os
from ops.os_operation import mkdir

def Evaluate_Haruspex(input_path,study_file_path,indicate,type):
    test_id_list = []  # the list which we needs to get phase2 input
    if type!=3:
        with open(study_file_path, 'r') as file:
            line = file.readline()
            while line:
                line = line.strip()
                test_id_list.append(line)
                line = file.readline()
    else:
        for k in range(4):
            tmp_study_path=os.path.join(study_file_path,'Fold'+str(k)+'.txt')
            tmp_list=[]
            with open(tmp_study_path, 'r') as file:
                line = file.readline()
                while line:
                    line = line.strip()
                    tmp_list.append(line)
                    line = file.readline()
            tmp_list=tmp_list[:5]
            test_id_list+=tmp_list
    print("We have %d maps to evaluate" % len(test_id_list))
    output_path=os.path.join(os.getcwd(),"Predict_Result")
    mkdir(output_path)
    output_path=os.path.join(output_path,indicate)
    mkdir(output_path)
    listfiles=os.listdir(input_path)
    code_path=os.path.join(os.getcwd(),'source')
    code_path=os.path.join(code_path,'hpx_unet_190116.py')
    network_path=os.path.join(os.getcwd(),'network')
    network_path=os.path.join(network_path,'hpx_190116')
    for item in listfiles:
        if item[:4] not in test_id_list:
            continue
        tmp_output_path=os.path.join(output_path,item[:4])
        mkdir(tmp_output_path)
        tmp_map_path=os.path.join(input_path,item)
        run_cmd="python3 "+code_path+" -n "+network_path+" -d map-predict "+tmp_map_path+" -o "+tmp_output_path
        os.system(run_cmd)





