python3 create_large_file.py

cd ./sorted_files
split --verbose -l70000  ../large.txt sorted_
cd ..