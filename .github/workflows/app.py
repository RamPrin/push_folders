import argparse

import yaml

parser = argparse.ArgumentParser()
parser.add_argument('--path')
parser.add_argument('--url')
parser.add_argument('--out')
args = parser.parse_args()

data = yaml.load(open(args.path), yaml.FullLoader)
app = [*data.keys()][0]
print(data[app]['app']['container_ref'])
data[app]['app']['container_ref'] = args.url
yaml.dump(data, open(args.out, 'w'))
yaml.dump(data, open(args.path, 'w'))
