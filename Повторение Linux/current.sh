#! /bin/bash
mkdir hello_current
touch current.txt
cat > current.txt << EOF
Hello current!!
EOF
cat current.txt
ls -l current.txt
