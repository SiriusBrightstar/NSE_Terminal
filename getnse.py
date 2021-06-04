from pynse import *
import yaml

nse = Nse()

def welp():
    print('clear():         Clears Screen')
    print('nse_clr():       Clears Data')
    print('EQ(\'Ticker\'):  Prints Stock Info')
    print('MM():            Prints FII & DII data. MM: Market Manipulators')
    print('stonk(n):        Prints n Top Gainers (F&O Only)')
    print('stink(n):        Prints n Top Losers (F&O Only)')

def clear():
    os.system('clear')

def nse_clr():
    nse.clear_data()

def EQ(Stk):
    x = nse.get_quote(Stk)
    print(yaml.dump(x, sort_keys=False, default_flow_style=False))

def MM():
    print(nse.fii_dii().T)

def stonk(x=10):
    print(nse.top_gainers(index=IndexSymbol.FnO, length=x))

def stink(x=10):
    print(nse.top_losers(index=IndexSymbol.FnO, length=x))
