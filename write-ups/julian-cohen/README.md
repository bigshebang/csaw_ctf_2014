Julian Cohen - Recon 100
========================
## Challenge

> **Description:** Figure out how to get Julian to go on a date with you.
> 
> **Hints:** Julian uses OkCupid
> 
> **Author:** HockeyInJune
>
> **Solvers:** 331

## Solution
On Friday night my teammates had attempted this challenge but after seeing that it had the fewest solves among recons and with my previous CSAW CTF experience, I figured there would be a hint released at some point. So I waited for that before even starting.

Once we got the OkCupid hint we went hard with google on OkCupid. Then we figured it would be smart to just search for users by name to try seeing if they had created an account for Julian. We obviously know his nickname is HockeyInJune, so that helped give us more ideas and things to search for on their site. One thing that really messed me up and pissed me off was how terrible the OkCupid search interface was. After every search I made, it reset the location filter to "within 25 miles of me", even after I had just changed it to "Anywhere". I'm not sure if the organizers purposely chose OkCupid because of its terrible search UI, but it definitely made this challenge harder for me. I was unable to find a HockeyInJune account and spent too much time searching for an account with Julian Cohen in it without good results.

After a few hours of being away from this challenge, my teammate decided he would try searching again. I warned him about the abomination of a search interface that OkCupid had, but he managed to find a user named [HockeyInJune](http://www.okcupid.com/profile/hockeyinjune). I was in such disbelief, because I didn't find that profile even though I had searched with the same keyword.

Next when we tried to click the profile from the search, it required us to sign in, so we made an account. Naturally, we made a female account interested in males of age 22 and from NY, because we assumed it would be a good match for Julian's profile. However, after signing up and going to the link of the search result and searching manually again, we did not see this profile come up. We can see the account when not logged in, but cannot see it after logging in? WTF!

After some rage and thought, I had an idea. I figured that maybe the profile we wanted was not a male interested in females, which is who OkCupid would match us with. Then I returned to our favorite search interface and changed the "everybody" filter to varying values, ultimately finding that this account was a female interested in males. So after changing our account to a male interested in females, we were able to view the profile's page to get the correct flag of `flowers_and_wine_will_get_me`.

Once we saw some writeups, we realized that OkCupid accounts can be easily searched/enumerated if you know the scheme by which they are located on the site. The scheme is `/profile/YOUR_PROFILE_NAME_HERE`. If we had known this, we wouldn't have had to create an account or finagle the amazing OkCupid search engine. But rather we could have just visited `www.okcupid.com/profile/hockeyinjune`, gotten the flag and been done with the atrocity that is OkCupid.

However, this solution was not completely correct. We received full points, but after talking to ColdHeat and some mods in the CSAW IRC channel, they revealed that there were actually two OkCupid accounts: a real one and a fake one. The organizers had created the real profile, but some troll created the fake one and added an incorrect flag to the profile. But the mods trolled the troll and actually started accepting this fake flag, making the challenge a little easier. Isn't it great when trolls fail?

ColdHeat also told us the [real profile](http://www.okcupid.com/profile/TheJulianCohen) so we could find the _real_ flag. But, the way they created the profile you did have to create an account to easily view it. The real flag was `julian_will_not_date_you_sorry`.

## Thoughts and Considerations
### Counter trolling
This challenge and the fuzyll recon challenge each faced the problem of competitors planting false flags([here](https://www.youtube.com/watch?v=PXFsGdnAYkg), [here](https://www.youtube.com/channel/UCdvlx_HsXFEKvlthf4odvbg/discussion), and [here](http://www.dotabuff.com/matches/905568116)). This can be difficult to deal with because it's nearly impossible to moderate due to the unregulated and anonymous environment the internet allows. The organizers of this CTF reacted well though in my opinion. The fake flag on OkCupid was just about as hard to find as the original and it was only a 100 point challenge, so expanding the accepted flags was probably the best choice to make. The fake fuzyll challenge flags were almost obviously fake because of where they were posted, how easy they were to find, and the time stamp associated with them. So it was a good choice to leave those alone.

Overall, I don't think fake flag planting was very detrimental to this CTF. But it could pose a problem in future CTFs if trolls continue to troll due to the difficulty involved with preventing and monitoring it as well as with deciphering between real and fake flags as a competitor.

### OkCupid...
After using OkCupid just to find one user and view their profile, I despise their site. Besides their awful search interface, they don't validate emails of users when signing up and somehow they have this idea that 9 character entirely lowercase letter passwords are the ["best ever"](http://imgur.com/uykNP64). The amount of cringe is unreal.

## Flags
Real flag: `julian_will_not_date_you_sorry`

Fake flag: `flowers_and_wine_will_get_me`
