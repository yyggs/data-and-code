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
#SBATCH --qos=standard

module load intel-20.4/compilers

# Change to the submission directory
cd $SLURM_SUBMIT_DIR

run() {
    # Save $OMP_SCHEDULE and $OMP_NUM_THREADS to the CSV
    echo -n "$OMP_NUM_THREADS," >> $OUTPUT_FILE

    # Append the output of ./loop to the CSV
    srun --cpu-bind=cores ./loop >> $OUTPUT_FILE
}

# Experiment loop for 10 runs
for experiment_num in 41
do
    # Each experiment gets its own output file
    OUTPUT_FILE="data_output_${experiment_num}.csv"
    echo "NumThreads,Time_Loop1,Time_Loop2" > $OUTPUT_FILE

    export OMP_SCHEDULE="DYNAMIC,4"

    # Loop over the desired number of threads
    for threads in 1 2 4 6 8 12 16 18 24 28 32
    do
        export OMP_NUM_THREADS=$threads
        run
    done

done
