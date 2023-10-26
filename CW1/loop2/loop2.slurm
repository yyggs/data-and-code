#!/bin/bash

# Slurm job options (name, compute nodes, job time)
#SBATCH --job-name=loop
#SBATCH --time=0:20:0
#SBATCH --exclusive
#SBATCH --nodes=1
#SBATCH --tasks-per-node=1
#SBATCH --cpus-per-task=36

# Replace [budget code] below with your budget code (e.g. dc116-s1234567)
#SBATCH --account=m23oc-s2484724
# We use the "standard" partition as we are running on CPU nodes
#SBATCH --partition=standard
# We use the "short" QoS as our runtime is less than 20 minutes
#SBATCH --qos=short

module load intel-20.4/compilers

# Change to the submission directory
cd $SLURM_SUBMIT_DIR


# Set the number of threads 
export OMP_NUM_THREADS=8

# Launch the parallel job
run() {
    # Save $OMP_SCHEDULE and $OMP_NUM_THREADS to the CSV
    echo -n "$OMP_SCHEDULE," >> $OUTPUT_FILE

    # Append the output of ./loop to the CSV
    srun --cpu-bind=cores ./loop >> $OUTPUT_FILE
}

# Experiment loop for 10 runs
for experiment_num in $(seq 1 50)
do
    # Each experiment gets its own output file
    OUTPUT_FILE="loop2/data_output_${experiment_num}.csv"
    echo "OMP_SCHEDULE,Chunksize,Time_Loop1,Time_Loop2" > $OUTPUT_FILE

    # 将OpenMP并行化线程数设置为8
    export OMP_NUM_THREADS=8



    # 动态调度策略带有块大小
    declare -a dynamic_chunksizes=("1" "2" "4" "8" "16")
    for chunk in "${dynamic_chunksizes[@]}"
    do
        export OMP_SCHEDULE="DYNAMIC,$chunk"
        run
    done


done
