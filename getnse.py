from pynse import *
import yaml

nse = Nse()

def clear():
    os.system('clear')

def nse_clr():
    nse.clear_data()

def EQ(Stk):
    x = nse.get_quote(Stk)
    print(yaml.dump(x, sort_keys=False, default_flow_style=False))

def FD():
    print(nse.fii_dii().T)

def gainers(x=10):
    print(nse.top_gainers(index=IndexSymbol.FnO, length=x))

def losers(x=10):
    print(nse.top_losers(index=IndexSymbol.FnO, length=x))
