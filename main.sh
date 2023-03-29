rm -rf .git
git init
git remote add origin git@github.com:zzhassulan/bash.git
git add . && git commit -m "all"
git push -u origin master
escho "Все было залито в GitHub"