# iss.py

A brutally simple python script for getting predictions on the next time ISS
will come visit.

This makes use of `ipecho.net` and `freegeoip.net` to determine your location,
and `open-notify.org` for predictions.

Returns 10 predictons at a time.  Prediction times are based on when ISS is at
10 degrees above the horizon based on an observer altitude of 80m.
