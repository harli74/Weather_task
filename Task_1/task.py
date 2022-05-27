import sys
sys.path.extend(['Weather_task'])
import Resources
Resources.__path__
import Resources.Logic


def Execute():
    Resources.Logic.CityGenerate.Generate()
    Resources.Logic.CityGenerate.Input(input())


Execute()
