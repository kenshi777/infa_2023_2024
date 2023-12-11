#! /bin/bash
cd /tmp
mkdir hello_world
cd hello_world
touch absolute.txt
cat > absolute.txt << EOF
Hello world!
EOF
ls -l

