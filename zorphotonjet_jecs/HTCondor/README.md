# 🖱️ Submit jobs to HTCondor (T2B)

## 💡 How to
1. Check the available options by running:
```bash
./SubmitToHTCondor.sh
```
2. The arguments needed are:
   - **Dataset** ➡️ Choose among: All || EGamma || Muon || SingleMuon || G-4Jets.
   - **Year** ➡️ Choose among: 2022 || 2023.
   - **Era** ➡️ Depends on the year and dataset (check the [Datasets folder](Datasets)).
   - **Output** ➡️ The directory (for the output root files) to be created in:
     ```bash
     /pnfs/iihe/cms/store/user/${USER}/JEC/<Year>/<Dataset>/Run<Era>/
     ```
     You can modify this option within the script by setting the ```$output``` variable.
3. Example:
   ```bash
   ./SubmitToHTCondor.sh EGamma 2022 C Validation
   ```

## ℹ️ Information
The [SubmitToHTCondor.sh](SubmitToHTCondor.sh) script proceeds as follows:
1. Checks the validity of the provided arguments: dataset, year etc.
2. Uses the [Template.sub](Template.sub) and [Template.sh](Template.sh) as templates for the submission:
   - [Template.sub](Template.sub) is the submission file as this would be submitted with ```condor_submit```
   - [Template.sh](Template.sh) is the executable script which runs the analysis ```python3 ...```
3. It creates 2 new scripts (based on the templates) with the input dataset(s), path configuration etc.
4. It creates a sub-directory ```JobSub``` (within HTCondor directory) which is used as submission directory.  
   The ```JobSub``` directory holds the 2 new scripts, along with directories for job progress reporting:
   - error
   - log
   - output
   
   You can modify the sub-directory name within the script by setting the ```$jobsub``` variable.
5. The output root files will be stored in the directory:
   ```bash
   /pnfs/iihe/cms/store/user/${USER}/JEC/<Year>/<Dataset>/Run<Era>/<Output>
   ```
   You can modify this option within the script by setting the ```$output``` variable.
6. Finally, the script prints information with the location of submission, job reporting and output root files.

## ⚠️ For the moment the scripts has been tested for:
- Dataset = EGamma
- Year = 2022
- Era = C
   
