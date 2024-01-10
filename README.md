 ## Five Year Cost of Ownership

According to the US census, 91.9% of households have at least one vehicle [usc22]. One of the most expensive items that an average person spends in their lifetime is a vehicle [bus19]. There are currently three major types of cars based on fuel types currently on the market today. They are the internal combustion engines vehicles, internal combustion engines with supplemental battery vehicles or hybrids, and fully electric vehicles or evs [car24]. Arguments have been made to encourage the purchase of evs over traditional internal combustion engine cars that burns fuel and increases carbon dioxide emissions. The environmental protection agency reported that of the 5,586 metric tons of carbon dioxide emissions in the United States, 29% of the Greenhouse gas emission is produced by transportation [epa22]. To combat the increase in Greenhouse gasses, on December 8, 2021, President Biden sign an executive order aiming to end purchases of vehicles that produce emission by the federal government by 2027 for light-duty vehicles (10,000 pounds or 4,536 kg [epa23]) and by 2035 for other vehicles in a push to create a clean energy economy[whi21]. This was done in hopes of encouraging the increase in the number of all electric vehicles [nyt23].

Ultimately, it was found in a 2022 survey, the fuel efficiency, safety and low price was the most important consideration when purchasing a new vehicle [stat22]. What many do not account for is the hidden cost of buying a vehicle is the cost of ownership. There exist several websites that calculate a 5 year estimate for the cost of ownership [aaa, kel, edu] with non-existent api’s or restricted access to them based on commercial usage. For the purpose of this project, data was extracted from the Edumunds database. Tables from the html pages were extracted from a subset of 2023 vehicle data using a python script[kwa24]. The data was converted and saved as cvs files in the Resources folder. The file analysis_5year_ownership_all.ipynb contains the analysis of the yearly cost of ownership for five years for a new 2023 internal combustion engine cars or traditional gas cars, hybrid and electric cars which reads the Edmunds.csv, Edmunds_hybrid.csv and Edmunds_ev.csv data files. The data extracted was confined to only cars, specifically sedans and SUVs, from the model year 2023 due to the limiting number of models and data available of fully electric cars in prior years. The actual cost of ownership will vary from person to person and on what assumptions the databases use assumes. The seven main factors for the cost of ownership included in this analysis are taxes and fees, fuel, maintenance, repairs, financing costs or interest, insurance premiums and depreciation.
Edumonds assumes an average deprecation of 23.5% of the manufacturer’s suggested retail price for the first year of ownership and a 60% deprecation in five years. They also assume that a typical person drives 15,000 miles/year and that the car is financed for 60 months with 10% of the cost of the vehicle down. The price of fuel or electricity and the amount of taxes paid depends on the location and for the purpose of this analysis Mid-Michigan is used. 


<figure>
<p align="center">
<img src="YearlyCostOfOwnership.pdf" width= "200">
<figure>
<p align="center">
<img src="cost_per_mile.pdf" width= "200">


<figure>
<p align="center">
<img src="depreciation. pdf" width= "200">

<figure>
<p align="center">
YearlyPercentageOfCost.pdf. pdf" width= "200">


## References 

[usc22] U.S. Census Bureau 5-Year American Community Survey (2018-2022) https://data.census.gov/table/ACSDP5Y2022.DP04?g=040XX00US15&tid=ACSDP5Y2022.DP04
[bus19] Knueven, L. "The 7 most expensive things you’ll ever pay for, according to financial planners." Business Insiderhttps://www.businessinsider.com/personal-finance/most-expensive-things-americans-will-pay-for-2019-8, Aug 15, 2019.
[epa23] United States Environmental Protection Agency https://www.epa.gov/moves/how-does-moves-define-light-duty-trucks
[car24] "Powertrains & fuel types explained", https://www.carmax.com/research/powertrains-and-fuel-types
[epa22] "Inventory of U.S. Greenhouse Gas Emissions and Sinks". https://www.epa.gov/ghgemissions/inventory-us-greenhouse-gas-emissions-and-sinks
[whi21] "FACT SHEET: President Biden Signs Executive Order Catalyzing America’s Clean Energy Economy Through Federal Sustainability The White House briefing room statements and release" https://www.whitehouse.gov/briefing-room/statements-releases/2021/12/08/fact-sheet-president-biden-signs-executive-order-catalyzing-americas-clean-energy-economy-through-federal-sustainability/, Dec 8, 2021.
[nyt23] Tankersley, J,  Swanson, A., Ewing, J,  and  Davenport, C.
"A New Law Supercharged Electric Car Manufacturing, but Not Sales"
https://www.nytimes.com/2023/11/08/business/energy-environment/electric-vehicles-biden.html
[lin17]  Armstrong, M. Global Consumer Survey 2018 "Most Important Factors When Buying a Car." https://www.statista.com/chart/13075/most-important-factors-when-buying-a-car/
[aaa] https://www.aaa.com/autorepair/drivingcosts
[kel] https://www.kbb.com/new-cars/total-cost-of-ownership/
[edm] https://www.edmunds.com/tco.html
[kwa24] https://github.com/ekfrib23/project1-ev-ice/read.py
	  https://github.com/ekfrib23/project1-ev-ice/ was used for the 	  initial commits to github for this analysis


