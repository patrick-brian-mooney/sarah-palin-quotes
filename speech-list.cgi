#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv, os

print("""Content-Type: text/html; charset=utf-8

<!doctype html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
<link rel="stylesheet" type="text/css" href="http://patrickbrianmooney.nfshost.com/~patrick/css/skeleton-normalize.css" />
<link rel="stylesheet" type="text/css" href="http://patrickbrianmooney.nfshost.com/~patrick/css/skeleton.css" />
<link rel="stylesheet" type="text/css" href="http://patrickbrianmooney.nfshost.com/~patrick/css/content-skel.css" />
<link rel="stylesheet" type="text/css" href="http://patrickbrianmooney.nfshost.com/~patrick/css/pullquotes.css" />
<link rel="pgpkey" type="application/pgp-keys" href="/~patrick/505AB18E-public.asc" />
<link rel="author" href="http://plus.google.com/109251121115002208129?rel=author" />
<link rel="sitemap" href="/sitemap.xml" />
<link rel="home" href="/~patrick/projects/sarah-palin/" title="Home page" />
<link rel="meta" type="application/rdf+xml" title="FOAF" href="/~patrick/foaf.rdf" />
<meta name="foaf:maker" content="foaf:mbox_sha1sum '48a3091d919c5e75a5b21d2f18164eb4d38ef2cd'" />
<link rel="profile" href="http://microformats.org/profile/hcalendar" />
<link rel="profile" href="http://gmpg.org/xfn/11" />
<link rel="icon" type="image/x-icon" href="/~patrick/icons/favicon.ico" />
<title>List of Sources Used in the Sarah Palin Gibberish Quiz</title>
<meta name="generator" content="Bluefish 2.2.5" />
<meta name="author" content="Patrick Mooney" />
<meta name="dcterms.rights" content="Copyright © 2016 Patrick Mooney" />
<meta name="description" content="Can Sarah Palin pass a crowdsourced Turing test?" />
<meta name="rating" content="general" />
<meta name="revisit-after" content="3 days" />
<meta name="date" content="2016-01-28T14:57:15-0800" />
<meta property="fb:admins" content="100006098197123" />
<meta property="og:title" content="List of Sources Used in the Sarah Palin Gibberish Quiz" />
<meta property="og:type" content="website" />
<meta property="og:url" content="http://patrickbrianmooney.nfshost.com/~patrick/projects/sarah-palin/speech-list.cgi" />
<meta property="og:image" content="http://patrickbrianmooney.nfshost.com/~patrick/icons/gear-large.png" />
<meta property="og:description" content="List of sources used in my quiz, 'Sarah Palin Quote, or Random Algorithmic Gibberish?'" />
<meta name="twitter:card" content="summary" />
<meta name="twitter:site" content="@patrick_mooney" />
<meta name="twitter:creator" content="@patrick_mooney" />
<meta name="twitter:title" content="List of Sources Used in the Sarah Palin Quiz" />
<meta name="twitter:description" content="List of sources used in my quiz, 'Sarah Palin Quote, or Random Algorithmic Gibberish?'" />
<meta name="twitter:image:src" content="http://patrickbrianmooney.nfshost.com/~patrick/icons/gear-large.png" />
</head>

<body><div class="container">
<h1>List of Sources Used in <q>Sarah Palin Quote, or Random Algorithmic Gibberish?</q></h1>

<p>This page lists all of the sources that are used in <a rel="me" href="index.cgi">my quiz</a> <q>Sarah Palin Quote, or Random Algorithmic Gibberish?</q> These sources contribute to the quiz in two ways:</p>

<ol>
<li>By being sources from which Sarah Palin quotes are directly drawn.</li>
<li>By being texts on which the text generator that generates algorithmic gibberish is trained.</li>
</ol>

<h3 id="perfect">Are these perfect, exact transcriptions?</h3>

<p>No. For one thing, transcribing from verbal speech to written text already embeds a large number of small- and medium-scale assumptions about meaning. For another thing, I didn't make these transcriptions myself, and haven't made more than a cursory attempt to verify that they are accurate—the Sarah Palin Gibberish Quiz is a quick project I threw together, not a real survey with real-world social-science survey methodology. For another thing, these texts have undergone a minimal textual massaging to make them more compatible with the kinds of textual processing that needs to happen for this quiz to occur. These are genuinely minor changes—replacing of three periods with the Unicode ellipsis character, for instance, or removing the parts of the transcript indicating audience feedback, as the focus of this quiz is Palin's own words—and I have tried to ensure that no real distortions of meanings occur. Nevertheless, if you have feedback on the accuracy of transcriptions, or on other matters, or have other suggestions, please get in touch with me; there is contact information at the bottom of this page.</p>

<h2 id="source-list">Current sources</h2>
<ul>""")

openers_to_discard = ['in her', 'in a', 'at a'] # Kind of a hack, but oh well, it's a small issue

with open('speeches/sources.csv') as f:
    header = f.readline()               # Yeah, ignore that line.
    reader=csv.reader(f)
    for row in reader:
        local_filename = row[0]
        description = row[1]
        for which_opener in openers_to_discard:
            if description.lower().startswith(which_opener):
                description = description[1 + len(which_opener) :]
        url = row[2]
        print("""<li><a href="%s">%s</a> (or <a href="https://github.com/patrick-brian-mooney/sarah-palin-quotes/blob/master/speeches/%s">see the exact transcript the quiz uses</a>)</li>""" % (url, description, local_filename))


print("""</ul>
<h2>But that's a small list!</h2>

<p>Indeed. Even <a rel="nofollow" href="https://sarahpalininformation.wordpress.com/2010/04/17/sarah-palin-speaks-at-charity-of-hope-fundraiser-in-hamilton-ontario/">Sarah Palin fans complain</a> that it's hard to find transcripts of her speaking engagements. A cynical response to this might involve believing that there just aren't that many times that Sarah Palin speaks in public where she doesn't sound batshit crazy. Alternately, maybe it's just that no one actually cares enough about the words that she speaks to bother to transcribe them in full. Maybe it's something else entirely. I'll let you come to your own conclusions..</p>

<p>However, if you know of other <strong> reliable, accurately transcribed, not-trivial-in-length</strong> sources, please let me know <a rel="me" href="https://gnusocial.no/p">on GNUsocial</a> or <a rel="me" href="http://twitter.com/patrick_mooney">on Twitter</a> or <a rel="me" href="http://patrickbrianmooney.nfshost.com/~patrick/personal.html#other-web">elsewhere online</a>.</p>

<p class="status vevent vcard"><a rel="me author" class="url location" href="#">This web page</a> is copyright © 2016 by <span class="fn">Patrick Mooney</span>. <abbr class="summary description" title="Description of Patrick Mooney's technical projects last updated">Last update to this HTML file</abbr>: <abbr class="dtstart" title="2016-01-28">28 January 2016</abbr>.</p>
</footer>
</div></body>
</html>""")