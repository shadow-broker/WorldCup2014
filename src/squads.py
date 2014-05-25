import urllib2
import json
import sys
import datetime
from bs4 import BeautifulSoup

def parse_squads(url='http://en.wikipedia.org/wiki/2014_FIFA_World_Cup_squads'):
  response = urllib2.urlopen(url)
  soup = BeautifulSoup(response.read())
  ret = dict()

  for h2 in soup('h2'):
    if not h2.text.startswith('Group'):
      continue

    squads = dict()

    for h3 in h2.find_next_siblings('h3', limit=4):
      squad = dict()

      p = h3.find_next_sibling('p')
      coach = p.text.split(':')[1].strip()
      squad['Coach'] = coach

      table = h3.find_next_sibling('table')('table')[0]
      header_row = table('tr')[0]
      players = list()

      for row in table('tr')[1:]:
        player = dict()

        for th, td in zip(header_row('th'), row('td')):
          for span in td('span', {'style' : 'display:none'}):
            span.extract()
          string = th.text.strip()

          value = td.text.strip()
          try:
            value = int(value)
          except ValueError:
            pass
          if value == u'\u2013':
            value = None

          player[string] = value

        players.append(player)

      squad['Players'] = players
      squads[h3.text] = squad

    ret[h2.text] = squads

  return ret

if __name__ == '__main__':
  squads = parse_squads()
  dump = json.dumps(squads, sort_keys=True, indent=4, separators=(',', ': '))

  if len(sys.argv) > 1:
    with open(sys.argv[1], 'w') as f:
      f.write(dump)
  else:
    print dump
