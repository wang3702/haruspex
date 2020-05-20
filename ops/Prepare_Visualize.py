import os
def Prepare_Visualize(trimmap_path,pred_dict,Visual_trimmap_path,Visual_predict_path):
    write_lines=[]
    write_pred=[]
    write_Real=[]
    use_flag=False
    with open(trimmap_path,'r') as fil1:
        line=fil1.readline()
        while line:
            if (line.startswith('#Base') or line.startswith('#Steps')):
                write_lines.append(line)
                line=fil1.readline()
                continue

            elif (line.startswith("#Voxel")):
                print('!!!!!!!!!1here!!!!!!!!!!!!!!!!!')
                write_lines.append(line)
                line=fil1.readline()
                continue
            elif (line.startswith('#C:')):
                split_Result=line.split()
                label=int(split_Result[2])
                if label==-1:
                    line=fil1.readline()
                    continue
                else:
                    write_lines.append(line)
                    equ = line.split('=')
                    coords = equ[-2].split(' ')[1:4]  # use real coord
                    search_str=''
                    for k in range(3):
                        search_str+=str(int(float(coords[k])))+','
                    if search_str in pred_dict:
                        pred_result=pred_dict[search_str]
                        write_pred.append(str(pred_result)+'\n')
                        use_flag=True
                    else:
                        use_flag=False
                    line=fil1.readline()
                    continue
            elif (line.startswith("-1")):
                line=fil1.readline()
                continue
            if use_flag:
                write_lines.append(line)


            line=fil1.readline()
    with open(Visual_trimmap_path,'w') as file:
        for line in write_lines:
            file.write(line)
    with open(Visual_predict_path,'w') as file:
        for line in write_pred:
            file.write(line)



