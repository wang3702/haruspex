
import os
from ops.argparser import argparser


if __name__ == "__main__":
    params = argparser()
    # print(params)
    if params['mode'] == 0:
        #evaluate using haruspex
        input_path = params['F']#mrc file dir
        study_file_path=params['M']
        type = params['type']
        input_path = os.path.abspath(input_path)
        if type == 0:
            indicate = 'SIMU6'
        elif type == 1:
            indicate = 'SIMU10'
        elif type == 2:
            indicate = 'SIMU'
        elif type == 3:
            indicate = 'REAL'
        else:
            print("we only have 4 type predictions: simulated(0,1,2) and real map(3)")
            exit()
        choose = params['choose']
        os.environ["CUDA_VISIBLE_DEVICES"] = choose
        from Evaluate.Evaluate_Haruspex import Evaluate_Haruspex
        Evaluate_Haruspex(input_path,study_file_path,indicate,type)

