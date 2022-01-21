#!/usr/bin/env sh

# abort on errors

# build
npm run build

# let git know about the /dist folder
git add -f dist && git commit -m "Initial dist subtree commit"
# add it to the gh-pages branch as a subtree
git subtree push --prefix dist origin gh-pages
