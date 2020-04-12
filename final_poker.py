from flask import Flask , render_template,redirect
import random
from poker_winner import winner


app = Flask(__name__)

@app.route('/')
def welcome():
	global p_a
	global p_b
	global center_cards
	p_a = []
	p_b = []
	center_cards =[]
	for i in range(2):
		p_a.append(deck.pop())
		p_b.append(deck.pop())
	for i in range(5):
		center_cards.append(deck.pop())
	c='background_img.jpg'
	return render_template("poker_strt.html",show=c)

@app.route('/deal')
def w():
	global p_a
	global p_b
	global d
	c='background_img.jpg'
	cd=[]
	cd1=[]
	cd2 = []
	for i in p_a:
		a=i.split()
		cd.append(d[a[0]][a[2]])
	for i in p_b:
		cd1.append("cover.png")
	for i in range(5):
		cd2.append("cover.png")
	return render_template('poker_home.html',show=c,show1=cd,show2=cd1,show3=cd2)

@app.route('/pass')
def pas():
	global p_a
	global p_b
	global center_cards
	global d
	c='background_img.jpg'
	cd=[]
	cd1=[]
	cd2 = []
	for i in p_a:
		a=i.split()
		cd.append(d[a[0]][a[2]])
	for i in p_b:
		cd1.append("cover.png")
	for i in range(3):
		a = center_cards[i].split()
		cd2.append(d[a[0]][a[2]])
	for i in range(2):
		cd2.append("cover.png")	
	return render_template('pass1.html',show=c,show1=cd,show2=cd1,show3=cd2)

@app.route('/pass2')
def pas1():
	global p_a
	global p_b
	global center_cards
	global d
	c='background_img.jpg'
	cd=[]
	cd1=[]
	cd2 = []
	for i in p_a:
		a=i.split()
		cd.append(d[a[0]][a[2]])
	for i in p_b:
		cd1.append("cover.png")
	for i in range(4):
		a = center_cards[i].split()
		cd2.append(d[a[0]][a[2]])
	for i in range(1):
		cd2.append("cover.png")	
	return render_template('pass2.html',show=c,show1=cd,show2=cd1,show3=cd2)


@app.route('/pass3')
def pas2():
	global p_a
	global p_b
	global center_cards
	global d
	c='background_img.jpg'
	cd=[]
	cd1=[]
	cd2 = []
	for i in p_a:
		a=i.split()
		cd.append(d[a[0]][a[2]])
	for i in p_b:
		cd1.append("cover.png")
	for i in range(5):
		a = center_cards[i].split()
		cd2.append(d[a[0]][a[2]])	
	return render_template('pass3.html',show=c,show1=cd,show2=cd1,show3=cd2)


@app.route('/show')
def show():
	global p_a
	global p_b
	global center_cards
	global d
	global m
	c='background_img.jpg'
	cd=[]
	cd1=[]
	cd2 = []
	for i in p_a:
		a=i.split()
		cd.append(d[a[0]][a[2]])
	for i in p_b:
		a=i.split()
		cd1.append(d[a[0]][a[2]])
	for i in range(5):
		a = center_cards[i]
		a = a.split()
		cd2.append(d[a[0]][a[2]])
	result = winner(p_a,p_b,center_cards)
	return render_template('show.html',show=c,show1=cd,show2=cd1,show3=cd2,result=result)

@app.route('/fold')
def fold():
	return redirect("/")




@app.route('/reset')
def reset():
	return redirect("/")


if __name__ == '__main__':
	card_number = ['Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace']
	cards = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}
	suit = ['Diamond','Clubs','Hearts','Spades']
	d={'Two':{"Clubs":"20.png","Diamond":"21.png","Hearts":"22.png","Spades":"23.png"},"Three":{"Clubs":"30.png","Diamond":"31.png","Hearts":"32.png","Spades":"33.png"},"Four":{"Clubs":"40.png","Diamond":"41.png","Hearts":"42.png","Spades":"43.png"}
		,"Five":{"Clubs":"50.png","Diamond":"51.png","Hearts":"52.png","Spades":"53.png"},"Six":{"Clubs":"60.png","Diamond":"61.png","Hearts":"62.png","Spades":"63.png"},"Seven":{"Clubs":"70.png","Diamond":"71.png","Hearts":"72.png","Spades":"73.png"}
		,"Eight":{"Clubs":"80.png","Diamond":"81.png","Hearts":"82.png","Spades":"83.png"},"Nine":{"Clubs":"90.png","Diamond":"91.png","Hearts":"92.png","Spades":"93.png"},"Ten":{"Clubs":"T0.png","Diamond":"T1.png","Hearts":"T2.png","Spades":"T3.png"}
		,"Jack":{"Clubs":"J0.png","Diamond":"J1.png","Hearts":"J2.png","Spades":"J3.png"},"Queen":{"Clubs":"Q0.png","Diamond":"Q1.png","Hearts":"Q2.png","Spades":"Q3.png"},"King":{"Clubs":"K0.png","Diamond":"K1.png","Hearts":"K2.png","Spades":"K3.png"}
		,"Ace":{"Clubs":"A0.png","Diamond":"A1.png","Hearts":"A2.png","Spades":"A3.png"}}
	m = {8:"Straight Flush",7:"Four of a kind",6:"Full house",5:"Flush",4:"Straight",3:"Three of a kind",2:"Two pairs",1:"Pair",0:"High Card"}
	deck=[]
	for i in suit:
		for j in cards.keys():
			deck.append(j+' of '+i)
	random.shuffle(deck)
	p_a = []
	p_b = []
	center_cards = []
	app.config['DEBUG']=True
	app.run()
