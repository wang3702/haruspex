def Prepare_Visualize_Real(outputFile,Visual_real_path):
    with open(outputFile,'r') as file1:
        with open(Visual_real_path,'w') as file2:
            line=file1.readline()
            line=file1.readline()
            while line:
                line = line.strip('\n')
                result = line.split(',')
                if result[3]=='-1':
                    line=file1.readline()
                    continue
                file2.write(result[3]+'\n')
                line=file1.readline()