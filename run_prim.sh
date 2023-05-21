#!/bin/zsh

algorithm="prim_smarter.py"
inputpath="../test_files_2023_05_15"
outputpath="../outputs_2023_05_21_v4"

python3 $algorithm < $inputpath/input01.txt > $outputpath/output01.txt
python3 $algorithm < $inputpath/input02.txt > $outputpath/output02.txt
python3 $algorithm < $inputpath/input03.txt > $outputpath/output03.txt
python3 $algorithm < $inputpath/input04.txt > $outputpath/output04.txt
python3 $algorithm < $inputpath/input05.txt > $outputpath/output05.txt
python3 $algorithm < $inputpath/input06.txt > $outputpath/output06.txt
python3 $algorithm < $inputpath/input07.txt > $outputpath/output07.txt
python3 $algorithm < $inputpath/input08.txt > $outputpath/output08.txt
python3 $algorithm < $inputpath/input09.txt > $outputpath/output09.txt
python3 $algorithm < $inputpath/input10.txt > $outputpath/output10.txt
python3 $algorithm < $inputpath/input11.txt > $outputpath/output11.txt
python3 $algorithm < $inputpath/input12.txt > $outputpath/output12.txt
python3 $algorithm < $inputpath/input13.txt > $outputpath/output13.txt
python3 $algorithm < $inputpath/input14.txt > $outputpath/output14.txt
python3 $algorithm < $inputpath/input15.txt > $outputpath/output15.txt
python3 $algorithm < $inputpath/input16.txt > $outputpath/output16.txt
python3 $algorithm < $inputpath/input17.txt > $outputpath/output17.txt
python3 $algorithm < $inputpath/input18.txt > $outputpath/output18.txt
python3 $algorithm < $inputpath/input19.txt > $outputpath/output19.txt
python3 $algorithm < $inputpath/input20.txt > $outputpath/output20.txt

echo "Done!"