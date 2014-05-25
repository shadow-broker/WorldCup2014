import urllib2
import json
import sys
import datetime
from bs4 import BeautifulSoup

def parse_matches(url='http://en.wikipedia.org/wiki/2014_FIFA_World_Cup'):
  response = urllib2.urlopen(url)
  soup = BeautifulSoup(response.read())
  ret = dict()

  for h3 in soup('h3'):
    if not h3.text.startswith('Group'):
      continue

    matches = list()

    for div in h3.find_next_siblings('div', {'class' : 'vevent'}, limit=6):
      match = dict()
      tables = div('table')

      date_string = tables[0].text.replace('\n', ' ').strip()
      date = datetime.datetime.strptime(date_string, '%d %B %Y %H:%M')
      date += datetime.timedelta(hours=3) # times listed in UTC-3
      match['Date'] = date.isoformat()

      teams = tables[1].text.strip().split('\n')
      match['Home Team'] = teams[0].strip()
      match['Match'] = int(teams[1].split(' ')[1])
      match['Away Team'] = teams[2].strip()

      venue = tables[2].text.strip()
      match['Venue'] = venue

      matches.append(match)
      
    ret[h3.text] = matches

  return ret

if __name__ == '__main__':
  matches = parse_matches()
  dump = json.dumps(matches, sort_keys=True, indent=4, separators=(',', ': '))

  if len(sys.argv) > 1:
    with open(sys.argv[1], 'w') as f:
      f.write(dump)
  else:
    print dump
