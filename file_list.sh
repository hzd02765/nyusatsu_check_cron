#!/bin/sh

# $B%U%!%$%k$d%G%#%l%/%H%j$r8!:w$7!"%U%!%$%k$K=q$-=P$9(B

# find : $B%U%!%$%k$d%G%#%l%/%H%j$r8!:w(B
# -type c
# $B;XDj$7$?%U%!%$%k!&%?%$%W$r8!:w$9$k!#(B
# c$B$O(Bd$B$,%G%#%l%/%H%j$r!"(Bf$B$,DL>o%U%!%$%k$r!"(Bl$B$,%7%s%\%j%C%/!&%j%s%/$rI=$9(B
# -name pattern
# $B%U%!%$%kL>$,(Bpattern$B$HF1$8%U%!%$%k$r8!:w$9$k!#(B
# $B%o%$%k%I!&%+!<%I$rMQ$$$k$3$H$,$G$-$k(B

# find /usr/local/app/nyusatsu_check_cron -type f -name "*.py" | sort > file_list.txt
find -type f -name "*.py" | sort > file_list.txt
