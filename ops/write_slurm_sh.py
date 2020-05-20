import os
from ops.os_operation import mkdir
def write_slurm_sh(id,command_line,outlog_path):
    run_path=os.path.join(os.getcwd(),'log')
    mkdir(run_path)
    batch_file=os.path.join(run_path,'slurm-job'+str(id)+'.sh')
    with open(batch_file,'w') as file:
        file.write('#!/usr/bin/env bash\n')
        file.write('\n')
        file.write('#SBATCH -o '+outlog_path+'\n')
        file.write('#SBATCH -p kihara\n')
        file.write('#SBATCH --cpus-per-task=1\n')
        file.write('#SBATCH --ntasks=1\n')
        file.write(command_line+'\n')
    return batch_file

