#! /bin/bash
cd ..
mkdir hello_parent
touch parent.txt
cat > home.txt << EOF
Hello parent!!
EOF
cat parent.txt
ls -l parent.txt
