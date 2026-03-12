#!/usr/bin/env python3
_B='rockyou.txt'
_A=True
import itertools,string,os,sys,random,time,requests,hashlib,gzip,shutil,math,re,argparse
def banner():print('\n\n    ______                      __   _  __\n  / ____/______  ______  _____/ /_ | |/ /\n / /   / ___/ / / / __ \\/ ___/ __ \\|   / \n/ /___/ /  / /_/ / / / / /__/ / / /   |  \n\\____/_/   \\__,_/_/ /_/\\___/_/ /_/_/|_|  \n\n\n          ⚡ CrunchX Wordlist Framework ⚡\n\nCreated By : Hackerk17 💻⚡\n_________________________________________________\n_________________________________________________\n\n')
def loading(msg):
	for A in range(3):print(msg+'.'*(A+1));time.sleep(.5)
def save(generator,count,output):
	A=output;loading('⚙ Generating wordlist');B=0
	with open(A,'w')as C:
		for D in generator:
			C.write(D+'\n');B+=1
			if B>=count:break
	print('\n✅ Successfully generated ❗❗');print('📂 Saved ->',A)
def pattern_gen(pattern):
	A=pattern
	while _A:yield A;yield A.capitalize();yield A.upper()
def smart_guess(name):
	A=name;C=['123','1234','@123','2024','2025','!','@$','@#','@@$$','@@$$#','321','456','789','@$#']
	while _A:
		for B in C:yield A+B;yield A.capitalize()+B;yield A+'_'+B;yield A+'.'+B
def random_password():
	A=string.ascii_letters+string.digits+'!@#$%'
	while _A:yield''.join(random.choice(A)for B in range(10))
def mask_gen(mask):
	B=mask;D={'?l':string.ascii_lowercase,'?u':string.ascii_uppercase,'?d':string.digits,'?s':'!@#$%'};C=[];A=0
	while A<len(B):
		if B[A]=='?'and A+1<len(B):
			E=B[A:A+2]
			if E in D:C.append(D[E]);A+=2;continue
		C.append(B[A]);A+=1
	for F in itertools.product(*C):yield''.join(F)
def company_osint(company):
	A=company;B=[A,A+'123',A+'2024',A+'2025',A+'admin',A+'login',A+'portal',A+'Administrator',A+'2026',A+'Guest']
	while _A:
		for C in B:yield C
def crawl_words(url):
	try:
		print('🕷 Crawling website');A=requests.get(url,timeout=10);B=re.findall('[A-Za-z]{4,}',A.text);C=list(set(B))
		while _A:
			for D in C:yield D.lower()
	except:print('❌ Crawl failed')
def entropy(password):
	B=password;A=0
	if re.search('[a-z]',B):A+=26
	if re.search('[A-Z]',B):A+=26
	if re.search('[0-9]',B):A+=10
	if re.search('[!@#$%]',B):A+=5
	C=len(B)*math.log2(A if A else 1);print('📊 Entropy:',round(C,2),'bits')
def crack_hash(hash_value,wordlist,hash_type):
	B=hash_type;print('🔓 Starting hash cracking')
	try:
		with open(wordlist,'r',errors='ignore')as D:
			for A in D:
				A=A.strip()
				if B=='md5':C=hashlib.md5(A.encode()).hexdigest()
				elif B=='sha1':C=hashlib.sha1(A.encode()).hexdigest()
				elif B=='sha256':C=hashlib.sha256(A.encode()).hexdigest()
				else:print('Unsupported hash type');return
				if C==hash_value:print('\n✅ Password Found:',A);return
		print('❌ Password not found')
	except:print('Error reading wordlist')
def kali_rockyou():
	B='/usr/share/wordlists/rockyou.txt';A='/usr/share/wordlists/rockyou.txt.gz'
	if os.path.exists(B):print('✅ RockYou already installed')
	elif os.path.exists(A):
		C=input('RockYou compressed. Unzip? (yes/no): ')
		if C.lower()=='yes':
			with gzip.open(A,'rb')as D:
				with open(_B,'wb')as E:shutil.copyfileobj(D,E)
			print('✅ Extracted')
def download():
	print('\n\n1 📥 RockYou (~134MB)\n2 📥 SecLists (~500MB)\n\n');C=input('Select: ');D=input('Proceed download? (yes/no): ')
	if D!='yes':return
	if C=='1':loading('⬇ Downloading RockYou');A='https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt';B=requests.get(A);open(_B,'wb').write(B.content);print('✅ RockYou downloaded')
	if C=='2':loading('⬇ Downloading SecLists');A='https://github.com/danielmiessler/SecLists/archive/refs/heads/master.zip';B=requests.get(A);open('seclists.zip','wb').write(B.content);print('✅ SecLists downloaded')
def menu():
	E='Output: ';D='Count: '
	while _A:
		print('\n\n1 🔐 Pattern Wordlist\n2 🤖 Smart Password Guess\n3 🎭 Mask Attack\n4 🎲 Random Passwords\n5 🏢 Company OSINT Wordlist\n6 🕷 Website Wordlist\n7 📊 Password Entropy\n8 📦 Download Wordlists\n9 🔓 Hash Cracker\n0 🚪 Exit\n\n');C=input('Select option: ')
		if C=='1':F=input('Pattern: ');A=int(input(D));B=input('Output file: ');save(pattern_gen(F),A,B)
		elif C=='2':G=input('Name: ');A=int(input(D));B=input(E);save(smart_guess(G),A,B)
		elif C=='3':H=input('Mask: ');A=int(input(D));B=input(E);save(mask_gen(H),A,B)
		elif C=='4':A=int(input(D));B=input(E);save(random_password(),A,B)
		elif C=='5':I=input('Company: ');A=int(input(D));B=input(E);save(company_osint(I),A,B)
		elif C=='6':J=input('URL: ');A=int(input(D));B=input(E);save(crawl_words(J),A,B)
		elif C=='7':K=input('Password: ');entropy(K)
		elif C=='8':kali_rockyou();download()
		elif C=='9':L=input('Enter hash: ');M=input('Hash type (md5/sha1/sha256): ');N=input('Wordlist file: ');crack_hash(L,N,M)
		elif C=='0':sys.exit()
def cli():
	A=argparse.ArgumentParser();A.add_argument('-p','--pattern');A.add_argument('-c','--count',type=int);A.add_argument('-o','--output');B=A.parse_args()
	if B.pattern:save(pattern_gen(B.pattern),B.count,B.output)
def main():
	banner()
	if len(sys.argv)>1:cli()
	else:menu()
if __name__=='__main__':main()