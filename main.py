# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

def greet(name, groet = 'Hello, <name>!'):
    if name or groet:
        x = groet.replace('<name>', name)
    return x 

# dic_mass wordt niet 'gebruikt' in def force(), is alleen bedoelt om mass per planeet op te zoeken:
dic_mass = {'planeten_mass':{
	'Sun':1.9891 * 10**30,
	'Jupiter': 1.8986 * 10**27,
	'Saturn':5.6846 * 10**26,
	'Neptune':10.243 * 10**25,
	'Uranus': 8.6810 * 10**25,
	'Earth':5.9736 * 10**24,
	'Venus':4.8685 * 10**24,
	'Mars':	6.4185 * 10**23,
	'Mercury': 3.3022 * 10**23,
	'Moon':	7.349 * 10**22,
	'Pluto':1.25 * 10**22}}

dic_gravety = {'planeten_gravety':
	{'sun':'274.0',
	'jupiter':'24.9',
	'neptune':'11.2',
	'saturn':'10.4',
	'earth':'9.8',
	'uranus':'8.9',
	'venus':'8.9',
	'mars':'3.7',
	'mercury':'3.7',
	'moon':'1.6',
	'pluto':'0.6'}}

def force(mass, body = 'earth'):
	body = dic_gravety['planeten_gravety'][body]
	return mass*float(body)


def pull(m1, m2, d):
	G = (6.674*(10**-11))
	pull = (G*((m1*m2)/(d**2)))
	return pull









 


	











  
