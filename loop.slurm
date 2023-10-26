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

run() {
    # Save $OMP_SCHEDULE to the CSV
    echo -n "$OMP_SCHEDULE," >> $OUTPUT_FILE

    # Append the output of ./loop to the CSV
    srun --cpu-bind=cores ./loops >> $OUTPUT_FILE
}

# Set the number of threads to 32
export OMP_NUM_THREADS=32

# Experiment loop for 10 runs
for experiment_num in $(seq 11 20)
do
    # Each experiment gets its own output file
    OUTPUT_FILE="data_output_${experiment_num}.csv"
    echo "SchedulingType,Chunksize,Time_Loop1,Time_Loop2" > $OUTPUT_FILE

    # Loop over the desired scheduling types and their corresponding chunk sizes
    for schedule_type in STATIC DYNAMIC GUIDED
    do
        for chunk_size in 16
        do
            export OMP_SCHEDULE="${schedule_type},${chunk_size}"
            #echo "${schedule_type},${chunk_size}" >> $OUTPUT_FILE
            run >>  $OUTPUT_FILE
        done
    done
done
