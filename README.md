# OLXstatistics

  Project made to easily follow price trends on polish real estate market. Core of the project is parser which runs daily and uploads data to local database. Next, part of the data is being uploaded to cloud database on Azure server, which Django webapplication creates its models from. 
  
  <p align="center">
  <img src="https://user-images.githubusercontent.com/113203886/196746636-92388b46-4142-4457-9c50-76300260f81a.jpg">
  </p>
  
  I've tried multiple diffferent approaches to gather data from OLX efficiently. At the beggining I used Selenium library but it turned out that scraping 25 000 offers this way was very time-consuming. Looking for better solution I came accross requests library which let's you obtain data from OLX API by making custom GET requests. I found the right request pattern by analysing requests sent by browser during page loading. 
  Now, having dealt with all these issues parser runs daily and gathering the data takes it around 6 minutes which is huge improvement over 6 hours achieved with initial attempts.
