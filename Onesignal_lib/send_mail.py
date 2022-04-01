from Onesignal import  Mailer

mailer=Mailer("dbe9d90b-3455-4947-98f2-f27cc387e826","ZmJhMDBkMjMtNDdjZC00Y2Q3LTllMDItYTA4MTA1ZjZhZThj","en")
subject= "cat facts"
body= "<html><head>Welcome to Cat Facts</head><body><h1>Welcome to Cat Facts<h1><h4>Learn more about everyone's favorite furry companions!</h4><hr/><p>Hi Nick,</p><p>Thanks for subscribing to Cat Facts! We can't wait to surprise you with funny details about your favorite animal.</p><h5>Today's Cat Fact (March 27)</h5><p>In tigers and tabbies, the middle of the tongue is covered in backward-pointing spines, used for breaking off and gripping meat.</p><a href='https://catfac.ts/welcome'>Show me more Cat Facts</a><hr/><p><small>(c) 2018 Cat Facts, inc</small></p><p><small><a href='[unsubscribe_url]'>Unsubscribe</a></small></p></body></html>"
mailer.send_mail(body,subject,"6392d91a-b206-4b7b-a620-cd68e32c3a76")