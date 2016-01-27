#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sentence_generator import *       # https://github.com/patrick-brian-mooney/markov-sentence-generator
import glob

print("""Content-Type: text/html; charset=utf-8

<!doctype html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
<link rel="stylesheet" type="text/css" href="http://patrickbrianmooney.nfshost.com//~patrick/css/skeleton-normalize.css" />
<link rel="stylesheet" type="text/css" href="http://patrickbrianmooney.nfshost.com//~patrick/css/skeleton.css" />
<link rel="stylesheet" type="text/css" href="http://patrickbrianmooney.nfshost.com//~patrick/css/content-skel.css" />
<link rel="pgpkey" type="application/pgp-keys" href="http://patrickbrianmooney.nfshost.com/~patrick/505AB18E-public.asc" />
<link rel="author" href="http://plus.google.com/109251121115002208129?rel=author" />
<link rel="sitemap" href="/sitemap.xml" />
<link rel="home" href="http://patrickbrianmooney.nfshost.com/~patrick/ta/w16/" title="Home page" />
<link rel="meta" type="application/rdf+xml" title="FOAF" href="http://patrickbrianmooney.nfshost.com/~patrick/foaf.rdf" />
<meta name="foaf:maker" content="foaf:mbox_sha1sum '48a3091d919c5e75a5b21d2f18164eb4d38ef2cd'" />
<link rel="profile" href="http://microformats.org/profile/hcalendar" />
<link rel="profile" href="http://gmpg.org/xfn/11" />
<link rel="icon" type="image/x-icon" href="http://patrickbrianmooney.nfshost.com/~patrick/icons/favicon.ico" />
<title>Sarah Palin Quote, or Random Algorithmic Gibberish?</title>
<meta name="generator" content="Bluefish 2.2.5" />
<meta name="author" content="Patrick Mooney" />
<meta name="dcterms.rights" content="Copyright © 2016 Patrick Mooney" />
<meta name="description" content="A quick quiz I threw together during a bout with insomnia." />
<meta name="rating" content="general" />
<meta name="revisit-after" content="3 days" />
<meta name="date" content="2016-01-27T12:18:07-0800" />
<meta property="fb:admins" content="100006098197123" />
<meta property="og:title" content="Sarah Palin Quote, or Random Algorithmic Gibberish?" />
<meta property="og:type" content="website" />
<meta property="og:url" content="FIXME" />
<meta property="og:image" content="http://patrickbrianmooney.nfshost.com/~patrick/icons/gear-large.png" />
<meta property="og:description" content="A quick quiz I threw together during a bout with insomnia." />
<meta name="twitter:card" content="summary" />
<meta name="twitter:site" content="" />
<meta name="twitter:creator" content="@patrick_mooney" />
<meta name="twitter:title" content="Sarah Palin Quote, or Random Algorithmic Gibberish?" />
<meta name="twitter:description" content="A quick quiz I threw together during a bout with insomnia." />
<meta name="twitter:image:src" content="http://patrickbrianmooney.nfshost.com/~patrick/icons/gear-large.png" />

</head>

<body><div class="container">
<h1>Sarah Palin Quote, or Random Algorithmic Gibberish?</h1>""")

the_list = []
for which_file in glob.glob('speeches/*txt'):
    the_list = the_list + word_list(which_file)
starts, the_mapping = buildMapping(the_list, markov_length=2)

print('<p>%s</p>' % gen_text(the_mapping, starts, markov_length=2, sentences_desired=5, paragraph_break_probability=0) )
print("""</div></body>
</html>""")
