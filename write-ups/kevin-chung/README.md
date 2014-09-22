Kevin Chung - Recon 100
========================
## Challenge

> **Description:** Find a picture of me that's from before I was a high school student. Submit the URL to the file on the internet
>
> If you find an alternative to the file I'm thinking of, PM it to me on IRC and I'll consider it but use this site to check if it's right first :)
> 
> **Hints:** Just because it was before I started high school doesnt mean I wasn't in high school
> 
> **Author:** ColdHeat
>
> **Solvers:** 111

## Solution - Step by Step
In my opinion, this was the easiest recon of the ctf because the description told us _exactly_ what we needed to find. Sure we don't really know who Kevin Chung is, but being slightly racist and going to [the judges page](https://ctf.isis.poly.edu/judges) gave us a good idea of who to look for.

The first step was to do a little bit of research about Kevin Chung to find out where we could look to find a picture from his past. Probably the most useful result for this challenge was his [Linkedin profile](https://www.linkedin.com/pub/kevin-chung/50/971/2b3) and Facebook profile, which helped us figure out approximately where he lived and what he was up to during and before high school. 

One of my teammates realized he had one mutual friend with Kevin on Facebook and was able to browse through most of his pictures and information. He certainly found more than one picture of Kevin from his Facebook account that was from his pre-high school days, but we were given the response of "Incorrect" when submitting these as flags. So we PM'd ColdHeat on the CSAW IRC channel insisting that these pictures should count. He coldly said no.

Next we tried utilizing Google's awesome filename search feature by trying terms like `kevin chung filetype:*.jpg` and `kevin chung filetype:*.png`, but this was not too useful.

Then we thought we should look into his high school because we thought we could find a baby picture from their yearbook or graduation ceremony or something like that. So from the LinkedIn information, we searched for Staten Island High School 2011 graduation which is when we stumbled upon [a picture gallery from the ceremony](http://photos.silive.com/4499/gallery/staten_island_high_school_graduations_2011/index.html#/0). Convinced that one of the pictures would work, we submitted literally every image that had or seemed to have an Asian in them. This didn't work either.

Next we found the [school site](http://www.siths.org/) and looked for some type of picture gallery of the students and/or events from the school's history. After we found their [photo album](http://www.siths.org/apps/album/), we figured we would be interested in pictures from 2011 (Kevin's graduation) and previous. Then we saw a high school info night and a [picture with a young Asian boy](http://www.siths.org/apps/album/#albumREC_ID=24883&s=0&photoIdx=2) in it and thought that had to be it! It was the year before he started going to school, so it seemed _highly_ likely that his picture would be there as well as satisfy the pre-high school requirement. But we were wrong again.

After almost leaving the site and trying to look elsewhere, I figured I should at least look through the other pictures first. So I tried the freshman orientation album next and there were some pictures with young Asian boys! So I began rapidly submitting every image that met this criterion and eventually I found [this one](http://www.siths.org/album/48915/23451.jpg). I really didn't think that image would be the winner because of how young Kevin looks in it, but sure enough that was what Kevin was looking for.

## Thoughts and Considerations
### Social Engineering
I found this type of recon interesting and different from past Recon challenges from the CSAW CTFs. It almost seemed like it could've been a social engineering challenge, and that's kind of what it turned into when kids got desperate and realized they knew childhood friends or family of Kevin. That being said, I think a social engineering category could and should be added to future CTFs that could have a similar description, except the picture wouldn't be online, but instead you'd have to get a scanned copy or picture of some physical thing and submit it as evidence of your finding. You would have to social engineer relatives and friends of the victim in order to get the proper information the challenge requires. 

I see how this may bring up a legal and possibly ethical issue, but it would still make for a really fun, interesting and different challenge.

### Bots and AI
Because of how specific this challenge was and how much guessing happened, it seems like a bot with some basic AI could do a decent job at this. You would give it the images of Kevin you know are definitely him, and have it submit links to images that the AI identifies as possibly being him. Or just have it submit every image having to do with his high school that has an Asian in the picture.

## Flag
`http://www.siths.org/album/48915/23451.jpg`
