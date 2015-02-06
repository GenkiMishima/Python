import os
os.system("""
gnuplot <<EOF
set grid
set xlabel "time"
set ylabel "rates"
set terminal png
set key below
set output "plot/Ast_Doller.png"
p "rates/Ast_Doller.d" w lp
EOF""" )
