"""
This is a python script that requires you have python installed, or in a cloud environment.

This script scrapes the CVS website looking for vaccine appointments in the cities you list.
To update for your area, update the locations marked with ### below.

If you receive an error that says something is not install, type

pip install beepy

in your terminal.

Source:
https://python.plainenglish.io/how-i-built-a-cvs-vaccine-appointment-availability-checker-in-python-6beb379549e4
"""


import requests
import time
import beepy
import subprocess


def findAVaccine():
    hours_to_run = 24
    # Update this to set the number of hours you want the script to run.
    max_time = time.time() + hours_to_run * 60 * 60
    while time.time() < max_time:

        state = "IL"  ###Update with your state abbreviation. Be sure to use all CAPS, e.g. RI

        url = "https://www.cvs.com/immunizations/covid-19-vaccine"

        response = requests.get(
            "https://www.cvs.com/immunizations/covid-19-vaccine.vaccine-status.{}.json?vaccineinfo".format(
                state.lower()
            ),
            headers={"Referer": url},
        )
        payload = response.json()

        mappings = {}
        for item in payload["responsePayloadData"]["data"][state]:
            mappings[item.get("city")] = item.get("status")

        print(time.ctime())
        cities = ["CHICAGO"]  ###Update with your cities nearby
        for city in cities:
            print(city, mappings[city])

        for key in mappings.keys():
            if (key in cities) and (mappings[key] != "Fully Booked"):
                subprocess.Popen(["open", url])
                for _ in range(20):  # repeat sound 20 times
                    beepy.beep(sound="coin")
                break
            else:
                pass

        time.sleep(60)
        # This runs every 60 seconds. Update here if you'd like it to go every 5min (300sec)
        print("\n")


findAVaccine()  ###this final line runs the function. Your terminal will output the cities every 60seconds

