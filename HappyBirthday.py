import time

def TimeToDrink():
	print("Hey Conrad, how old are you today?")
	age = raw_input()
	print("Wow you are" + age + "!, that is amazing you must be such a mature man now.\n")
	print("How many shots have you had tonight?")
	shots = raw_input()
	moreshots = str(float(age)-float(shots)) 
	print("Gotcha, so that means you need to take " + moreshots + " more shots if you want to die tonight!\n#TopTip #ProTip #HaveFun #YoY #nudLife")

	print("\nOk, now for a sobriety test.\n")
	print("What is the FFT of the sound waves propegating in a 5 foot radius of your left ear?\n")
	answer = raw_input()
	print("Visually calculating where your left ear is...")
	time.sleep(3)
	print("Recording Audio...")
	time.sleep(3)
	print("Processing...")
	time.sleep(3)
	print("Performing FFT on recorded audio...")
	time.sleep(5)
	print("Done!\n")
	time.sleep(1) 
	print("Wow you weren't even close buddy, you must be hammered.")
	time.sleep(1)
	print("Rage on. \nThat is all.")
	time.sleep(5)
	print(";)\n HAPPY BIRTHDAY CONRAD!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")	

TimeToDrink()	
