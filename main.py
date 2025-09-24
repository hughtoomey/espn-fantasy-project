import requests

league_id = 1405559583
year = 2025
swid = "38CCAB4B-3222-4674-9F17-1163B2B11233"
espn_s2 = "AECWBFakIHktXzPlY%2BoVCG4yPTBAvdSzbWm5%2Fhc4Eavbe1FGjCLfNcAHbzWrEjrcT0oSJ0ASZpCPGDvgTRAt8WC3%2BDNocWvWOgA46ivpCf4cMt0A9DBxwT0uWPc15lDujmg0zn7H8jy4za9BKLuZE5xk%2BncUIQTClkQUQt6Z9mETxbXhVW7I7GNpY5NrIg50S3hNTb%2FqBsXvftihWaijqQhJvkyHw221t90SU107awDLyVfYKtVfb8YE9pTCeiF75%2B468qyJbfzpyJTBaQZHLah5TAIV6KQAVM3FvODqDqC7ZQ%3D%3D"
url = "https://fantasy.espn.com/apis/v3/games/ffl/leagueHistory/" + \
      str(league_id) + "?seasonId=" + str(year)

r = requests.get(url,
                 cookies={"swid": "{" + swid + "}",
                          "espn_s2": espn_s2})
d = r.json()[0]