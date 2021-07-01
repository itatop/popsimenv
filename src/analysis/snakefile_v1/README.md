# Snakefile_v1

> The template directory is the basis of running a new experiment using snakefile_v1. It contains essential code & files for every experiment.
> Usage:
> 1. Copy the template dir and paste it in the current dir (or sub-dir) with an informative name.
> 2. Modify the config.json file in the “experiment” dir, based on the configurations for this run.
> 3. Modify params_extractor.py if needed.
> 4. Run in terminal : 
	```bash
    snakemake -j 1 --config config="experiment"
    ```
> 5. Wait for results and analyze.
> 6. Create a README.md that documents this experiment inside the pasted directory.
