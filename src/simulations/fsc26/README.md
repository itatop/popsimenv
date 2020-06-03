#fsc26

This readme should use us to document the usage and the algorithms of fsc26.
The main source of information is from the official manual (see fastsimcoal26.pdf).

#introduction:

there are 2 main ways to run fsc26:

1. Simulating population trees with parameters (as msprime does):

    ```fsc26 -i test.par -n 100```

2. Estimating parameters from the site frequency spectrum (more relevant to us)

    ```fsc26 -t test.tpl -n 10 -e test.est -E 100```
		
    > see page 39 in the manual for more info on estimating parameters

#file types:

.par

    file extention is a special fsc26 format describes the demographic events and population parameters for simulation.
    
.tpl

    file extention is the same format as ".par", but allows missing parameters to be placed instead of values.
    
.est

    file extention is a format which describes how to sample the missing parameters in a ".tpl" file.
    
.obs

    observed joint SFS. the file is used when exists with the suffix "_jointDAFpop1_0.obs"

Here are the matching ".tpl" and ".est" files used in the two_population_analysis:

IM_hum.tpl:
```
//Parameters for the coalescence simulation program : simcoal.exe
2 samples to simulate :
//Population effective sizes (number of genes)
NPOP1
NPOP2
//Samples sizes
SAMPLE_SIZE
SAMPLE_SIZE
//Growth rates: negative growth implies population expansion
0
0
//Number of migration matrices : 0 implies no migration between demes
2
//Migration matrix 0
0 MIG21
MIG12 0
//Migration matrix 1
0 0
0 0
//historical event: time, source, sink, migrants, new deme size, growth rate, migr mat index
1 historical event
TDIV 0 1 1 RESIZE 0 1
//Number of independent loci [chromosome]
1 0
//Per chromosome: Number of contiguous linkage Block: a block is a set of contiguous loci
1
//per Block:data type, number of loci, per gen recomb and mut rates
FREQ 1 0 1e-8 OUTEXP
```




IM_hum.est:

```
// Priors and rules file
// *********************

[PARAMETERS]
//#isInt? #name   #dist.#min  #max
//all N are in number of haploid individuals
1  ANCSIZE     unif     100  100000   output
1  NPOP1       unif     100  100000   output
1  NPOP2       unif     100  100000   output
0  N1M21       logunif  1e-2 20       hide
0  N2M12       logunif  1e-2 20       hide
1  TDIV        unif     100   20000   output


[RULES]

[COMPLEX PARAMETERS]

0  RESIZE = ANCSIZE/NPOP2     hide
0  MIG12  = N1M21/NPOP1       output
0  MIG21  = N2M12/NPOP2       output
```

first, lets translate the .tpl file and understand what we are simulating:
we have 1 historical event which accours TDIV generations ago. lets break the historical event params into 3 parts:
a. the "0 1 1" means pop0 merges into pop1 by the proportion of 1. in other words - all pop0 merged into pop1.
b. "RESIZE" is the new size of pop1 relative to its size before the merge.
we can see from the .est file that this parameter derive from ANCSIZE/NPOP2 as expected, since NPOP2 is pop1 size and ANCSIZE is pop1 size after the merge.
c. "0 1" means we fix pop1 size and switching to migration matrix 1.
so we simulating the migration of two populations from one common population X generations ago.

after the historical event section, we see the section describing the number of chromosomes and blocks, block size, and mutation rate:
this setting sets 1 chromosome and one block.
i believe "FREQ 1 0 1e-8 OUTEXP" means frequency of '1' site, 0 (no) recombination rate, 1e-8 mutation rate.
from the menual: "OUTEXP: Output of expected site frequency spectrum for estimated parameters of the model"

now lets look at the .est file to see the estimated parameters settings:
ANCSIZE, NPOP1, NPOP2 are the populations sizes. all integers uniformly sampled from 100 to 100000.
TDIV is the generation t value, integer uniformly sampled from 100 to 20000.
N1M21, N2M12 are floats log-uniformly dist sampled from 0.02 to 20. these values control the migration rate.

> note that SAMPLE_SIZE is not an estimated parameter, but is replaced by the Snakefile in the "fsc_setup" rule.


# running
	
lets look at the fsc26 commandline used in the Snakefile:

```fsc26 -t IM_hum.tpl -n 100000 -d -e IM_hum.est -M -L 40 -q -c 4```

the passing of .tpl/.est files suggest it is a parameter estimation launch.
-n is the number of simulations and -d is to compute the derived SFS
-M is for using max liklihood, and -L sets the number of ECM loops.
-q sets "quiet" output
-c sets number of CPUs

this commandline is iterates 10 runs, each time it copies the files IM_hum.est, IM_hum.tpl, IM_hum_jointDAFpop1_0.obs from the source directory.
it looks to me that only the the 10-th run is used and the first 9 runs has no effect.
