@echo off

pandoc -V documentclass=extarticle -V fontsize=17pt -V pagestyle=empty -V geometry:margin=1cm -V mainfont="Carlito" ^
  recipes.md --pdf-engine=xelatex -o recipes.pdf