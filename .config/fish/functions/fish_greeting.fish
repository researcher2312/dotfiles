set processes (pgrep -f fish | wc -l)

if test $processes = 1
    command fastfetch
end
