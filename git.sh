#!/bin/sh

git add . 
read com 
git commit -m "$com"
ggpush

