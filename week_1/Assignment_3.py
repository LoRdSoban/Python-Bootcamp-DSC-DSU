import time


# Song: Falling by Trevor daniel

#           even though I don't have any 'last', I really like this song *insert sad nibba voices* :(
song = '''My last made me feel like I would never try again, 
But when I saw you,I felt something I never felt,
Come closer,I'll give you all my love,
If you treat me right baby,I'll give you everything,
My last made me feel like I would never try again,
But when I saw you,I felt something I never felt,
Come closer,I'll give you all my love,
If you treat me right baby,I'll give you everything,
Talk to me,I need to hear you need me like I need ya,
Fall for me,I wanna know you feel how I feel for you, love,
Before you baby,I was numb drowned out pain by pouring up,
Speeding fast on the run,never want to get caught up,
Now you the one that I'm calling,
Swore that I'd never fall again,don't think I'm just talking,
I think I might go all in,no exceptions girl,I need ya,
Think I'm out of my mind,cause I can't get enough,
Only one that I give my time,cause I got eyes for ya,
Might make an exception for ya,cause I been feeling ya,
Think I might be out of my mind,I think that you're the one,
My last made me feel like I would never try again,
But when I saw you,I felt something I never felt,
Come closer,I'll give you all my love,
If you treat me right baby,I'll give you everything,
My last made me feel like I would never try again,
But when I saw you,I felt something I never felt,
Come closer,I'll give you all my love,
If you treat me right, baby,I'll give you everything,
I'll never give my all again,
Cause I'm sick of falling down,
When I open up and give my trust,
They find a way to break it down,
Tear me up inside, and you break me down '''


splittedSong = song.split(",")

print("Falling by Trevor Daniel\n\n")
for lines in splittedSong:
	print(lines)
	time.sleep(.8)