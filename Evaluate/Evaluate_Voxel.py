import os
import numpy as np
import sklearn
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
from ops.os_operation import mkdir
from collections import defaultdict
def Evaluate_Voxel(haru_path,input_path,type,indicate):
    factor=2
    listfiles=[x for x in os.listdir(input_path) if "predict.txt" in x]
    save_path=haru_path
    tmp_csv_path = os.path.join(save_path, 'harusPerformance_' + str(indicate) + "_fixed.csv")
    Accuracy_Dict = defaultdict(list)
    F1_Dict = defaultdict(list)
    with open(tmp_csv_path, 'w') as csvfile:
        csvfile.write("PDB_ID,Beta f1, Alpha f1,DRNA f1, overall f1,Beta recall, Alpha recall,DRNA recall, overall recall\n")
        for item in listfiles:
            tmp_predict_path = os.path.join(input_path, item)
            pdb_id = item[:4]
            tmp_haru_path = os.path.join(haru_path, pdb_id)
            if type != 3:
                tmp_haru_path = os.path.join(tmp_haru_path, pdb_id + "_predict4.npz")
            else:
                tmp_haru_path = os.path.join(tmp_haru_path, pdb_id + "_new_predict4.npz")  # resized predictions
            # get our label
            Label_dict = {}
            with open(tmp_predict_path, 'r') as file:
                line = file.readline()
                while line:
                    split_result = line.split()
                    location = split_result[0]
                    label = int(split_result[1])
                    Label_dict[location] = label
                    line = file.readline()
            haru_result = np.load(tmp_haru_path)
            haru_result = haru_result['map']
            tR = []
            pR = []
            for location in Label_dict.keys():
                split_result = location.split(',')
                z = int(int(split_result[0]) * factor)
                y = int(int(split_result[1])* factor)
                x = int(int(split_result[2])* factor)
                tmp_label = Label_dict[location] - 1  # 0: beta 1:alpha 2:dna/rna
                if tmp_label==-1:
                    continue#do not evaluate coil
                tmp_pred = int(np.argmax(haru_result[x, y, z]))
                tmp_sum = np.sum(tmp_pred)
                if tmp_sum == 0:
                    tmp_pred = 3  # denotes nothing here
                tR.append(tmp_label)
                pR.append(tmp_pred)
            # calculate the f1 score, recall(accuracy)
            f1score = f1_score(tR, pR, labels=[0, 1, 2, 3], average=None)
            print("f1 score:" + str(f1score))
            overall_f1score = f1_score(tR, pR, average="weighted", zero_division=1)
            csvfile.write(item[:4] + ",")
            csvfile.write(str(f1score[0]) + "," + str(f1score[1]) + "," + str(f1score[2]) + ","+str(overall_f1score)+",")
            true_array=tR
            pred_array=pR
            accuracy = recall_score(true_array, pred_array, labels=[0, 1, 2, 3], average=None)
            overall_accuracy = recall_score(true_array, pred_array, average='weighted', zero_division=1)
            csvfile.write(
                str(accuracy[0]) + "," + str(accuracy[1]) + "," + str(accuracy[2]) + "," + str(accuracy[3]) + "," + str(
                    overall_accuracy) + ",\n")
            tmp_true_array = np.array(true_array)
            for k in range(4):
                if len(np.argwhere(tmp_true_array == k)) != 0:
                    F1_Dict[k].append(f1score[k])
                    Accuracy_Dict[k].append(accuracy[k])
                else:
                    print("We do not have %d structures for this structure %s" % (k, item[:4]))
            F1_Dict[4].append(overall_f1score)
            Accuracy_Dict[4].append(overall_accuracy)

    final_report_path= os.path.join(save_path, 'map_based_report.txt')
    with open(final_report_path, 'w') as file:
        file.write("Type\tF1 score\tAccuracy\n")
        for key in F1_Dict:
            file.write(str(key) + "\t")
            file.write(str(np.mean(F1_Dict[key])) + "\t")
            file.write(str(np.mean(Accuracy_Dict[key])) + "\t")








