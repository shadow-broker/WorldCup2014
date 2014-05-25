import urllib2
import json
import sys
from bs4 import BeautifulSoup

def parse_groups(url='http://en.wikipedia.org/wiki/2014_FIFA_World_Cup', name_only=False):
  response = urllib2.urlopen(url)
  soup = BeautifulSoup(response.read())
  ret = dict()

  for h3 in soup('h3'):
    if not h3.text.startswith('Group'):
      continue

    teams = list()

    table = h3.find_next_sibling('table')
    header_row = table('tr')[0]

    for row in table('tr')[1:]:
      if name_only:
        team = row('td')[0].text.strip()
      else:
        team = dict()

        for th, td in zip(header_row('th'), row('td')):
          if th('abbr'):
            string = th('abbr')[0]['title']
          else:
            string = th.text.strip().split('\n')[0]

          value = td.text.strip()
          try:
            value = int(value)
          except ValueError:
            pass

          team[string] = value

      teams.append(team)

    ret[h3.text] = teams

  return ret

if __name__ == '__main__':
  groups = parse_groups()
  dump = json.dumps(groups, sort_keys=True, indent=4, separators=(',', ': '))

  if len(sys.argv) > 1:
    with open(sys.argv[1], 'w') as f:
      f.write(dump)
  else:
    print dump
