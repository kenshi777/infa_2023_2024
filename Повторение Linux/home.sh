#! /bin/bash
cd ~
mkdir hello_home
touch home.txt
cat > home.txt << EOF
Hello home!!
EOF
cat home.txt
ls -l home.txt
