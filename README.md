remote create github repository

echo "# thrift-py" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/blanker/thrift-py.git
git push -u origin master