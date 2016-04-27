awk -F, '
    BEGIN { midnight = mktime(strftime("%Y %m %d 0 0 0", systime())) }
    {
        seconds = $1 / 1e3
        fraction = $1 % 1e3
        printf "%s.%03d,%s\n", strftime("%T", midnight + seconds), fraction, $0
    }
'
